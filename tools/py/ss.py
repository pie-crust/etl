import os, sys, io, csv, time, boto, gzip, math
import pyodbc
e=sys.exit
from pprint import pprint as pp


try:
	from io import  BytesIO as cStringIO
except:
	try:
		import cStringIO
	except ImportError:
		import io as cStringIO	
	
	
	
	
def setKeytabCache(keyTabFile, keyTabPrincipal='',isVertica=True):
	
	
	DEFAULT_DOMAIN = dbenvars.get('DEFAULT_DOMAIN'); assert DEFAULT_DOMAIN
	if isVertica:
		if keyTabFile != '':
			verticakeyTabPrincipal = dbenvars.get('DB_SERVER') + '@' + DEFAULT_DOMAIN
			os.system("kinit -k -t {} {}".format(keyTabFile, verticakeyTabPrincipal))
		else:
			message="keyTabFile {} not defined. Check environ variable KRB5_CLIENT_KTNAME".format(keyTabFile)
			print 'ERROR', message
			raise Exception(message)
	else:
		 if keyTabFile != '' and keyTabPrincipal != '':
			os.system("kinit -k -t {} {}".format(keyTabFile, keyTabPrincipal))
		 else:
			message="keyTabFile {} or keyTabPrincipal not defined. Check environ variable KRB5_CLIENT_KTNAME".format(keyTabFile,keyTabPrincipal)
			print 'ERROR', message
			raise Exception(message)
			
encoding = 'utf-8'
write_file='_sqldata.csv'
stream =  io.BytesIO()
#line_as_list = [line.encode(encoding) for line in line_as_list]

	
			
dbenvars={ 'DB_SERVER':'MDDATAMART1\MDDATAMART1', 'DEFAULT_DOMAIN':"homeGROUP.COM"}

def insert_data(data):

	if 1:
		stmt="INSERT INTO ACCOUNTINGBI.POSITION.DY_FiccDistribution (TransactionId,SettleDate,TransactionTypeCode,ClearedDate,CloseDate,CloseLeg, QuantityType,Quantity,AccountingDate,AsOfDateTime) values (?,?,?,?,?,?,?,?,?,?)"
		#CAST(? AS DATE),CAST(? AS TIMESTAMP))
		#tcur.setinputsizes([(pyodbc.SQL_WVARCHAR, 0, 0)])
		tcur.fast_executemany = True
		tcur.executemany(stmt, data)
		e()
import datetime
def insert_data_2(data):

	if 1:
		stmt="INSERT INTO ACCOUNTINGBI.POSITION.DY_FiccDistribution (TransactionId,SettleDate,TransactionTypeCode,ClearedDate,CloseDate,CloseLeg, QuantityType,Quantity,AccountingDate,AsOfDateTime) values %s"
		#tcur.setinputsizes([(pyodbc.SQL_WVARCHAR, 0, 0)])
		#tcur.fast_executemany = True
		out=[]
		for row in data:
			tmp=[str(x) if isinstance(x, datetime.date) else x for x in list(row)]
			out.append('^'.join(["'1971-01-01'" if x==None else str(x) if isinstance(x, int) else "'%s'" % x for x in tmp]))
		if out:
			stmt="INSERT INTO ACCOUNTINGBI.POSITION.DY_FiccDistribution values (%s)" % '),\n('. join (out)
			#print(stmt)
			#e()
			tcur.execute(stmt)
			tcur.execute('commit')
			print tcur.rowcount

def get_cnt(cur,tab):
	cur.execute("SELECT count(1) from %s" % tab)
	return cur.fetchone()[0]

rid=0
file_rows=25000 #16384
s3_rows=10000
def s3_upload_rows( bucket, s3_key, data, suffix='.gz' ):

	rid=0
	
	assert data
	key = s3_key +suffix
	use_rr=False

	mpu = bucket.initiate_multipart_upload(key,reduced_redundancy=use_rr , metadata={'header':'test'})

	stream = cStringIO()
	
	compressor = gzip.GzipFile(fileobj=stream, mode='wb')

	uploaded=0
	
	#@timeit
	def uploadPart(partCount=[0]):
		global total_comp
		partCount[0] += 1
		stream.seek(0)
		mpu.upload_part_from_file(stream, partCount[0])
		total_comp +=stream.tell()
		
		stream.seek(0)
		stream.truncate()
	#@timeit
	def upload_to_s3():
		global total_size,total_comp, rid
		i=0
		
		while True:  # until EOF
			i+=1
			start_time = time.time()
			chunk=''
			#pp(data[0])
			tmp=[]
			if rid<len(data):
				tmp= data[rid:][:s3_rows]
				chunk=os.linesep.join(tmp)+os.linesep
			
			#print rid, len(chunk), len(data)
			rid +=len(tmp)
			if not chunk:  # EOF?
				compressor.close()
				uploadPart()
				mpu.complete_upload()
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
	
	return key
def convertSize( size):
	if (size == 0):
		return '0B'
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size,1024)))
	p = math.pow(1024,i)
	s = round(size/p,2)
	return '%s %s' % (s,size_name[i])

tbl='DY_FICCDISTRIBUTION'
stg='POSITION_MODEL_STAGE_TEST_2'
sch='ACCOUNTINGBI.POSITION'
wrh='LOAD_WH'
def bulk_copy(cur,  file_names):
	global tbl, stg, sch, LOAD_WH


	assert tbl and  stg and sch and wrh
	
	assert len(file_names)
	files="','".join(file_names)
	before=get_cnt(cur,tbl)
	start_time=time.time()

	if 1:
		
		cmd="""
COPY INTO 
%s 
FROM '@%s/%s/'
FILES=('%s')

		""" % (tbl,stg, 'DEMO', files)	

		

		if 1:
			cur.execute("USE WAREHOUSE %s" % wrh)
			cur.execute("USE SCHEMA %s" % sch)
			try:
				out=cur.execute(cmd) 
			except:
				print(cmd)
				raise
			pp(out)

			match=0
			for id, row in enumerate(cur.fetchall()):
				status, cnt = row[1:3]
				print('%s: Insert #%d, status: [%s], row count: [%s]' % ('DEMO', id, status, cnt))
				if status not in ['LOADED']:
					match +=1
			if match:
				raise Exception('Unexpected load status')
			cur.execute("commit")
			after=get_cnt(cur,tbl)
			print 'Rows inserted: ', after-before
			sec=round((time.time() - start_time),2)

				
if __name__=="__main__":
					
	if 1:
		pyodbc.pooling = False


	if 0:
		
		keyTabFile=os.getenv('SSRSREPORTINGKEYTABFILE'); assert keyTabFile
		keyTabPrincipal=os.getenv('DATASTAGINGSQLUSER'); assert keyTabPrincipal
		#setKeytabCache(KEYTABFILE, os.getenv('DATASTAGINGSQLUSER'), None)
		print ("kinit -k -t {} {}".format(keyTabFile, keyTabPrincipal))
		#e()
		os.system("kinit -k -t {} {}".format(keyTabFile, keyTabPrincipal))
	connS='DSN=MDIR01;Database=DataStaging;Trusted_Connection=yes;POOL=0;App=FiccApi'
	connS='DSN=MDDATAMART1;Database=Accounting;Trusted_Connection=yes;POOL=0;App=PositionReader'
	sconn = pyodbc.connect(connS)	
	scur = sconn.cursor()
	scur.arraysize=file_rows
	#scur.setinputsizes([(pyodbc.SQL_WVARCHAR, 0, 0)])
	if 1:
		
		stmt="SELECT COUNT(*) from DY_FiccDistribution"

		scur.execute(stmt)


