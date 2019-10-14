import boto3
from boto3.s3.transfer import TransferConfig
		
tc= TransferConfig(multipart_threshold=8388608, max_concurrency=10, multipart_chunksize=8388608, num_download_attempts=5, max_io_queue=100, io_chunksize=262144, use_threads=True)
if 1:
	# Create an S3 client
	s3 = boto3.client('s3')

	filename = 'test.csv.gz'
	bucket_name = 'home-pmt-accounting-dev'

	# Uploads the given file using a managed uploader, which will split up large
	# files automatically and upload parts in parallel.
	s3.upload_file(filename, bucket_name, filename, Config=tc)
	
if 0:

	s3 = boto3.resource(
		's3',
		region_name='us-east-1',
		aws_access_key_id=KEY_ID,
		aws_secret_access_key=ACCESS_KEY
	)
	content="String content to write to a new S3 file"
	s3.Object('my-bucket-name', 'newfile.txt').put(Body=content)
	