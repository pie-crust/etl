import sys, time
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
		
		
mm=[31,29,31,30,31,30,31,31,30,31,30, 31]

clid=223906

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

		if 0:
			cur.execute(""" select  extract(YEAR from ACCOUNTINGDATE) yr,extract(MONTH from ACCOUNTINGDATE) mo,  
			SUM(CASE clientid WHEN 223906 THEN 1 ELSE 0 END) cnt_223906, 
			SUM(CASE clientid WHEN 223907 THEN 1 ELSE 0 END) cnt_223907
      from ACCOUNTINGBI.PL_HIST.DY_DESKPLRSRANGE03
      group by  1,2 order by 1,2,3,4"""); show()
				
sum=0
mon=9
year=2016
table='DY_DeskPLRSRange03'

for x in range(1,mm[mon-1]+1):
	if x not in [3,4,10,11,17,18]:
		cur.execute(""" select  extract(YEAR from ACCOUNTINGDATE) yr,extract(MONTH from ACCOUNTINGDATE) mo,  
				SUM(CASE clientid WHEN 223906 THEN 1 ELSE 0 END) cnt_223906, 
				SUM(CASE clientid WHEN 223907 THEN 1 ELSE 0 END) cnt_223907
		  from ACCOUNTINGBI.PL_HIST.%s
		  WHERE clientid= %s and ACCOUNTINGDATE='%02d/%02d/%s'
		  group by  1,2""" % (table, clid,mon ,x, year)); 
		rows=cur.fetchall()
		#print x, len(rows)
		if len(rows):
			sum +=rows[0][3]
			#print rows[0][3], sum
		else:
			params="%s '%02d/%02d/%d' '%02d/%02d/%d'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'" % (clid, mon,x,year, mon,x, year)
			cmd= "~/python27/bin/python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/%s.json --proc_params %s" % (table, params)
			print table, year, mon, x
			pipe=subprocess.Popen([cmd], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

			line= pipe.stderr.readline()
			while line: #pipe.poll() is None:
				print 'ERROR:', line			
				line= pipe.stderr.readline()

			while	pipe.poll() is None:
				print 'Waiting...'
				time.sleep(1)
			print("retcode =", pipe.returncode)
		#e()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
if 0:
	for i in range(1,32):
		print """
	python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/%02d/2016' '05/%02d/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'

		""" % (i,i,i,i,i,i,i,i)