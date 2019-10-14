
(cli, conn_pool)=app_init
import os, sys, csv, time, math, glob
import pyodbc
import multiprocessing
import collections
from collections import OrderedDict
from pprint import pprint as pp
e=sys.exit
import logging
log=logging.getLogger('cli')

import requests, json
try:
	import __builtin__ as builtins
except:
	import builtins

#from include.extractor.common.DataStreamer import DataStreamer
from include.extractor.common.Extractor import Extractor

from include.utils import  ctimeit, api

try:
	from itertools import chain, imap, islice
except:
	from itertools import chain,  islice
	imap=map



try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk as new_walk

#from pubsub import pub


class Opt(object):
	def __init__(self, cli):
		assert cli.dop
		self.processes	= cli.dop
		self.walk		= 'filesystem'
		self.prefix		= 'racct'
		self.put		= 'update'
		self.gzip		= True
		self.secure		= True
		self.host		= 's3.amazonaws.com'
		self.bucket		= 'home-pmt-accounting-dev'
		self.headers	= None
		self.content_type = None
		self.dry_run	= False
		self.grant		= None
		self.encrypt_key= False
		self.quiet		= False
		self.verbose	= True
		self.lame_duck	= 0
		self.peek		= 5000
		self.chunk_size = 4*10*10<<20

		
options=Opt(cli)



class Dir(Extractor):
	def __init__(self, **kwargs):
		Extractor.__init__(self)
		global actors
		self.cli =cli= kwargs.get('cli', None)
		assert cli
		self.cpool =cpool= kwargs.get('conn_pool', None)
		self.cln=cln= self.__class__.__name__
		self.uploaded={}
		#pub.subscribe(self.onTopic11, 'cli.ParallelS3')
	def onTopic11(self, msg, extra=None):
		print('Method Listener.onTopic11 received: ', repr(msg), repr(extra))
		self.uploaded[1]=extra
	def __call__(self, **kwargs):
		print('Listener instance received: ', kwargs)
		
	def walk_filesystem(self, source, options):
		chunk_size=options.chunk_size
		
		if os.path.isdir(source):
			for dirpath, dirnames, filenames in new_walk(source):
				
				for filename in filenames:
					
					abs_path = os.path.join(dirpath, filename)
					rel_path = os.path.relpath(abs_path, source)
					basename=os.path.basename(rel_path)
					key_name = '/'.join([options.prefix]+[x for x in os.path.relpath(dirpath).split(os.sep) if x not in ['..']] + [basename])
					if 1:
						fsize=float(os.stat(abs_path).st_size)
						if fsize>chunk_size:
							for x in range(int(math.ceil(fsize/chunk_size))):
								new_key_name='%s.%s' % (key_name,x) 
								#print 444, new_key_name
								yield (new_key_name, dict(filename=abs_path, offset=x*chunk_size, size=chunk_size))
						else:	
							#print 222, key_name
							yield (key_name, dict(path=abs_path))
		
		elif os.path.isfile(source):

			key_name = os.path.normpath(os.path.join(options.prefix, source))
			fsize=float(os.stat(source).st_size)
			if fsize>chunk_size:
				for x in range(int(math.ceil(fsize/chunk_size))):
					new_key_name='%s.%s' % (key_name,x)
					yield (new_key_name, dict(filename=source, offset=x*chunk_size, size=chunk_size))
			else:
				#print 333, key_name
				yield (key_name, dict(path=source))
		else:
			raise Exception('Given path is not a dir or file [%s]' % source)
	def walk_files(self, source, options):
		chunk_size=options.chunk_size
		
		
		if os.path.isdir(source):
			
			for dirpath, dirnames, filenames in new_walk(source):
				
				for filename in filenames:
					
					abs_path = os.path.join(dirpath, filename)
					rel_path = os.path.relpath(abs_path, source)
					basename=os.path.basename(rel_path)
					
					if 1:
						yield abs_path
		
		elif os.path.isfile(source):

			
			yield source
		else:
			raise Exception('Given path is not a dir or file [%s]' % source)
			
	def walker(self,walk, out, sources, options):
		log = logging.getLogger(os.path.basename(sys.argv[0]))
		pairs = chain(*imap(lambda source: walk(source, options), sources))

		for pair in pairs:
			out.file_names.append(pair)

	@api
	@ctimeit
	def get_files(self, path, out, skip_header=0, chunk_size=4*10*10<<20):
		global options
		path=path
		#pp(self.cli.tab_root)
		#options.skip_header=options
		options.chunk_size=chunk_size
		self.walker(walk=self.walk_filesystem, out=out, sources=[path], options=options)

	@api
	@ctimeit
	def glob_dir(self, path, out,  ext='*.*'):
		assert os.path.isdir(path), path
		fltr="%s/%s" % (path.strip().rstrip('/'), ext)
		for filename in glob.glob(fltr):
			abs_path = os.path.join(path, os.path.splitext(filename)[0])
			out.file_names.append(filename)


