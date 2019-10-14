import sys, time
from pprint import pprint as pp
import subprocess
e=sys.exit
def show():
	global cursor
	try:
		for row in cur.fetchall():
			print(row)
			
	except Exception, ex:
		print str(ex)
		print 'nothing o show'
		
		


if 1:
	import pyodbc
	pyodbc.pooling = False
	conn = pyodbc.connect("DSN=SFDDATAMART;Database=ACCOUNTINGBI;WSID=ld-dbn-bofin006;APP=AnishTest;authenticator=https://home.okta.com;uid=s_dev_racct@homegroup.com;pwd=home312!;autocommit=False;ROLE=s_dev_racct_ROLE;")
	conn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
	if 1:
		cur = conn.cursor()
		cur.execute("USE WAREHOUSE LOAD_WH")
		cur.execute("USE DATABASE ACCOUNTINGBI")
		cur.execute("USE SCHEMA POSITION")



mm=[31,29,31,30,31,30,31,31,30,31,30, 31]


sum=0

mon=1
year=2017
table='DY_DeskPLRSRange03'
def load_day(table, year, mon, clid):
	mf = "-mf 'dump/DY_DeskPLRSRange03/raw_dump.s2iyzK.20190718_152436.csv'"
	
	params="%s '%02d/%02d/%d' '%02d/%02d/%d'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'" % (clid, mon,x,year, mon,x, year)
	cmd= "~/python27/bin/python cli.py -nopp 18  --no-dump  -dcf config/db_config.DEV.json -pcf config/proc/pnl/iq_stream_s3_snow/%s.json --proc_params %s " % (table, params)
	print table, year, mon, clid
	print cmd
	#e()
	if 1:
		pipe=subprocess.Popen([cmd], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
		line= pipe.stdout.readline()
		while line: #pipe.poll() is None:
			print 'OUTPUT:', line.strip()			
			line= pipe.stdout.readline()
		line= pipe.stderr.readline()
		while line: #pipe.poll() is None:
			print 'ERROR:', line			
			line= pipe.stderr.readline()

		while	pipe.poll() is None:
			print 'Waiting...'
			time.sleep(1)
		print("retcode =", pipe.returncode)
					
for x in range(1,mm[mon-1]+1):
	if not x  in []:
		stmt=""" select  extract(YEAR from ACCOUNTINGDATE) yr,extract(MONTH from ACCOUNTINGDATE) mo,  
	SUM(CASE clientid WHEN 223906 THEN 1 ELSE 0 END) cnt_223906, 
	SUM(CASE clientid WHEN 223907 THEN 1 ELSE 0 END) cnt_223907
from ACCOUNTINGBI.PL_HIST.%s
WHERE ACCOUNTINGDATE='%02d/%02d/%s'
group by  1,2""" % (table, mon ,x, year)
		print(stmt)
		cur.execute(stmt); 
		rows=cur.fetchall()
		if rows:
			c06, c07 = rows[0][2], rows[0][3]
			if (not c06 and c07):
				clid=223906
				print x, rows[0][2], rows[0][3]
				load_day(table, year, mon, clid)
				#e()
			elif (c06 and not c07):
				print x, rows[0][2], rows[0][3]
			else:
				print x, rows[0][2], rows[0][3]
				#e()
		else:
			print x, rows

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
