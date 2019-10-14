(cli, conn_pool)=app_init
import os, sys, time, gzip, math, gzip
import boto
import tempfile
import collections
from datetime import datetime
from pprint import pprint as pp

e=sys.exit
try:
	from io import  BytesIO as cStringIO
except:
	try:
		import cStringIO
	except ImportError:
		import io as cStringIO	
	

	
total_size=0
total_comp=0
total_rows=0

from include.utils import timeit, ctimeit, csource, api


s3_rows=50000
rid=0
from include.Db import Loader
class S3(Loader):
	@ctimeit
	#@csource
	def __init__(self, **kwargs):
		self.cli =cli= kwargs.get('cli', None)
		#self._in =kwargs.get('_in', None)
		assert cli
		self.cpool =cpool= kwargs.get('conn_pool', None)
		self.cln=cln= self.__class__.__name__
		self.bname=cli.s3cfg['targetBucket']		
		self.conn=self.bucket=None
		if 0:
			self.conn, self.bucket = self.s3_init(conn_key='%s.%s' % (cln,self.bname))
			#self.write_chunk_size=10<<19
			self.write_row_cnt=self.cli.s3cfg['writeBufferSize']
			#pp(self.cli.s3cfg)
			#e()
		self.skip_header=0
	
	def connect(self):
		self.conn, self.bucket = self.s3_init(conn_key='%s.%s' % (self.cln,self.bname))
		
	@ctimeit
	def s3_init(self, conn_key):
		
		if conn_key in self.cpool.keys():
			log.debug('%s: Reusing connect/bucket.' % self.cln)
			return self.cpool[conn_key]
		else:
			log.debug('%s: New connect/bucket.' % self.cln)

			conn = boto.connect_s3(*self.get_creds())
			bucket = conn.get_bucket(self.bname, validate=False)
			self.cpool[conn_key] = (conn, bucket)
			return conn, bucket

		
	@ctimeit
	def get_meta(self):
		opt.s3_bucket_name='home-pmt-accounting-dev'
		opt.s3_key_name='racct/Daily_FinancingPosition/20k.csv'
		import boto
		conn = boto.connect_s3(self.get_creds())
		bucket = conn.get_bucket(opt.s3_bucket_name, validate=False)
		key = bucket.get_key('racct/Daily_FinancingPosition/15.csv.gz')

	def convertSize(self, size):
		if (size == 0):
			return '0B'
		size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
		i = int(math.floor(math.log(size,1024)))
		p = math.pow(1024,i)
		s = round(size/p,2)
		return '%s %s' % (s,size_name[i])

	@api
	@ctimeit
	def delete_files(self, file_names):
		"""Bulk S3 file delete"""
		if not self.bucket:
			self.connect()
		#pp(file_names.file_keys)
		#e()
		result = self.bucket.delete_keys(file_names.file_keys)
		for v in result.deleted:
			print log.debug(v)
		assert len(result.deleted) == len(file_names.file_keys)
		if result.errors:		
			log.error('#'*80)
			log.error('S3 ERROR: The following errors occurred')
			for error in result.errors:
				log.error(error)
			log.error('#'*80)
			
		log.info('S3: deleted [%d] files.' % len(file_names.file_keys))
		return result
	@api
	@ctimeit
	def delete_file(self, file_name):
		"""Bulk S3 file delete"""
		if not self.bucket:
			self.connect()		
		result = self.bucket.delete_keys([file_name])
		for v in result.deleted:
			print log.debug(v)
		assert len(result.deleted) == 1
		if result.errors:		
			log.error('#'*80)
			log.error('S3 ERROR: The following errors occurred')
			for error in result.errors:
				log.error(error)
			log.error('#'*80)
			
		log.info('S3: deleted 1 file.')
		return result

	@api
	@ctimeit
	def compress_file(self,from_fn, to_fn):
	
		content = open(from_fn, 'rb').read()
		f = gzip.open(to_fn, 'wb')
		f.write(content)
		f.close()

	@api
	@ctimeit
	def upload_file(self, fname):
		import boto3

		
		

		# Create an S3 client
		s3 = boto3.client('s3')

		# Uploads the given file using a managed uploader, which will split up large
		# files automatically and upload parts in parallel.
		to_dir=self.cli.s3cfg['targetDir']
		s3_key_name='%s/%s/%s' % (to_dir, cli.tcfg['targetTable'], fname)
		s3.upload_file(fname, self.bname, s3_key_name)
		#print s3_key_name
		return s3_key_name
