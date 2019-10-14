#!/usr/bin/env python
# Parallel uploads to Amazon AWS S3


try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO
from fnmatch import fnmatch
from gzip import GzipFile
from itertools import chain, imap, islice
import logging
from multiprocessing import JoinableQueue, Process, current_process
from optparse import OptionGroup, OptionParser
import os.path
import re
from ssl import SSLError
import sys
import tarfile
import time
import magic #python-magic
import mimetypes

import boto
from boto.s3.connection import S3Connection
from boto.s3.acl import CannedACLStrings
from boto.utils import compute_md5
e=sys.exit
from pprint import pprint

DONE_RE = re.compile(r'\AINFO:s3-parallel-put\[putter-\d+\]:\S+\s+->\s+(\S+)\s*\Z')

# These content types are amenable to compression
# WISHLIST more types means more internets
GZIP_CONTENT_TYPES = (
	'application/javascript',
	'application/x-javascript',
	'text/css',
	'text/html',
	'text/javascript',
)
GZIP_ALL = 'all'


def repeatedly(func, *args, **kwargs):
	while True:
		yield func(*args, **kwargs)


class FileObjectCache(object):

	def __init__(self):
		self.name = None
		self.file_object = None

	def open(self, name, *args):
		if name != self.name:
			self.name = name
			self.file_object = open(self.name, *args)
		return self

	def __enter__(self):
		return self.file_object

	def __exit__(self, exc_type, exc_value, traceback):
		pass


class Value(object):

	def __init__(self, file_object_cache, content=None, filename=None, md5=None, offset=None, path=None, size=None, bucket_name=None):
		self.file_object_cache = file_object_cache
		self.content = content
		self.filename = filename
		self.md5 = md5
		self.offset = offset
		self.path = path
		self.size = size
		self.bucket_name = bucket_name

	def get_content(self):
		if self.content is None:
			if self.filename:
				with self.file_object_cache.open(self.filename) as file_object:
					file_object.seek(self.offset)
					self.content = file_object.read(self.size)
			elif self.path:
				with open(self.path) as file_object:
					self.content = file_object.read()
			else:
				assert False
		return self.content

	def calculate_md5(self):
		if self.md5 is None:
			self.md5 = compute_md5(StringIO(self.get_content()))
		return self.md5

	def get_size(self):
		if self.size is None:
			if self.content:
				self.size = len(self.content)
			elif self.path:
				self.size = os.stat(self.path).st_size
			else:
				assert False
		return self.size

	def should_copy_content(self):
		return self.bucket_name is None

def excluded(pathname, options):
  for glob in options.include:
	if fnmatch(pathname, glob):
	  return False

  for glob in options.exclude:
	if fnmatch(pathname, glob):
	  return True

  return False

def walk_filesystem(source, options):
	#print 111,source
	#e()
	if os.path.isdir(source):
		for dirpath, dirnames, filenames in os.walk(source):
			if excluded(dirpath, options):
				continue
			for filename in filenames:
				abs_path = os.path.join(dirpath, filename)
				if not os.path.isfile(abs_path):
					continue
				if excluded(filename, options):
					continue
				rel_path = os.path.relpath(abs_path, source)
				key_name = '/'.join([options.prefix] + rel_path.split(os.sep))
				yield (key_name, dict(path=abs_path))
	elif os.path.isfile(source):
		if excluded(source, options):
			return
		key_name = os.path.normpath(os.path.join(options.prefix, source))
		yield (key_name, dict(path=source))


def walk_tar(source, options):
	try:
		tar_file = tarfile.open(source, 'r:')
		for tarinfo in tar_file:
			if tarinfo.isfile():
				path = tarinfo.name
				if excluded(path, options):
					continue
				key_name = os.path.normpath(os.path.join(options.prefix, path))
				filename = source
				offset = tarinfo.offset_data
				size = tarinfo.size
				yield (key_name, dict(filename=filename, offset=offset, path=path, size=size))
			# http://blogs.oucs.ox.ac.uk/inapickle/2011/06/20/high-memory-usage-when-using-pythons-tarfile-module/
			tar_file.members = []
	except tarfile.ReadError:
		tar_file = tarfile.open(source)
		for tarinfo in tar_file:
			if tarinfo.isfile():
				path = tarinfo.name
				if excluded(path, options):
					continue
				key_name = os.path.normpath(os.path.join(options.prefix, path))
				content = tar_file.extractfile(tarinfo).read()
				yield (key_name, dict(content=content, path=path))


def walk_s3(source, options):
	connection = S3Connection(host=options.host, is_secure=options.secure)
	for key in connection.get_bucket(source, validate=False).list():
		if excluded(key.name, options):
			continue
		yield (
			key.name,
			dict(
				bucket_name=key.bucket.name,
				md5=key.etag,
				size=key.size,
				path='%s/%s' % (source, key.name)))


def walker(walk, put_queue, sources, options):
	logger = logging.getLogger('%s[walker-%d]' % (os.path.basename(sys.argv[0]), current_process().pid))
	pairs = chain(*imap(lambda source: walk(source, options), sources))
	#print list(pairs)
	if options.resume:
		done = set()
		for filename in options.resume:
			with open(filename) as file_object:
				for line in file_object:
					match = DONE_RE.match(line)
					if match:
						done.add(match.group(1))
		pairs = ((key_name, args) for key_name, args in pairs if key_name not in done)
	if options.limit:
		pairs = islice(pairs, options.limit)
	for pair in pairs:
		print pair
		put_queue.put(pair)


def put_add(bucket, key_name, value):
	key = bucket.get_key(key_name)
	if key is None:
		return bucket.new_key(key_name)
	else:
		return None


def put_stupid(bucket, key_name, value):
	return bucket.new_key(key_name)


def put_update(bucket, key_name, value):
	key = bucket.get_key(key_name)
	if key is None:
		return bucket.new_key(key_name)
	else:
		# Boto's md5 function actually returns 3-tuple: (hexdigest, base64, size)
		value.calculate_md5()
		if key.etag == '"%s"' % value.md5[0]:
			return None
		else:
			return key


def put_copy(bucket, key_name, value):
	return bucket.copy_key(key_name, value.bucket_name, key_name)


def putter(put, put_queue, stat_queue, options):
	logger = logging.getLogger('%s[putter-%d]' % (os.path.basename(sys.argv[0]), current_process().pid))
	connection, bucket = None, None
	file_object_cache = FileObjectCache()
	# Figure out what content types we want to gzip
	if not options.gzip_type:  # default
		gzip_content_types = GZIP_CONTENT_TYPES
	elif 'all' in options.gzip_type:
		gzip_content_types = GZIP_ALL
	else:
		gzip_content_types = options.gzip_type
	if 'guess' in gzip_content_types:
		# don't bother removing 'guess' from the list since nothing will match it
		gzip_content_types.extend(GZIP_CONTENT_TYPES)
	if options.gzip:
		logger.debug('These content types will be gzipped: %s' % unicode(gzip_content_types))
	while True:
		args = put_queue.get()
		if args is None:
			put_queue.task_done()
			break
		key_name, value_kwargs = args
		#pprint(value_kwargs)
		#pprint(key_name)
		e()
		value = Value(file_object_cache, **value_kwargs)
		should_gzip = False
		try:
			if connection is None:
				connection = S3Connection(is_secure=options.secure, host=options.host)
			if bucket is None:
				bucket = connection.get_bucket(options.bucket, validate=False)
			key = put(bucket, key_name, value)
			if key:
				if value.should_copy_content():
					if options.headers:
						headers = dict(tuple(header.split(':', 1)) for header in options.headers)
					else:
						headers = {}

					content_type = None
					if options.content_type:
						if options.content_type == 'guess':
							content_type = mimetypes.guess_type(value.path)[0]
						elif options.content_type == 'magic':
							content_type = mimetypes.guess_type(value.path)[0]
							if content_type is None:
								content_type = magic.from_file(value.path, mime=True)
						else:
							content_type = options.content_type
						headers['Content-Type'] = content_type

					content = value.get_content()
					md5 = value.md5
					should_gzip = options.gzip and (
						content_type and content_type in gzip_content_types or
						gzip_content_types == GZIP_ALL)
					if should_gzip:
						headers['Content-Encoding'] = 'gzip'
						string_io = StringIO()
						gzip_file = GzipFile(compresslevel=1, fileobj=string_io, mode='w')
						gzip_file.write(content)
						gzip_file.close()
						content = string_io.getvalue()
						md5 = compute_md5(StringIO(content))
					if not options.dry_run:
						key.set_contents_from_string(content, headers, md5=md5, policy=options.grant, encrypt_key=options.encrypt_key)
				logger.info('%s %s> %s' % (
					value.path, 'z' if should_gzip else '-', key.name))
				stat_queue.put(dict(size=value.get_size()))
			else:
				logger.info('skipping %s -> %s' % (value.path, key_name))
		except SSLError as exc:
			logger.error('%s -> %s (%s)' % (value.path, key_name, exc))
			put_queue.put(args)
			connection, bucket = None, None
		except IOError as exc:
			logger.error('%s -> %s (%s)' % (value.path, key_name, exc))
		put_queue.task_done()


def statter(stat_queue, start, options):
	logger = logging.getLogger('%s[statter-%d]' % (os.path.basename(sys.argv[0]), current_process().pid))
	count, total_size = 0, 0
	while True:
		kwargs = stat_queue.get()
		if kwargs is None:
			stat_queue.task_done()
			break
		count += 1
		total_size += kwargs.get('size', 0)
		stat_queue.task_done()
	duration = time.time() - start
	logger.info('put %d bytes in %d files in %.1f seconds (%d bytes/s, %.1f files/s)' % (total_size, count, duration, total_size / duration, count / duration))


def main(argv):
	parser = OptionParser()
	group = OptionGroup(parser, 'S3 options')
	group.add_option('--bucket', metavar='BUCKET',
			help='set bucket')
	group.add_option('--bucket_region', default='us-east-1',
			help='set bucket region if not in us-east-1 (default new bucket region)')
	group.add_option('--host', default='s3.amazonaws.com',
			help='set AWS host name')
	group.add_option('--insecure', action='store_false', dest='secure',
			help='use insecure connection')
	group.add_option('--secure', action='store_true', default=True, dest='secure',
			help='use secure connection')
	parser.add_option_group(group)
	group = OptionGroup(parser, 'Source options')
	group.add_option('--walk', choices=('filesystem', 'tar', 's3'), default='filesystem', metavar='MODE',
			help='set walk mode (filesystem or tar)')
	group.add_option('--exclude', action='append', default=[], metavar='PATTERN', 
			help='exclude files matching PATTERN')
	group.add_option('--include', action='append', default=[], metavar='PATTERN', 
			help='don\'t exclude files matching PATTERN')
	parser.add_option_group(group)
	group = OptionGroup(parser, 'Put options')
	group.add_option('--content-type', default='guess', metavar='CONTENT-TYPE',
			help='set content type, set to "guess" to guess based on file name '
			'or "magic" to guess by filename and libmagic.')
	group.add_option('--gzip', action='store_true',
			help='gzip values and set content encoding')
	group.add_option('--gzip-type', action='append', default=[],
			help='if --gzip is set, sets what content-type to gzip, defaults '
			'to a list of known text content types, "all" will gzip everything.'
			' Specify multiple times for multiple content types. '
			'[default: "guess"]')
	group.add_option('--put', choices=('add', 'stupid', 'update', 'copy'), default='update', metavar='MODE',
			help='set put mode (add, stupid, copy or update)')
	group.add_option('--prefix', default='', metavar='PREFIX',
			help='set key prefix')
	group.add_option('--resume', action='append', default=[], metavar='FILENAME',
			help='resume from log file')
	group.add_option('--grant', metavar='GRANT', default=None, choices=CannedACLStrings,
			help='A canned ACL policy to be applied to each file uploaded.\nChoices: %s' %
			', '.join(CannedACLStrings))
	group.add_option('--header', metavar='HEADER:VALUE', dest='headers', action='append',
					 help='extra headers to add to the file, can be specified multiple times')
	group.add_option('--encrypt-key', action='store_true', default=False, dest='encrypt_key',
			help='use server side encryption')
	parser.add_option_group(group)
	group = OptionGroup(parser, 'Logging options')
	group.add_option('--log-filename', metavar='FILENAME',
			help='set log filename')
	group.add_option('--quiet', '-q', action='count', default=0,
			help='less output')
	group.add_option('--verbose', '-v', action='count', default=0,
			help='more output')
	parser.add_option_group(group)
	group = OptionGroup(parser, 'Debug and performance tuning options')
	group.add_option('--dry-run', action='store_true',
			help='don\'t write to S3')
	group.add_option('--limit', metavar='N', type=int,
			help='set maximum number of keys to put')
	group.add_option('--processes', default=8, metavar='PROCESSES', type=int,
			help='set number of putter processes')
	parser.add_option_group(group)
	options, args = parser.parse_args(argv[1:])
	#pprint(args)
	#e()
	logging.basicConfig(filename=options.log_filename, level=logging.INFO + 10 * (options.quiet - options.verbose))
	logger = logging.getLogger(os.path.basename(sys.argv[0]))
	if len(args) < 1:
		logger.error('missing source operand')
		return 1
	if not options.bucket:
		logger.error('missing bucket')
		return 1
	if not options.bucket_region:
		options.bucket_region = 'us-east-1'
	connection = boto.s3.connect_to_region(options.bucket_region,
	   aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
	   aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
	   is_secure=True,
	   calling_format = boto.s3.connection.OrdinaryCallingFormat(),
	   )
	#walk_filesystem(option=options)
	#e()
	import ssl
	if hasattr(ssl, '_create_unverified_context'):
		 ssl._create_default_https_context = ssl._create_unverified_context
			
	bucket = connection.get_bucket(options.bucket, validate=False)
	del bucket
	del connection
	start = time.time()
	put_queue = JoinableQueue(1024 * options.processes)
	stat_queue = JoinableQueue()
	walk = {'filesystem': walk_filesystem, 'tar': walk_tar, 's3': walk_s3}[options.walk]
	walker_process = Process(target=walker, args=(walk, put_queue, args, options))
	walker_process.start()
	put = {'add': put_add, 'stupid': put_stupid, 'update': put_update, 'copy': put_copy}[options.put]
	putter_processes = list(islice(repeatedly(Process, target=putter, args=(put, put_queue, stat_queue, options)), options.processes))
	for putter_process in putter_processes:
		putter_process.start()
	statter_process = Process(target=statter, args=(stat_queue, start, options))
	statter_process.start()
	walker_process.join()
	for putter_process in putter_processes:
		put_queue.put(None)
	put_queue.close()
	for putter_process in putter_processes:
		putter_process.join()
	stat_queue.put(None)
	stat_queue.close()
	statter_process.join()
	put_queue.join_thread()
	stat_queue.join_thread()


if __name__ == '__main__':
	sys.exit(main(sys.argv))
