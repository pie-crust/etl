from pprint import pprint as pp
import sys
e=sys.exit

from include.cols_init import cmd , result

if 1:
	import pyodbc
	conn = pyodbc.connect('DSN=IQDEV9;uid=CIGActgDownload;pwd=m0n3ybuck3t;db=CIGActgH')
	cursor = conn.cursor()
	

	
e()

def exec_IQ(cfg,key, store):

	stmt='SET TEMPORARY OPTION DATE_ORDER=MDY exec %s %s' % (cfg['proc'], cfg['params'])
	print(stmt)
	cursor.execute(stmt)
	set_result(cursor, key, store)

def exec_Snow(cfg,key, store):
	if 1:
		import pyodbc
		conn = pyodbc.connect("DSN=SFDDATAMART;Database=ACCOUNTINGBI;WSID=ld-dbn-bofin006;APP=AnishTest;authenticator=https://home.okta.com;uid=s_dev_racct@homegroup.com;pwd=home312!;autocommit=False;ROLE=s_dev_racct_ROLE;")
		cursor = conn.cursor()
		cursor.execute("USE WAREHOUSE LOAD_WH")
		cursor.execute("USE DATABASE ACCOUNTINGBI")
		cursor.execute("USE SCHEMA POSITION")	
		cursor.execute('SELECT * from %s LIMIT 1' % cfg['table'])
		set_result(cursor, key, store)
		
def exec_S3(cfg,key, store):
	if 1:
		import pyodbc
		conn = pyodbc.connect("DSN=SFDDATAMART;Database=ACCOUNTINGBI;WSID=ld-dbn-bofin006;APP=AnishTest;authenticator=https://home.okta.com;uid=s_dev_racct@homegroup.com;pwd=home312!;autocommit=False;ROLE=s_dev_racct_ROLE;")
		cursor = conn.cursor()
		cursor.execute("USE WAREHOUSE LOAD_WH")
		cursor.execute("USE DATABASE ACCOUNTINGBI")
		cursor.execute("USE SCHEMA POSITION")	
		stmt="""SELECT %s from @position_model_stage_test_2/%s/%s t  LIMIT 1""" % (','.join(['$%s' % str(x+1) for x in range(cfg['num_of_cols'])]), key,cfg['key'])
		print (key, store)
		pp(stmt)
		#e()
		cursor.execute(stmt)
		set_result(cursor, key, store)
		
def show():
	for row in cursor.fetchall():
		pass
				
				
def show_one(cursor):
	row=cursor.fetchone()
	if row:
		for id,column in enumerate(cursor.description):
			print ('%s: %s (%s): [%s]' % (str(id+1).ljust(3), str(column[0]).ljust(25), str(column[1]).ljust(30),row[id]))
	else:
		for id,column in enumerate(cursor.description):
			print ('%s: %s (%s)' % (str(id+1).ljust(3), str(column[0]).ljust(25), str(column[1]).ljust(30)))

def set_result(cursor,key, store):
	global result 
	row=cursor.fetchone()
	#result[key]={store:[]}
	a=result[key][store]
	
	if row:
		for id,column in enumerate(cursor.description):
			a[id+1]=(column[0], column[1],row[id])
	else:
		for id,column in enumerate(cursor.description):
			a[id+1]=(column[0], column[1])

def gen_report(res):
	s3=res['S3']
	snow=res['Snow']
	iq=res['IQ']
	pp(iq)
	pp(s3)
	pp(snow)
	for i in range(max([len(s3), len(snow), len(iq)])):
		a=iq.get(i+1)
		b=s3.get(i+1)
		c=snow.get(i+1)
		print ('%d\t%s\t%s\t%s' %( i, '%s\t[%s]' %(a[0],str(a[2])) if a else '-\t[-]',  '%s\t[%s]' %  (c[0],str(c[2])) if c else '-\t[-]','%s\t[%s]' % (b[0],str(b[2])) if b else '-\t[-]'))
		

proc='DY_Position_SD'
for key, val in cmd.items():
	print (key)
	pp(val)
	if key in [proc]:
		for store, val2 in val.items():
			print  (store, key)
			if 1:
				if store=='IQ':
					exec_IQ(val2, key, store)
			if 1:
				if store=='Snow':
					exec_Snow(val2, key, store)	
					#pp(result['DY_FinancingPosition'].keys())
			if 1:
				if store=='S3':
					exec_S3(val2,key,  store)
					#pp(result['DY_FinancingPosition'].keys())
		gen_report(result[key])