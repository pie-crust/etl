(cli, conn_pool)=app_init
import os, sys, time, gzip, math, gzip
import boto
import tempfile
from boto.exception import S3ResponseError
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

from include.utils import timeit, ctimeit, csource, api, clierr


s3_rows=50000
rid=0


from include.loader.common.Loader import Loader



class S3StreamLoader(Loader):
	def __init__(self, **kwargs):
		self.cli =cli= kwargs.get('cli', None)
		#self._in =kwargs.get('_in', None)
		assert cli
		self.cpool =cpool= kwargs.get('conn_pool', None)
		self.cln=cln= self.__class__.__name__

		
		
		#self.write_chunk_size=10<<19
		self.write_row_cnt=self.cli.s3cfg['writeBufferSize']
		#pp(self.cli.s3cfg)
		#e()
		self.skip_header=0
		self.conn=self.bucket=None

	def connect(self):
		cli=self.cli
		if 1:
			tb=cli.s3cfg['targetBucket']
			if isinstance(tb, dict):
				assert 'env_var' in tb
				cli.s3cfg['targetBucket']=os.getenv(tb['env_var'])
				assert cli.s3cfg['targetBucket'], 'Set bucket name in "%s"' % tb['env_var']
					
		self.bname=cli.s3cfg['targetBucket']		
		self.conn, self.bucket = self.s3_init(conn_key='%s.%s' % (self.cln,self.bname))
		
	@ctimeit
	def s3_init(self, conn_key):
		if 0:
			if conn_key in self.cpool.keys():
				log.debug('%s: Reusing connect/bucket.' % self.cln)
				return self.cpool[conn_key]

		if 1:
			log.debug('%s: New connect/bucket.' % self.cln)
			keys=self.get_creds()
			#print keys 
			#e()
			conn = boto.connect_s3(*keys)
			
			bucket = conn.get_bucket(self.bname, validate=False)
			self.cpool[conn_key] = (conn, bucket)
			return conn, bucket
	@api
	@ctimeit
	def load_stream(self, source,skip_header, out):
		global total_size, total_comp
		cli=self.cli
		if not self.conn or not self.bucket:
			self.connect()
		
		pipe=source.pipe
		col_map=source.col_map
		#assert col_map
		skip=str(self.skip_header).strip()
		if skip_header is not None:
			skip=str(skip_header).strip()
		assert str(skip).strip() in ['0','1'], 'skip_header [%s] should be "0" or "1"' % str(skip).strip()
		if str(skip) == '1':
			pipe.readline()
			log.debug('Skip header = %s' %  skip)
		#Out = collections.namedtuple('Out','file_filter file_names file_cnt actor col_map')
		
		filter='%s.%s' % (source.actor,cli.filter)
			
		tbl=cli.tcfg['targetTable']
		files=[]
		keys=[]
		
		assert tbl 
		
		timeFormat = "%Y-%m-%d %H:%M:%S"
		currentTimeStamp = time.strftime(timeFormat)
		fid=0
		start_time = time.time()
		total_all=0
		comp_all=0
		while True:
			pipe.file_id=fid
			fname='file_%d.%s.csv' % (fid,filter)
			
			to_dir=cli.s3cfg['targetDir']
			
			s3_key_name='%s/%s/%s' % (to_dir, cli.proc_key, fname)
			
			self.load_streamed_chunk(s3_key_name, pipe)
			
			log.info('s3://%s/%s.gz' %(self.bname, s3_key_name))
			if total_size:
				#log.debug('S3: %s' % s3_key_name)
				files.append('%s.gz' % fname)
				keys.append('%s.gz' % s3_key_name)
				pipe.reset()
				total_all +=total_size
				total_size=0
				comp_all +=total_comp
				total_comp=0
				fid +=1	
			if pipe.Done:
				break;
			if cli.lame_duck and pipe.rid>=cli.lame_duck:
				break

		sec=round((time.time() - start_time),2)
		if pipe.rid:
			log.info('S3: Loaded:{:,.0f}, Read:{:,.0f}, Files:{:,.0f}, Elapsed: {:,.0f} sec/{:,.0f} min'.format (pipe.rid - int(skip), pipe.rid, fid, sec, round(sec/60,2)))
			#log.info('S3: Read:{:,.0f} Loaded:{:,.0f}, Files:{:,.0f}, Elapsed: {:,.0f} sec/{:,.0f} min' % ( pipe.rid, pipe.rid - int(skip), fid, sec, round(sec/60,2)))
			log.info('S3: Total:%s, Compressed (gz):%s \n' %( self.convertSize(total_all), self.convertSize(comp_all)))
		pipe.close()
		#e()
		if not pipe.rid:
			log.debug(pipe.stmt)			
			raise Exception(clierr.E_EMPTY_SOURCE_PIPE[0])
		
		out.file_filter, out.file_names, out.file_keys, out.file_cnt, out.actor, out.col_map = filter, files, keys, fid, self.cln, col_map
		
		return out

	@timeit
	def load_streamed_chunk(self, s3_key, pipe, suffix='.gz' ):
		#conn, bucket = s3conf
		cli=self.cli
		bucket=self.bucket
		assert pipe
		key = s3_key +suffix
		use_rr=False
		
		mpu = bucket.initiate_multipart_upload(key,reduced_redundancy=use_rr , metadata={'header':'test'})
		
		stream = cStringIO()
		
		compressor = gzip.GzipFile(fileobj=stream, mode='wb')

		uploaded=0
		@timeit
		def uploadPart(partCount=[0]):
			global total_comp
			partCount[0] += 1
			stream.seek(0)
			mpu.upload_part_from_file(stream, partCount[0])
			total_comp +=stream.tell()
			
			stream.seek(0)
			stream.truncate()
		@timeit
		def upload_to_s3(dump_file=None):
			global total_size,total_comp
			i=0
			
			while True:  # until EOF
				#print(stream.tell() )
				i+=1
				start_time = time.time()
				chunk=pipe.read(self.write_row_cnt)

				if not chunk:  # EOF?
					compressor.close()
					uploadPart()
					mpu.complete_upload()
					#break
					if 1:
						if pipe.cnt in [0]: #cleanup/ delete empty file
							bucket.delete_key(key)
						else:
							log.debug ('%d: %s/%s [%s sec]' %(pipe.file_id, self.convertSize(total_size), self.convertSize(total_comp), round((time.time() - start_time),2)))
							
						break
				if sys.version_info[0] <3 and isinstance(chunk, unicode):
					compressor.write(chunk.encode('utf-8'))
				else:
					compressor.write(chunk)
				total_size +=len(chunk)
				if dump_file:
					#pp(chunk)
					dump_file.write(chunk)
				if stream.tell() > 10<<20:  # min size for multipart upload is 5242880
					
					uploadPart()
				#log.info ('S3: Uploaded: File_%d: Chunk_%d: %s [%s sec]' % (pipe.file_id,i, self.convertSize(len(chunk)),round((time.time() - start_time),2)))
				#print('S3 key: %s' % key)
		if 0 and cli.dump:
			
			dn=os.path.dirname(s3_key)
			bn=os.path.basename(s3_key)
			dump_dir=os.path.join('dump',dn)	

			if not os.path.isdir(dump_dir):
				os.makedirs(dump_dir)
			dump_fn= os.path.join(dump_dir,'%s.gz' % (  bn) )
			
			log.debug('Dump: %s' % os.path.abspath(dump_fn) )
			with gzip.GzipFile(dump_fn, mode='w') as c:
				upload_to_s3(c)
		else:
			upload_to_s3(None)
		
		return key
		
	@ctimeit
	def get_meta(self):
		opt.s3_bucket_name='home-pmt-accounting-dev'
		opt.s3_key_name='racct/Daily_FinancingPosition/20k.csv'
		import boto
		conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
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
	def s3_delete_files(self, bucket, prefix):
		"""Bulk S3 file delete"""
		
		s3 = boto.connect_s3()
		bucket = s3.get_bucket(bucket, validate=False)
		to_delete = list(bucket.list(prefix=prefix))	
		log.info('S3: deleting [%d] files.' % len(to_delete))
		result = bucket.delete_keys(to_delete)

		if result.errors:		
			log.error('#'*80)
			log.error('S3 ERROR: The following errors occurred')
			for error in result.errors:
				log.error(error)
			log.error('#'*80)
			
		log.info('S3: deleted [%d] files.' % len(to_delete))
		return result
	@api
	@ctimeit
	def delete_files(self, file_names):
		"""Bulk S3 file delete"""

		result = self.bucket.delete_keys(file_names.file_keys)
		for v in result.deleted:
			log.debug(v)
		assert len(result.deleted) == len(file_names.file_keys)
		if result.errors:		
			log.error('#'*80)
			log.error('S3 ERROR: The following errors occurred')
			for error in result.errors:
				log.error(error)
			log.error('#'*80)
			
		log.debug('S3: deleted [%d] files.' % len(file_names.file_keys))
		return result
	@api
	@ctimeit
	def delete_file(self, file_name):
		"""Bulk S3 file delete"""
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
	def upload_file(self, fname, target):
		import boto3

		
		

		# Create an S3 client
		s3 = boto3.client('s3')

		# Uploads the given file using a managed uploader, which will split up large
		# files automatically and upload parts in parallel.
		s3.upload_file(fname, self.bname, fname)

	@api
	@ctimeit
	def upload_data(self,data, target, out):
		global rid
		print (444,data)
		fname='file_%d_%d.%s.%s.csv' % (data.chunk_id, len(data.data), data.current_ts, data.actor)
		s3_key='%s/%s/%s' % (target['targetDir'], self.cli.tcfg['targetTable'], fname)

		rid=0
		if not hasattr(out,'file_names'):
			out.file_names=[]
			out.keys=[]
		print (444,data)
		assert data
		suffix='.gz'
		key = s3_key + suffix
		use_rr=False

		mpu = self.bucket.initiate_multipart_upload(key,reduced_redundancy=use_rr , metadata={'header':'test'})

		stream = cStringIO()
		
		compressor = gzip.GzipFile(fileobj=stream, mode='wb')

		uploaded=0
		
		@timeit
		def uploadPart(partCount=[0]):
			global total_comp
			partCount[0] += 1
			stream.seek(0)
			mpu.upload_part_from_file(stream, partCount[0])
			total_comp +=stream.tell()
			
			stream.seek(0)
			stream.truncate()
		@timeit
		def upload_to_s3():
			global total_size,total_comp, rid
			i=0
			
			while True:  # until EOF
				i+=1
				start_time = time.time()
				chunk=''
				#pp(data[0])
				tmp=[]
				
				if rid<len(data.data):
					tmp= data.data[rid:][:s3_rows]
					
					chunk=os.linesep.join(tmp)+os.linesep
				
				#print rid, len(chunk), len(data)
				rid +=len(tmp)
				if not chunk:  # EOF?
					compressor.close()
					uploadPart()
					mpu.complete_upload()
					log.info( 'Uploaded: s3://%s/%s' % (self.bname, key))
					#e()
					break
				else:
					if sys.version_info[0] <3 and isinstance(chunk, unicode):
						compressor.write(chunk.encode('utf-8'))
					else:
						compressor.write(chunk)
					total_size +=len(chunk)
					if stream.tell() > 10<<20:  # min size for multipart upload is 5242880
						
						uploadPart()

		upload_to_s3()
		out.file_names.append(fname+suffix)
		out.keys.append(key)
		return out