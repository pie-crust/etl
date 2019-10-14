import os
import boto3

s3_resource = boto3.resource("s3", region_name="us-east-1")

def upload_objects():
	try:
		bucket_name = "home-pmt-datamart-dev" #s3 bucket name
		root_path = '/home/s_dev_racct/ssrs-reporting-services/dump/CIGActgH/' # local folder for upload

		my_bucket = s3_resource.Bucket(bucket_name)
		print(list(os.walk(root_path)))
		for path, subdirs, files in os.walk(root_path):
			path = path.replace("\\","/")
			directory_name = path.replace(root_path,"")
			for file in files:
				print (file)
				my_bucket.upload_file(os.path.join(path, file), 'testdir'+'/'+file)

	except Exception as err:
		raise
		print(err)

if __name__ == '__main__':
	upload_objects()