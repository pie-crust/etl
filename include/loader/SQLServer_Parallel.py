(cli, conn_pool)=app_init
import os, sys, time, gzip, math, gzip
import boto
import tempfile
import collections
from datetime import datetime
from pprint import pprint as pp
from gzip import GzipFile
try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO
from fnmatch import fnmatch

from itertools import chain, imap, islice
import logging
from multiprocessing import JoinableQueue, Process, current_process
import multiprocessing
from optparse import OptionGroup, OptionParser
import os.path
import re
from ssl import SSLError


import tarfile

import magic #python-magic
import mimetypes

import boto
from boto.s3.connection import S3Connection
from boto.s3.acl import CannedACLStrings
from boto.utils import compute_md5

e=sys.exit

from include.utils import timeit, ctimeit
from include.loader.common.SQLServer import SQLServer

from pubsub import pub

def repeatedly(func, *args, **kwargs):
	while True:
		yield func(*args, **kwargs)
		
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk as new_walk
	
	
class Opt(object):
	def __init__(self):
		pass

chunk_size=10*10<<20

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

class  SQLServer_Parallel(SQLServer):
	@ctimeit
	def __init__(self, **kwargs):
		pp(kwargs)
		#e()
		env= kwargs.get('env')
		kwargs['env']=env.split('_')[0]
		SQLServer.__init__(self, **kwargs)
		self.opt=opt=Opt()
		self.file_names=[]
		self.file_keys=[]
		
		if 1:
			opt.processes	= 10 #multiprocessing.cpu_count() * 4
			opt.walk		= 'filesystem'
			opt.prefix		= 'racct'
			opt.put			= 'update'
			opt.gzip		= True
			opt.secure		= True
			opt.host		= 's3.amazonaws.com'
			opt.bucket		= 'home-pmt-accounting-dev'
			opt.headers		= None
			opt.content_type= None
			opt.dry_run		= False
			opt.grant		= None
			opt.encrypt_key = False
			opt.quiet		= False
			opt.verbose		= True
			opt.lame_duck	= 0
			opt.peek		= 5000
			opt.skip_header = None
			opt.rec_delim= None


		


	def insert_files(self, file_names, out,cfg, skip_header=0, rec_delim=os.linesep):
		self.opt.skip_header = skip_header
		self.opt.rec_delim = rec_delim
		log = logging.getLogger('cli')
		self.scfg, self.tcfg = cfg
		file_object_cache = FileObjectCache()
		start = time.time()
		if 1:
			put_queue = JoinableQueue(1024 * self.opt.processes)
			stat_queue = JoinableQueue()
			#walk = {'filesystem': self.walk_filesystem}[self.opt.walk]
			for file in file_names.file_names:
				put_queue.put(file)	
			
		if 1:
			put = {'update': self.put_update}[self.opt.put]
			putter_processes = list(islice(repeatedly(Process, target=self.putter, args=(put, put_queue, stat_queue)), self.opt.processes))
			for putter_process in putter_processes:
				putter_process.start()
		if 1:
			statter_process = Process(target=self.statter, args=(stat_queue, start))
			statter_process.start()
		
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
	
		#print(3334,file_names.file_names )
		#e()
		out.file_names = ['%s.gz' % os.path.basename(x[0]) for x in file_names.file_names]
		#pp(out.file_names)
		#e()
		out.file_keys = ['%s.gz' % x[0] for x in file_names.file_names]
		out.file_location = os.path.dirname(file_names.file_names[0][0])
		
		
	def put_update(self, bucket, key_name, value):
		key = 'test'
		return key
	def putter(self, put, put_queue, stat_queue):
		self.pid=current_process().pid
		log = logging.getLogger(os.path.basename(sys.argv[0]))
		connection, bucket = None, None
		file_object_cache = FileObjectCache()

		while True:
			args = put_queue.get()
			if args is None:
				put_queue.task_done()
				break
			key_name, value_kwargs = args

			if self.opt.gzip:
				key_name = '%s.gz' %  key_name
			value_kwargs.update(dict(opt=self.opt))
			value = Value(file_object_cache, **value_kwargs)
			try:
				if connection is None:
					connection = S3Connection(is_secure=self.opt.secure, host=self.opt.host)
				if bucket is None:
					bucket = connection.get_bucket(self.opt.bucket, validate=False)
				key = put(bucket, key_name, value)
				if key:
					comp_size=0
					if value.should_copy_content():
						if self.opt.headers:
							headers = dict(tuple(header.split(':', 1)) for header in self.opt.headers)
						else:
							headers = {}
						content = value.get_content()
						if not self.opt.dry_run:
							comp_size = self.insert_content(content, headers)
							
							
					stat_queue.put(dict(key_name=key_name, key_stats=dict(size=value.get_size(), comp_size=comp_size, filename=value.filename, path=value.path)))
				else:
					log.info('skipping %s -> %s' % (value.path, key_name))
			except SSLError as exc:
				log.error('%s -> %s (%s)' % (value.path, key_name, exc))
				put_queue.put(args)
				connection, bucket = None, None
			except IOError as exc:
				log.error('%s -> %s (%s)' % (value.path, key_name, exc))
			put_queue.task_done()
		
	def insert_content(self, content, headers):
		print ('insert_content: [%d], size= %d' % (self.pid, len(content)))

		if 1:
			#print self.conn
			conn=self._connect()
			print self.tcfg
			tbl = cli.get_parsed(ckey='targetTable', cfg=self.tcfg)
			print tbl
			data=[]
			
			linesep= self.scfg['recordDelimiter']
			colsep= self.scfg['columnDelimiter']
			if b"'" in content: 
				content=content.replace(b"'",b"''")
			limit =1000
			rowid=0
			vals=[]
			start_time = time.time()
			cur= conn.cursor()
			for line in [x.strip()  for x in  content.split(linesep)]:
				if line.strip():
					#data.append(line.split(colsep))
					vals.append(','.join(["'%s'" % x if x else 'NULL' for x in line.split(colsep)])) 
					rowid +=1
				if len(vals)==1000:
					stmt = 'INSERT INTO %s VALUES (%s)' % (tbl, '),('.join(vals))
					cur.execute(stmt)
					log.debug('[%d] Read: %d, Inserted: %d ' % (self.pid, rowid, limit))
					vals=[]
			if vals:
				log.debug('[%d] Read: %d, Inserted: %d ' % (self.pid, rowid, limit))
				cur.execute(stmt)
				log.debug('Read: %d, Inserted: %d ' % (rowid, limit))
			conn.commit()
			log.debug('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, rowid, cur.rowcount, round((time.time() - start_time),2)))
			return rowid
	#@api
	@ctimeit
	def __insert_data_chunk_2(self,conn, table, data):
		cur= conn.cursor()
		print conn
		if 1:
			start_time = time.time()
			if data:
				qmarks=('?,' * len(data[0])).strip(',')
				stmt = 'INSERT INTO %s VALUES (%s)' % (table, qmarks)
				pp(stmt)
				#e()
				cur.executemany(stmt , data)
				conn.commit()
				conn.close()
				log.debug('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, len(data), cur.rowcount, round((time.time() - start_time),2)))
			else:
				log.warn('Empty data chunk. Passing...')
				
	def insert_data_chunk_2(self,conn, table, data):
		cur= conn.cursor()
		print conn

		start_time = time.time()
		if data:
			#self.cur.fast_executemany = True
			
			start=0 
			limit =1000
			vals=[]
			stmt=''
			while start<len(data):
				
				for row in data[start:][:limit]:
					vals.append(','.join(["'%s'" % x if x else 'NULL' for x in row])) 
					#print len(row)
					#pp(vals)
				log.debug('Start: %d, limit: %d ' % (start, limit))
				assert vals
				stmt = 'INSERT INTO %s VALUES (%s)' % (table, '),('.join(vals))
				#pp(stmt)
				cur.execute(stmt)
				vals=[]
				
				
				start +=limit
			conn.commit()
			log.debug('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, len(data), cur.rowcount, round((time.time() - start_time),2)))
		else:
			log.warn('Empty data chunk. Passing...')

			
	def statter(self, stat_queue, start):
		log = logging.getLogger(os.path.basename(sys.argv[0]))
		count=total_size=total_comp =0
		self.file_stats={}
		while True:
			kwargs = stat_queue.get()
			if kwargs is None:
				stat_queue.task_done()
				break
			count += 1
			key_name = kwargs.get('key_name')
			self.file_keys.append(key_name)
			self.file_stats[key_name]=kwargs.get('key_stats', {})
			total_size += self.file_stats[key_name]['size']
			total_comp += self.file_stats[key_name]['comp_size']
			
			stat_queue.task_done()
		duration = time.time() - start
		log.info('put %d bytes (%s compressed) in %d files in %.1f seconds (%d bytes/s)' % (total_size, total_comp, count, duration, total_size / duration))

		
	
class Value_sh(object):
	def __init__(self, file_object_cache, content=None, filename=None, md5=None, offset=None, path=None, size=None, bucket_name=None, opt=None):
		self.file_object_cache = file_object_cache
		self.content 	= content
		self.filename 	= filename
		self.bucket_name= bucket_name
		self.md5 	= md5
		self.offset = offset
		self.path 	= path
		self.size 	= size
		self.peek	= opt.peek if opt.peek else 5000
		self.pid	= current_process().pid
		self.skip_header = opt.skip_header if opt.skip_header is not None else 0
		self.rec_delim = opt.rec_delim if opt.rec_delim is not None else os.linesep

	def get_content(self):
		if self.content is None:
			if self.filename:
				if self.offset>=0 and self.size:
					with self.file_object_cache.open(self.filename) as file_object:
						#adjust offset and size
						if 1: #offset
							if not self.offset: # beginning of file
								if self.skip_header: #skip first row
									print self.skip_header
									file_object.seek(self.offset)
									pos = file_object.read(self.peek).find(os.linesep)
									assert pos>-1, 'skip_header: Increase peek size to move offset to EOL.'
									print '[%d][%d]\SKIP_HEADER: %s -> %s, \tSIZE: %s -> %s' % (self.pid, self.offset, self.offset, self.offset+pos, self.size, self.size-pos)
									self.offset=self.offset+pos+len(os.linesep)
									self.size=self.size-pos
									#e()
							else:
								file_object.seek(self.offset)
								pos = file_object.read(self.peek).find(os.linesep)
								assert pos>-1, 'Increase peek size to move offset to EOL.'
								print '[%d][%d]\tOFFSET: %s -> %s, \tSIZE: %s -> %s' % (self.pid, self.offset, self.offset, self.offset+pos, self.size, self.size-pos)

								self.offset=self.offset+pos+len(os.linesep)
								self.size=self.size-pos
						if 1: #size
							file_object.seek(self.offset+self.size)
							contents=file_object.read(self.peek)
							if not contents: #EOF
								pass
							else:
								pos = contents.find(os.linesep)
								assert pos>-1, 'Increase peek size to move offset to EOL.'
								print '[%d][%d]\tsize: %s -> %s' % (self.pid,self.offset, self.size, self.size+pos)
								self.size=self.size+pos

						file_object.seek(self.offset)
						self.content = file_object.read(self.size)
				else:
					raise Exception('Wrong offset [%s] and size [%s]' % (self.offset, self.size))
			elif self.path:
				with open(self.path) as file_object:
					self.content = file_object.read()
			else:
				assert False
		return self.content

class Value(object):
	def __init__(self, file_object_cache, content=None, filename=None, md5=None, offset=None, path=None, size=None, bucket_name=None, opt=None):
		self.file_object_cache = file_object_cache
		self.content 	= content
		self.filename 	= filename
		self.bucket_name= bucket_name
		self.md5 	= md5
		self.offset = offset
		self.path 	= path
		self.size 	= size
		self.peek	= opt.peek if opt.peek else 5000
		self.pid	= current_process().pid
		self.skip_header = opt.skip_header if opt.skip_header is not None else None
		self.rec_delim = opt.rec_delim if opt.rec_delim is not None else None

	def get_content(self):
		assert self.rec_delim
		assert self.skip_header is not None
		assert self.skip_header in [0,1]
		linesep=self.rec_delim
		
		
		if self.content is None:
			if self.filename:
				if self.offset>=0 and self.size:
					with self.file_object_cache.open(self.filename) as file_object:
						#adjust offset and size
						if 1: #offset
							if not self.offset: # beginning of file
							
								if self.skip_header: #skip first row
									file_object.seek(self.offset)
									pos = file_object.read(self.peek).find(linesep)
									assert pos>-1, 'skip_header: Increase peek size to move offset to EOL.'
									print '[%d][%d]\SKIP_HEADER: %s -> %s, \tSIZE: %s -> %s' % (self.pid, self.offset, self.offset, self.offset+pos, self.size, self.size-pos)
									self.offset=self.offset+pos+len(linesep)
									self.size=self.size-pos-len(linesep)
									#e()
							else:
								file_object.seek(self.offset)
								pos = file_object.read(self.peek).find(linesep)
								assert pos>-1, 'OFFSET: Increase peek size to move offset to EOL.'
								print '[%d][%d]\tOFFSET: %s -> %s, \tSIZE: %s -> %s' % (self.pid, self.offset, self.offset, self.offset+pos, self.size, self.size-pos)

								self.offset=self.offset+pos+len(linesep)
								self.size=self.size-pos-len(linesep)
						if 1: #size
							file_object.seek(self.offset+self.size)
							contents=file_object.read(self.peek)
							if not contents: #EOF
								pass
							else:
								pos = contents.find(linesep)
								assert pos>-1, 'SIZE: Increase peek size to move offset to EOL.'
								print '[%d][%d]\tsize: %s -> %s' % (self.pid,self.offset, self.size, self.size+pos)
								self.size=self.size+pos+len(linesep)
						
						file_object.seek(self.offset)
						self.content = file_object.read(self.size)

			elif self.path:
				with open(self.path) as file_object:
					self.offset=0
					
					if self.skip_header: #skip first row
						file_object.seek(self.offset)
						pos = file_object.read(self.peek).find(linesep)
						assert pos>-1, 'skip_header: Increase peek size to move offset to EOL.'
						print '[%d][%d]\PATH/SKIP_HEADER: %s -> %s' % (self.pid, self.offset, self.offset, self.offset+pos)
						self.offset=self.offset+pos+len(linesep)
					file_object.seek(self.offset)
					self.content = file_object.read()
			else:
				assert False

		return self.content


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

class Value_noh(object):
	def __init__(self, file_object_cache, content=None, filename=None, md5=None, offset=None, path=None, size=None, bucket_name=None, opt=None):
		self.file_object_cache = file_object_cache
		self.content 	= content
		self.filename 	= filename
		self.bucket_name= bucket_name
		self.md5 	= md5
		self.offset = offset
		self.path 	= path
		self.size 	= size
		self.peek	= opt.peek if opt.peek else 5000
		self.pid	= current_process().pid
		self.skip_header = opt.skip_header if opt.skip_header is not None else 0
		self.rec_delim = opt.rec_delim if opt.rec_delim is not None else None

	def get_content(self):
		assert self.rec_delim
		
		linesep=self.rec_delim
		if self.content is None:
			if self.filename:
				if self.offset>=0 and self.size:
					with self.file_object_cache.open(self.filename) as file_object:
						#adjust offset and size
						if 1: #offset
							if not self.offset: # beginning of file
								pass
							else:
								file_object.seek(self.offset)
								pos = file_object.read(self.peek).find(linesep)
								assert pos>-1, 'Increase peek size to move offset to EOL.'
								print '[%d][%d]\tOFFSET: %s -> %s, \tSIZE: %s -> %s' % (self.pid, self.offset, self.offset, self.offset+pos, self.size, self.size-pos)

								self.offset=self.offset+pos+len(linesep)
								self.size=self.size-pos-len(linesep)
						if 1: #size
							file_object.seek(self.offset+self.size)
							contents=file_object.read(self.peek)
							if not contents: #EOF
								pass
							else:
								pos = contents.find(linesep)
								assert pos>-1, 'Increase peek size to move offset to EOL.'
								print '[%d][%d]\tsize: %s -> %s' % (self.pid,self.offset, self.size, self.size+pos)
								self.size=self.size+pos+len(linesep)
						
						file_object.seek(self.offset)
						self.content = file_object.read(self.size)

			elif self.path:
				with open(self.path) as file_object:
					self.content = file_object.read()
			else:
				assert False
		return self.content

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
		
class Value_new(object):
	def __init__(self, file_object_cache, content=None, filename=None, md5=None, offset=None, path=None, size=None, bucket_name=None, opt=None):
		self.file_object_cache = file_object_cache
		self.content 	= content
		self.filename 	= filename
		self.bucket_name= bucket_name
		self.md5 	= md5
		self.offset = offset
		self.path 	= path
		self.size 	= size
		self.peek	= opt.peek if opt.peek else 5000
		self.pid	= current_process().pid
		self.skip_header = opt.skip_header if opt.skip_header is not None else 0

	def get_content(self):
		if self.content is None:
			if self.filename:
				if self.offset>=0 and self.size:
					with self.file_object_cache.open(self.filename) as file_object:
						#adjust offset and size
						if 1: #offset
							if not self.offset: # beginning of file
								if self.skip_header: #skip first row
									print self.skip_header
									file_object.seek(self.offset)
									pos = file_object.read(self.peek).find(os.linesep)
									assert pos>-1, 'skip_header: Increase peek size to move offset to EOL.'
									print '[%d][%d]\SKIP_HEADER: %s -> %s, \tSIZE: %s -> %s' % (self.pid, self.offset, self.offset, self.offset+pos, self.size, self.size-pos)
									self.offset=self.offset+pos+len(os.linesep)
									self.size=self.size-pos
									#e()
							else:
								file_object.seek(self.offset)
								pos = file_object.read(self.peek).find(os.linesep)
								assert pos>-1, 'Increase peek size to move offset to EOL.'
								print '[%d][%d]\tOFFSET: %s -> %s, \tSIZE: %s -> %s' % (self.pid, self.offset, self.offset, self.offset+pos, self.size, self.size-pos)

								self.offset=self.offset+pos+len(os.linesep)
								self.size=self.size-pos
						if 1: #size
							file_object.seek(self.offset+self.size)
							contents=file_object.read(self.peek)
							if not contents: #EOF
								pass
							else:
								pos = contents.find(os.linesep)
								assert pos>-1, 'Increase peek size to move offset to EOL.'
								print '[%d][%d]\tsize: %s -> %s' % (self.pid,self.offset, self.size, self.size+pos)
								self.size=self.size+pos

						file_object.seek(self.offset)
						self.content = file_object.read(self.size)
				else:
					raise Exception('Wrong offset [%s] and size [%s]' % (self.offset, self.size))
			elif self.path:
				with open(self.path) as file_object:
					self.content = file_object.read()
			else:
				assert False
		return self.content
		


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

