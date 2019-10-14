import pyodbc
from pprint import pprint
import sys
e=sys.exit



def show(cursor):
	for row in cursor.fetchall():
		print(row)

#/opt/vertica/bin/vsql -h VDGMBO1.homegroup.com s_dev_rdm
if 1:
	connStr='Driver=Vertica;ServerName=VDGMBO1.homegroup.com;Database=VDGMBO1;KerberosServiceName=vertica;UID=s_dev_actrpt'
	print connStr
	conn = pyodbc.connect(connStr)
	print 'Connected!'