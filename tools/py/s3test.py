import os
try:
	import boto
	from boto.s3.key import Key
except ImportError:
	raise ImproperlyConfigured("Could not load Boto's S3 bindings")
if 1:
	AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
	AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') 
	assert AWS_SECRET_ACCESS_KEY, 'AWS_SECRET_ACCESS_KEY is not set'
	assert AWS_ACCESS_KEY_ID, 'AWS_ACCESS_KEY_ID is not set'
	print(AWS_ACCESS_KEY_ID)
	print(AWS_SECRET_ACCESS_KEY)
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bucket_name='home-pmt-datamart-dev'
bucket = conn.get_bucket(bucket_name, validate=False)

