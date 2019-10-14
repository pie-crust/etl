import boto3

some_binary_data = b'Here we have some data'
more_binary_data = b'Here we have some more data'
transfer_file='dump/CIGActgH/spTimeSeriesPL_WRAPPER/1k.csv'
if 0:
	# Method 1: Object.put()
	s3 = boto3.resource('s3')
	object = s3.Object('home-pmt-datamart-dev', transfer_file)
	object.put(Body=some_binary_data)

file_handle = open(transfer_file, 'rb')
# Method 2: Client.put_object()
client = boto3.client('s3')
client.put_object(Body=file_handle.read(), Bucket='home-pmt-datamart-dev', Key='racct/1k.csv')

