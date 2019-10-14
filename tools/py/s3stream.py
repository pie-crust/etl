import os, sys, time, math
import boto
import gzip
import __builtin__
import imp
e=sys.exit
from optparse import OptionParser
from boto.s3.connection import Location
from boto.exception import S3ResponseError, S3CreateError, BotoClientError
try:
    import cStringIO
except ImportError:
    import io as cStringIO
	
	
total_size=0

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') 
assert AWS_SECRET_ACCESS_KEY, 'AWS_SECRET_ACCESS_KEY is not set'
assert AWS_ACCESS_KEY_ID, 'AWS_ACCESS_KEY_ID is not set'
def sendStreamGz(bucket, s3_key, pipe, suffix='.gz'):
	key = s3_key +suffix
	use_rr=False
	if opt.s3_use_rr:
		use_rr=True
	mpu = bucket.initiate_multipart_upload(key,reduced_redundancy=use_rr, metadata={'my_key':'test'})
	stream = cStringIO.StringIO()
	compressor = gzip.GzipFile(fileobj=stream, mode='w')
	
	def uploadPart(partCount=[0]):
		global total_size
		partCount[0] += 1
		stream.seek(0)
		mpu.upload_part_from_file(stream, partCount[0])
		print('Size: Uncompressed: %s' % convertSize(total_size))
		print('Size: Compressed  : %s' % convertSize(stream.tell()))
		stream.seek(0)
		stream.truncate()
	def upload_to_s3(dump_file=None):
		global total_size
		i=0
		
		while True:  # until EOF
			i+=1
			start_time = time.time()
			#chunk = inputFile.read(8192)
			chunk=pipe.read(opt.s3_write_chunk_size)
			#print chunk
			#print(i)
			if not chunk:  # EOF?
				compressor.close()
				uploadPart()
				mpu.complete_upload()
				
				break
			compressor.write(chunk)
			total_size +=len(chunk)
			
			#print(compressor.tell())
			if dump_file:
				dump_file.write(chunk)
			#print(len(chunk),opt.s3_write_chunk_size)
			if stream.tell() > 10<<20:  # min size for multipart upload is 5242880
				
				uploadPart()
			print ('%d chunk %s [%s sec]' % (i, convertSize(len(chunk)),round((time.time() - start_time),2)))
	#with file(fileName) as inputFile:

	if opt.create_data_dump:
		q_file =os.path.splitext(os.path.basename(opt.pgres_query_file))[0]
		dump_dir=os.path.join('data_dump',q_file,opt.s3_bucket_name)	
		
		tss=datetime.now().strftime('%Y%m%d_%H%M%S')
		
		if not os.path.isdir(dump_dir):
			os.makedirs(dump_dir)
		dump_fn= os.path.join(dump_dir,'%s.%s.gz' % (  s3_key,tss) )
		#with open(dump_fn, 'w') as f:
		print ('Dumping data to: %s' % os.path.abspath(dump_fn) )
		with gzip.GzipFile(dump_fn, mode='w') as c:
			upload_to_s3(c)
	else:
		upload_to_s3(None)
	
	return key


def convertSize(size):
	if (size == 0):
		return '0B'
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size,1024)))
	p = math.pow(1024,i)
	s = round(size/p,2)
	return '%s %s' % (s,size_name[i])
	
def import_module(filepath):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)
	return py_mod	
if __name__ == "__main__":		
	parser = OptionParser()
	parser.add_option("-q", "--pgres_query_file", 	dest="pgres_query_file", type=str)
	parser.add_option("-d", "--pgres_col_delim",	dest="pgres_col_delim", type=str, default=',')
	parser.add_option("-a", "--pgres_quote", 	dest="pgres_quote", default='"')	
	parser.add_option("-j", "--pgres_user", 	dest="pgres_user", default='postgres')	
	parser.add_option("-f", "--pgres_db_name", 	dest="pgres_db_name", default='postgres')	
	parser.add_option("-n", "--pgres_db_server", 	dest="pgres_db_server", default='127.0.0.1')	

	#parser.add_option("-e", "--pgres_add_header", dest="ora_add_header",  action="store_true", default=False)
	parser.add_option("-l", "--pgres_lame_duck", dest="pgres_lame_duck", type=int, default=0)
	
	parser.add_option("-s", "--create_data_dump", dest="create_data_dump",  action="store_true", default=False)
	
	parser.add_option("-b", "--s3_bucket_name", dest="s3_bucket_name", type=str)
	parser.add_option("-t", "--s3_location", dest="s3_location", type=str, default='us-west-2')
	
	parser.add_option("-k", "--s3_key_name", dest="s3_key_name", type=str)
	parser.add_option("-w", "--s3_write_chunk_size", dest="s3_write_chunk_size", type=int, default=10<<20)
	
	parser.add_option("-r", "--s3_use_rr", dest="s3_use_rr",  action="store_true", default=False)
	parser.add_option("-p", "--s3_public", dest="s3_public",  action="store_true", default=False)
	parser.add_option("-o", "--red_to_table", dest="red_to_table")
	parser.add_option("-c", "--red_col_delim", dest="red_col_delim", type=str, default=',')
	parser.add_option("-u", "--red_quote", dest="red_quote",type=str, default='"')
	parser.add_option("-m", "--red_timeformat", dest="red_timeformat", default='MM/DD/YYYY HH12:MI:SS')
	parser.add_option("-i", "--red_ignoreheader", dest="red_ignoreheader", type=int, default=0)	
	
	(opt, _) = parser.parse_args()
	opt.s3_bucket_name='home-pmt-datamart-dev'
	opt.s3_key_name='racct/Daily_FinancingPosition/15.csv'
	print (opt)
	if 0 and len(sys.argv) < 2:
		print (__doc__)
		sys.exit()
	kwargs = dict(use_rr=opt.s3_use_rr, make_public=opt.s3_public)

	start_time = time.time()
	if not opt.s3_key_name:
		opt.s3_key_name =  q_file[0]
	
	conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
	#print(123)
	#e(0)
	
	try:
		bucket = conn.get_bucket(opt.s3_bucket_name)
		print ('Uploading results of "%s" to existing bucket "%s"' % (''.join(q_file),opt.s3_bucket_name))
	except S3ResponseError as err:
		
		if str(err).strip().endswith('404 Not Found'):
			print('Creating new bucket "%s" in location "%s"' % (opt.s3_bucket_name,opt.s3_location))
			try:
				conn.create_bucket(opt.s3_bucket_name, location=opt.s3_location)
				print ('Uploading results of "%s" to new bucket "%s" in region "%s"' % (''.join(q_file),opt.s3_bucket_name,opt.s3_location))
			except S3CreateError:
				print('Warning: Bucket "%s" already exists in "%s". Cannot proceed.' % (opt.s3_bucket_name,opt.s3_location))
				e(0)
		
			
	
	p=None
	if 	1:
		__builtin__.g = globals()
		abspath=os.path.abspath(os.path.dirname(sys.argv[0]))
		extractor_file = os.path.join(abspath,'include','extractor.py')		
		extractor=import_module(extractor_file)
		p=extractor.extract(os.environ)
	#e(0)
		
	bucket = conn.get_bucket(opt.s3_bucket_name, validate=False)
	sys.stdout.write('Started reading from PostgreSQL (%s sec).\n' % round((time.time() - start_time),2))

	pipe=p.stdout

	#transfer_file='dump/CIGActgH/spTimeSeriesPL_WRAPPER/1k.csv'
	if 0:
		# Method 1: Object.put()
		s3 = boto3.resource('s3')
		object = s3.Object('home-pmt-datamart-dev', pipe)
		object.put(Body=some_binary_data)

	#pipe = open(transfer_file, 'rb')

	s3key=sendStreamGz(bucket, opt.s3_key_name, pipe, suffix='.gz')

	

	
	
	#pp(dir(k))
	e(0)
	if opt.s3_public:
		k = Key(bucket)
		k.key = s3key
		k.set_metadata('my_key', 'value')
		k.make_public()

	sys.stdout.write('Elapsed: PostgreSQL+S3    :%s sec.\n' % round((time.time() - start_time),2))
	start_time2 = time.time()
	location='/'.join((opt.s3_bucket_name, '%s.gz' % opt.s3_key_name))
	file_type= 'PRIVATE'
	if opt.s3_public:
		file_type = 'PUBLIC'
		if 1: #options.make_public and location :
			_,region,aws,com =bucket.get_website_endpoint().split('.')		
			sys.stdout.write('Your %s upload is at: https://s3-%s.%s.%s/%s\n' % (file_type,opt.s3_location,aws,com,location))
	if location:
		import __builtin__
		__builtin__.g = globals()
		abspath=os.path.abspath(os.path.dirname(sys.argv[0]))
		loader_file = os.path.join(abspath,'include','loader.py')		
		loader=import_module(loader_file)
		loader.load(location)
		print ('Elapsed: S3->Redshift :%s sec.' % round((time.time() - start_time2),2))
	sys.stdout.write('--------------------------------\nTotal elapsed: %s sec.\n' % round((time.time() - start_time),2))	