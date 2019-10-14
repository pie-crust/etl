"""
((u'created_on', <type 'datetime.datetime'>, None, 23, 23, 3, True),
 (u'name', <type 'str'>, None, 16777216, 16777216, 0, True),
 (u'database_name', <type 'str'>, None, 16777216, 16777216, 0, True),
 (u'schema_name', <type 'str'>, None, 16777216, 16777216, 0, True),
 (u'kind', <type 'str'>, None, 16777216, 16777216, 0, True),
 (u'comment', <type 'str'>, None, 16777216, 16777216, 0, True),
 (u'cluster_by', <type 'str'>, None, 16777216, 16777216, 0, True),
 (u'rows', <class 'decimal.Decimal'>, None, 38, 38, 0, True),
 (u'bytes', <class 'decimal.Decimal'>, None, 38, 38, 0, True),
 (u'owner', <type 'str'>, None, 16777216, 16777216, 0, True),
 (u'retention_time', <type 'str'>, None, 16777216, 16777216, 0, True),
 (u'automatic_clustering', <type 'str'>, None, 16777216, 16777216, 0, True))
(datetime.datetime(2019, 5, 6, 13, 34, 9, 234000), u'DY_FINANCINGPOSITION', u'ACCOUNTINGBI', u'POSITION', u'TABLE', u'', u'LINEAR(ACCOUNTINGDATE, CLIENT)', Decimal('502552'), Decimal('61330432'), u'DB_OWNER', u'1', u'ON')

show table ACCOUNTINGBI.POSITION.ME_FINANCINGPOSITION
"""
from pprint import pprint as pp
import sys
e=sys.exit

cursor=None

def show():
	global cursor
	try:
		for row in cursor.fetchall():
			print(row)
	except e:
		print str(e)
		print 'nothing o show'
				
				
def show_one():
	global cursor
	row=cursor.fetchone()
	pp(row)
	if row:
		for id,column in enumerate(cursor.description):
			print '%s: %s (%s): [%s]' % (str(id+1).ljust(3), str(column[0]).ljust(25), str(column[1]).ljust(30),row[id])
	else:
		for id,column in enumerate(cursor.description):
			print '%s: %s (%s)' % (str(id+1).ljust(3), str(column[0]).ljust(25), str(column[1]).ljust(30))
			
if 1:
	import pyodbc
	conn = pyodbc.connect("DSN=SFDDATAMART;Database=ACCOUNTINGBI;WSID=ld-dbn-bofin006;APP=AnishTest;authenticator=https://home.okta.com;uid=s_dev_racct@homegroup.com;pwd=home312!;autocommit=False;ROLE=s_dev_racct_ROLE;")
	#cxn = pyodbc.connect("DSN=SFDDATAMART;Database=ACCOUNTINGBI;WSID=ld-dbn-bofin006;APP=AnishTest;authenticator=https://home.okta.com;uid=s_dev_racct@homegroup.com;pwd=home312!;autocommit=False;ROLE=s_dev_racct_ROLE;")
	
	#e()
	if 1:
		cursor = conn.cursor()
		try:
			#cursor.execute("desc table ACCOUNTINGBI.POSITION.ME_FINANCINGPOSITION")
			#cursor.execute("SELECT count(*) FROM  ACCOUNTINGBI.POSITION.ME_FINANCINGPOSITION")
			
			
			if 0:
				cursor.execute("USE SCHEMA ACCOUNTINGBI.POSITION")
				cursor.execute("""
create stage test_s3_stage url='s3://home-pmt-datamart-dev/racct/'
credentials=(aws_key_id='AKIAYCS5P5BHTQCNLIXT' aws_secret_key='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')
file_format = (type = 'CSV' field_delimiter = ',' skip_header = 1)
  """)		
  
  
			#'@%TEST_S3_STAGE/Daily_FinancingPosition/15.csv.gz';
			#cursor.execute("USE SCHEMA POSITION")
			#cursor.execute("CREATE TABLE test(id INT)")
			#cursor.execute("SHOW STAGES")
			#cursor.execute("SHOW TABLES like 'DY_FinancingPosition'")
			#DY_FINANCINGPOSITION
			#DY_FinancingPosition
			#cursor.execute("COPY INTO POSITION.DY_FINANCINGPOSITION FROM 's3://home-pmt-datamart-dev/racct/Daily_FinancingPosition/15.csv.gz'")
			cursor.execute("USE WAREHOUSE LOAD_WH")
			cursor.execute("USE ROLE AccountingBI_W")
			cursor.execute("USE DATABASE ACCOUNTINGBI")
			cursor.execute("USE SCHEMA POSITION")
			#cursor.execute("COPY INTO DY_FINANCINGPOSITION FROM '@TEST_S3_STAGE/Daily_FinancingPosition/15.csv.gz'")
			
			#cursor.execute("SELECT t.$1, t.$2 FROM '@TEST_S3_STAGE/Daily_FinancingPosition/15.csv.gz' t ")
			
			
			#cursor.execute("SELECT t.$1 from DY_FINANCINGPOSITION t limit 10")
			
			#cursor.execute("COPY INTO DY_FINANCINGPOSITION ( PARENTID) FROM (SELECT  (1) FROM '@TEST_S3_STAGE/Daily_FinancingPosition/15.csv.gz' t)")
			
			#cursor.execute("desc  TABLE INFORMATION_SCHEMA.columns")
			if 0:
				cursor.execute("SELECT count(*) from DY_FINANCINGPOSITION where POSITIONID =1"); show()
				
				cursor.execute("COPY INTO DY_FINANCINGPOSITION FROM '@position_model_stage/Daily_FinancingPosition/0.MOCK.va3bRP.20190522_095129.csv.gz'"); show()
				cursor.execute("commit"); 
				cursor.execute("SELECT count(*) from DY_FINANCINGPOSITION where POSITIONID =1"); show()
			#e(0)
			
			if 0:
				cursor.execute("SELECT count(*) from DY_FINANCINGPOSITION where POSITIONID =1"); show()
				cursor.execute("insert into DY_FINANCINGPOSITION (POSITIONID, ACCOUNTINGDATE, CLIENT, ASOFDATETIME, STAGE) values (1, to_date('2013-05-08T23:39:20.123'), 0.0, to_timestamp('2013-05-08T23:39:20.123'), 'test')")
				#cursor.execute("show columns in table DY_FINANCINGPOSITION")
				cursor.execute("commit")
				cursor.execute("SELECT count(*) from DY_FINANCINGPOSITION where POSITIONID =1"); show()
			#cursor.execute("USE SCHEMA ACCOUNTINGBI.INFORMATION_SCHEMA")
   			#cursor.execute("SELECT COLUMN_NAME, ORDINAL_POSITION FROM INFORMATION_SCHEMA.columns  WHERE table_schema = 'POSITION' AND table_name='DY_FINANCINGPOSITION' order by 2")
			#cursor.execute("SELECT t.POSITIONID FROM '@TEST_S3_STAGE/Daily_FinancingPosition/15.csv.gz' ")
			#cursor.execute("SELECT 1")
			"""
			
COPY INTO ME_13F FROM (SELECT $31,$1,$32,$2,$3,$4,$5,$6,$7,$8,$33,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23,$24,$25,$26,$27,$28,$29,$30 FROM '@position_model_stage/ME_13F/file0.IQStreamer.paGmuk.20190523_143328.csv.gz' t)
file_format = (type = CSV field_delimiter = ',' field_optionally_enclosed_by='"')
ON_ERROR = 'abort_statement'
validation_mode = 'RETURN_ERRORS'
9504134

			"""
			
			#pprint(one_row.cursor_description)
			#pprint(one_row)
			print 'Connected!'
			if 0:
				cursor.execute("TRUNCATE TABLE  ACCOUNTINGBI.POSITION.ME_13F"); show()
				cursor.execute("commit"); show()
				cursor.execute("SELECT count(1) from ME_13F"); show()
				
			if 0:
				cursor.execute("""
copy into @position_model_stage_test/test.csv.gz FROM (SELECT $31,$1,$32,$2,$3,$4,$5,$6,$7,$8,$33,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23,$24,$25,$26,$27,$28,$29,$30,$34,$35 FROM 
'@position_model_stage_test/ME_13F/file0.IQStreamer.PU7Wud.20190523_162621.csv.gz' )
"""); 
				for i,row in enumerate(cursor.fetchall()):
					print i, ','.join(row )
				#cursor.execute("commit")
				cursor.execute("select * from table(validate(t1, job_id => '_last'))")
				for row in cursor.fetchall():
					print row
				cursor.execute("SELECT count(*) from ME_13F"); show()
			if 0:
				if 0:
					cursor.execute("show columns in table ME_13F"); 
					for row in cursor.fetchall():
						print row[2], row[4], row[3]
					e()
				cursor.execute("SELECT count(*) from ME_13F"); show()
				cursor.execute("insert into ME_13F (InstrumentID, BUSINESSUNIT,BUSINESSUNITID, ACCOUNTINGDATE,  ASOFDATETIME) values (1,'test',1, to_date('2013-05-08T23:39:20.123'), to_timestamp('2013-05-08T23:39:20.123'))")
				cursor.execute("commit")
				cursor.execute("SELECT count(*) from ME_13F"); show()
				cursor.execute("TRUNCATE TABLE  ACCOUNTINGBI.POSITION.ME_13F"); show()
			if 0:
				cursor.execute("SELECT $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23,$24,$25,$26,$27,$28,$29,$30,$31,$32,$33,$34,$35\
				FROM '@position_model_stage_test/ME_13F/file0.IQStreamer.ysSvmR.20190524_115643.csv.gz' t ");
				for row in cursor.fetchall():
					print row
			if 1:
				cursor.execute("SELECT count(*) from ME_13F"); show()
				
				cursor.execute("""
COPY INTO ME_13F FROM '@position_model_stage_test/ME_13F/file0.IQStreamer.1qzbvu.20190524_123114.csv.gz' """
				);
				for row in cursor.fetchall():
					print row
				cursor.execute("commit")
				cursor.execute("SELECT count(*) from ME_13F"); show()
				


			if 0:
				cursor.execute("SELECT count(*) from ME_13F"); show()
				e()
				cursor.execute("SELECT count(*) from ME_13F"); #show()
				cnt=cursor.fetchone()[0]
				if 0:
					for line in open('/home/s_dev_racct/ab_ssrs_reporting_services/test/mock/ME_13F/50k.csv', 'r').readline():
						print len.split('^')
				cursor.fast_executemany = True
				cursor.execute("""
			insert into ME_13F VALUES 
				 ( 4,'2CPP',248989,'NO ADVISOR',0,'DOL.C-USAA','UNITED STATES DOLLARS','UNITED STATES DOLLARS','CURRENCY','CURRENCY',6,'Currency',0	,
				 0,0,0,260532935.71817073,260532935.71817073,0,0,0,0,0,0,0,0,1.0,0,0,
				 260532935.71817073,260532935.71817073,0,'Long','01/31/2018','2019-05-24 09:29:17'),
				 ( 4,'2CPP',248989,'NO ADVISOR',0,'DOL.C-USAA','UNITED STATES DOLLARS','UNITED STATES DOLLARS','CURRENCY','CURRENCY',6,'Currency',0	,
				 0,0,0,260532935.71817073,260532935.71817073,0,0,0,0,0,0,0,0,1.0,0,0,
				 260532935.71817073,260532935.71817073,0,'Long','01/31/2018','2019-05-24 09:29:17'),
				 ( 4,'2CPP',248989,'NO ADVISOR',0,'DOL.C-USAA','UNITED STATES DOLLARS','UNITED STATES DOLLARS','CURRENCY','CURRENCY',6,'Currency',0	,
				 0,0,0,260532935.71817073,260532935.71817073,0,0,0,0,0,0,0,0,1.0,0,0,
				 260532935.71817073,260532935.71817073,0,'Long','01/31/2018','2019-05-24 09:29:17')
				 """)
				cursor.execute("commit")
				cursor.execute("SELECT count(*) from ME_13F"); 
				print 'aaded: ', cursor.fetchone()[0] -cnt
			if 0:

				cursor.execute("SELECT count(*) from ME_13F"); #show()
				cnt=cursor.fetchone()[0]
				if 1:
					for line in open('/home/s_dev_racct/ab_ssrs_reporting_services/test/mock/ME_13F/50k.csv', 'r').readline():
						row=line.split('^')
				cursor.fast_executemany = True
				pp(row)
				e()
				stmt ="""
			insert into ME_13F VALUES 
				 (%s)
				 """ % ','.join(row)
				pp(stmt)
				cursor.execute(stmt)
				cursor.execute("commit")
				cursor.execute("SELECT count(*) from ME_13F"); 
				print 'aaded: ', cursor.fetchone()[0] -cnt
			if 0:
				cursor.execute("select * from table(information_schema.copy_history(table_name=>'ME_13F', start_time=> dateadd(hours, -1,\
				current_timestamp()))) LIMIT 1"); show()
			if 0:
				cursor.execute("SELECT count(*) from ME_13F"); show()
				a=('1','test','1', "2013-05-08", "2013-05-08")				
				params = [ ]
				for i in range(1):
					params.append(a)
				cursor.fast_executemany = False
				cursor.executemany("""insert into ME_13F (InstrumentID, BUSINESSUNIT,BUSINESSUNITID, ACCOUNTINGDATE,  ASOFDATETIME) 
				values (?,?,?,
				CAST(? AS DATE),CAST(? AS TIMESTAMP))""", params)
				
				#cursor.execute("insert into ME_13F (InstrumentID, BUSINESSUNIT,BUSINESSUNITID, ACCOUNTINGDATE,  ASOFDATETIME) values ()")
				cursor.execute("commit")
				cursor.execute("SELECT count(*) from ME_13F"); show()




		finally:
			cursor.close()