"""
Usage:  

  set AWS_ACCESS_KEY_ID=<you access key>
  set AWS_SECRET_ACCESS_KEY=<you secret key>
     "access_key_id": "AKIAYCS5P5BHTQCNLIXT",
    "secret_access_key": "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"


  s3_percent_uploader.exe <file_to_transfer> <bucket_name> [<s3_key_name>] [<use_rr>] [<public>]
	if <s3_key_name> is not specified, the filename will be used.
	--use_rr -- Use reduced redundancy storage.
	--public -- Make uploaded files public.

"""
import os, sys
from pprint import pprint
from optparse import OptionParser
class ImproperlyConfigured(Exception):
    """Base class for Boto exceptions in this module."""
    pass
	
try:
	import boto
	from boto.s3.key import Key
except ImportError:
	raise ImproperlyConfigured("Could not load Boto's S3 bindings")
e=sys.exit
bucket=None	
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') 
assert AWS_SECRET_ACCESS_KEY, 'AWS_SECRET_ACCESS_KEY is not set'
assert AWS_ACCESS_KEY_ID, 'AWS_ACCESS_KEY_ID is not set'
#e(0)
def progress(complete, total):
	sys.stdout.write('Uploaded %s bytes of %s (%s%%)\n' % (complete, total, int(100*complete/total)))

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)	
	
def main(transfer_file, bucket_name, s3_key_name=None, use_rr=False,
		 make_public=True):
	global bucket
	# open the wikipedia file
	if not s3_key_name:
		s3_key_name = os.path.basename(transfer_file)
	
	
	sys.stdout.write('Connecting to S3...\n')
	conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
	print (bucket_name)
	bucket = conn.get_bucket(bucket_name)
	e(0)
	#pprint(dir(bucket))
	#print 
	#e(0)
	file_handle = open(transfer_file, 'rb')

	k = Key(bucket)
	k.key = s3_key_name
	#pprint(dir(k))
	#e(0)
	#sys.stdout.write('Uploading to '+bucket.get_website_endpoint()+'...\n')
	sys.stdout.write('File size: %s\n' % sizeof_fmt(os.path.getsize(transfer_file)))
	sys.stdout.write('Public = %s\n' % str(make_public))
	sys.stdout.write('ReducedRedundancy = %s\n' % str(use_rr))
	
	
	k.set_contents_from_file(file_handle, cb=progress, num_cb=20, reduced_redundancy=use_rr )
	if make_public:
		k.make_public()

	sys.stdout.write('Upload complete.\n')

	return '/'.join((bucket_name, s3_key_name))
	

if __name__ == "__main__":
	fn=r'c:\tmp\data.zip'
	bn = 'pythonuploadtest1'
	parser = OptionParser()
	parser.add_option("-r", "--use_rr", dest="use_rr",
					  action="store_true", default=False)
	parser.add_option("-p", "--public", dest="make_public",
					  action="store_true", default=False)
	(options, args) = parser.parse_args()
	if len(args) < 2:
		print (__doc__)
		sys.exit()
	kwargs = dict(use_rr=options.use_rr, make_public=options.make_public)
	import time
	start_time = time.time()
	location=main(*args, **kwargs)
	#print (location)
	
	if options.make_public and location :
		_,region,aws,com =bucket.get_website_endpoint().split('.')		
		#print(region)
		sys.stdout.write('Your file is at: https://%s.%s.%s/%s\n' % (region.replace('-website-','-'),aws,com,location))
	print()
	print("Time elapsed: %s seconds" % (time.time() - start_time))
	
	
	
