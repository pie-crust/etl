#!~/python27/bin/python

#s3://home-pmt-accounting-dev/racct/DY_Position_SD/file_0_100.2019-06-17.13_39_12.IQ.csv.gz test.csv.gz

import os, sys
from boto.s3.connection import S3Connection
import gzip
import csv
import io

fh=open('test.csv.gz', 'rb')
import zlib

def stream_gzip_decompress(stream):
	dec = zlib.decompressobj(32 + zlib.MAX_WBITS)  # offset 32 to skip the header
	for chunk in stream:
		rv = dec.decompress(chunk)
		if rv:
			yield rv
			
			
if 0:
	for data in stream_gzip_decompress(fh):
		
		for line in data.split(os.linesep):
			print(', '.join(line.split('^')))

		
		
import gzip, zipfile
import csv
import io
import boto
from pprint import pprint
from gzip import GzipFile
from boto.s3.key import Key
s3 = boto.connect_s3()
bname='home-pmt-accounting-dev'
bucket = s3.get_bucket(bname, validate=False)
k = Key(bucket)
kname='racct/DY_DeskPLRSRange03/file_0.IQ.Jkmk22.20190618_175726.csv.gz'
k.key = kname
k.open()
print(dir(csv))
from include.fmt import get_formatted
if 1:
	gzipped = GzipFile(None, 'rb', fileobj=k)
	reader = io.TextIOWrapper(gzipped, newline="", encoding="utf-8")
	data=[]
	for id,line in enumerate(reader):
		data.append(line)
		pprint(line)
		if id>10: break
		
	ptitle= kname
	#headers=['Col#%d' % i for i in range(len(data[0]))]
	#print (get_formatted(ptitle,data,headers,join = True))
	
if 0:
	gzipped = GzipFile(None, 'rb', fileobj=k)
	reader = csv.reader(io.TextIOWrapper(gzipped, newline="", encoding="utf-8"), delimiter='^')
	data=[]
	for id,line in enumerate(reader):
		data.append(line)
		pprint(line)
		if id>10: break
		
	ptitle= kname
	#headers=['Col#%d' % i for i in range(len(data[0]))]
	#print (get_formatted(ptitle,data,headers,join = True))

	
	
if 0:
	buffer = io.BytesIO(k.read())
	print (buffer)
	z = zipfile.ZipFile(buffer)
	foo2 = z.open(z.infolist()[0])
	print(sys.getsizeof(foo2))
	line_counter = 0
	for _ in foo2:
		line_counter += 1
	print (line_counter)
	z.close()
	
	
if 0:
	#print k.read(10)
	gz_file = gzip.GzipFile(fileobj=k, mode='rb')
	reader = csv.ListReader(io.TextIOWrapper(gz_file, newline="", encoding="utf-8-sig"), delimiter='\t')
	for line in reader:
		print(line)