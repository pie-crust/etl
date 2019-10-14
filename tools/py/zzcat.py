#!~/python27/bin/python

#s3://home-pmt-accounting-dev/racct/DY_Position_SD/file_0_100.2019-06-17.13_39_12.IQ.csv.gz test.csv.gz


from boto.s3.connection import S3Connection
import gzip
import csv
import io


class ReadOnce(object):
	def __init__(self, k):
		self.key = k
		self.has_read_once = False

	def read(self, size=0):
		if self.has_read_once:
			return b''
		data = self.key.read(size)
		if not data:
			self.has_read_once = True
		return data

class ReadFromS3:
	def __init__(self, options):
		conn = S3Connection()
		self.bucket = conn.get_bucket(options['s3']['bucket'], validate=False)

	def stream_file(self, file):
		key = self.bucket.get_key(file)
		gz_file = gzip.GzipFile(fileobj=key, mode='r')
		#print gz_file.read(100)
		reader = csv.DictReader(io.TextIOWrapper(
			gz_file, newline="", encoding="utf-8-sig"), delimiter='\t')
		#for line in reader:
		#	print(line)

def main(options):
	tsr = ReadFromS3(options)
	tsr.stream_file('racct/DY_Position_SD/file_0_100.2019-06-17.13_39_12.IQ.csv.gz test.csv.gz')


if __name__ == "__main__":
	options = {
		's3':{
			'user': 's_dev_racct',
			#'key': ,
			'bucket':'home-pmt-accounting-dev',
		}
	}
	main(options)

