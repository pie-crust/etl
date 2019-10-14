import sys, time
import subprocess
from pprint import pprint as pp
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
				

mon=1
year=2018
table='DY_FinancingPosition'
wf='sql_stream_s3_snow'

clid=223907

def get_cmd( **kwargs):
	table=kwargs.get('table')
	assert table
	if table =='ME_Position_SD':
		return """~/python27/bin/python ./cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/pos/{wf}/{table}.json --proc_params \
{clid} {mon:02d}/{day:02d}/{year} 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" """.format(**kwargs)


def run_DY(**kwargs):
	ignore=kwargs.get('ignore')

	for x in range(1,mm[mon-1]+1):
		if x not in ignore:
			if 0:
				cur.execute(""" select  extract(YEAR from ACCOUNTINGDATE) yr,extract(MONTH from ACCOUNTINGDATE) mo,  
			SUM(CASE CLIENT WHEN 223906 THEN 1 ELSE 0 END) cnt_223906, 
			SUM(CASE CLIENT WHEN 223907 THEN 1 ELSE 0 END) cnt_223907
		from ACCOUNTINGBI.POSITION.%s
		WHERE CLIENT= {clid} and ACCOUNTINGDATE='%02d/%02d/%s'
		group by  1,2""" % (table, clid,mon ,x, year)); 
				rows=cur.fetchall()


			if 0:
				params="%s   '%02d/%02d/%d' '%02d/%02d/%d' EOD EOD 'HORZ' '*' '*' NONE '*' NOW 0" % (clid, mon,x,year, mon,x, year)
				cmd= "~/python27/bin/python cli.py -nopp 12  -dcf config/db_config.DEV.json -pcf config/proc/pos/%s/%s.json --proc_params %s" % ( wf,table, params)
			#clid, table, wf, year, mon, ignore
			kwargs.update({'day':x})
			cmd=get_cmd(**kwargs)
			#pp(cmd)
			#e()
			print clid, wf, table, year, mon, x
			print cmd
			if 1:
				pipe=subprocess.Popen([cmd], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

				line= pipe.stdout.readline()
				every=False
				while line: #pipe.poll() is None:
					if every or '|ERROR|' in line:
						every=True
						print 'ERROR:', line.strip()			
					line= pipe.stdout.readline()

				while	pipe.poll() is None:
					print 'Waiting...'
					time.sleep(1)
				print("retcode =", pipe.returncode)
def run_ME(**kwargs):
	ignore=kwargs.get('ignore')

	for mon, x in enumerate(mm):
		mon=mon+1
		if x not in ignore:
			if 0:
				cur.execute(""" select  extract(YEAR from ACCOUNTINGDATE) yr,extract(MONTH from ACCOUNTINGDATE) mo,  
			SUM(CASE CLIENT WHEN 223906 THEN 1 ELSE 0 END) cnt_223906, 
			SUM(CASE CLIENT WHEN 223907 THEN 1 ELSE 0 END) cnt_223907
		from ACCOUNTINGBI.POSITION.%s
		WHERE CLIENT= {clid} and ACCOUNTINGDATE='%02d/%02d/%s'
		group by  1,2""" % (table, clid,mon ,x, year)); 
				rows=cur.fetchall()


			kwargs.update({'day':x})
			cmd=get_cmd(**kwargs)
			#pp(cmd)
			#e()
			print clid, wf, table, year, mon, x
			print cmd
			if 1:
				pipe=subprocess.Popen([cmd], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

				line= pipe.stdout.readline()
				every=False
				while line: #pipe.poll() is None:
					if every or '|ERROR|' in line:
						every=True
						print 'ERROR:', line.strip()			
					line= pipe.stdout.readline()

				while	pipe.poll() is None:
					print 'Waiting...'
					time.sleep(1)
				print("retcode =", pipe.returncode)
if __name__=="__main__":
	run_ME(clid=clid, table='ME_Position_SD', wf=wf, year=year, mon=mon, ignore=[])
	
	
	
	"""('retcode =', 0)
223907 sql_stream_s3_snow DY_FinancingPosition 2018 2 29
~/python27/bin/python ./cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/pos/sql_stream_s3_snow/ME_Position_SD.json --proc_params 223907 01/29/2018 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*"
	"""
	
	
	
	
	
	
	
	
	
	
	
	
	
	
