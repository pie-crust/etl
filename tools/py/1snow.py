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
from pprint import pprint
import sys
e=sys.exit



def show(cursor):
	for row in cursor.fetchall():
		print(row)

			
if 1:
	import pyodbc
	conn = pyodbc.connect("DSN=SFDDATAMART;Database=ACCOUNTINGBI;WSID=ld-dbn-bofin006;APP=AnishTest;authenticator=https://home.okta.com;uid=s_dev_racct@homegroup.com;pwd=home312!;autocommit=False;ROLE=s_dev_racct_ROLE;")
	#cxn = pyodbc.connect("DSN=SFDDATAMART;Database=ACCOUNTINGBI;WSID=ld-dbn-bofin006;APP=AnishTest;authenticator=https://home.okta.com;uid=s_dev_racct@homegroup.com;pwd=home312!;autocommit=False;ROLE=s_dev_racct_ROLE;")
	
	#e()
	print 'Connected!'
	if 1:
		cursor = conn.cursor()
		cursor.execute("USE WAREHOUSE LOAD_WH")
		cursor.execute("USE ROLE AccountingBI_W")
		cursor.execute("USE DATABASE ACCOUNTINGBI")
		cursor.execute("USE SCHEMA POSITION")
			
		if 1:
			cursor.execute("desc table ACCOUNTINGBI.POSITION.ME_FINANCINGPOSITION")
			show(cursor)

