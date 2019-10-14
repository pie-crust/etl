
from pprint import pprint
import sys
e=sys.exit

cursor=None

def show():
	global cursor
	for row in cursor.fetchall():
		print(row)
				
				
def show_one():
	global cursor
	row=cursor.fetchone()
	if row:
		for id,column in enumerate(cursor.description):
			print '%s: %s (%s): [%s]' % (str(id+1).ljust(3), str(column[0]).ljust(25), str(column[1]).ljust(30),row[id])
	else:
		for id,column in enumerate(cursor.description):
			print '%s: %s (%s)' % (str(id+1).ljust(3), str(column[0]).ljust(25), str(column[1]).ljust(30))
if 1:
	import pyodbc
	conn = pyodbc.connect('DSN=IQDEV9;uid=CIGActgDownload;pwd=m0n3ybuck3t;db=CIGActgH')
	
	
	#e()
	if 1:
		cursor = conn.cursor()
		#stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.sp_Util_13F_WRAPPER '01/31/2018','223906','EOD','*','0','ALL','DETAIL','*','0','N','N','N'"
		#stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spTDPFinancialPosRptCnsldtd_WRAPPER '223906','01/01/2018','01/01/2018','EOD','EOD','*','*','*','NONE','*','NOW','1'"
		stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spSettleDatePosition_WRAPPER '223906','01/01/2018','EOD','ACCT','*','*','*','*','*','*','*','*','*','*','*','*','*','*'"
		stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spTDPFinancialPosRptCnsldtd_WRAPPER '223906','01/01/2018','01/01/2018','EOD','EOD','HORZ','*','*','NONE','*','NOW','0'"
		stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spSettleDatePosition_WRAPPER '223906','01/01/2018','EOD','ACCT','*','*','*','*','*','*','*','*','*','*','*','*','*','*'"
		stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spSOI_Cnsldtd_WRAPPER '223906','01/02/2018','ACCT','*','DEFAULT','REGULAR','1','0','NONE','*','*','N','0','0','NONE','ALL','0','FULL','NONE','N','ALL','*','0','*','Y','*'"
		stmt="SET TEMPORARY OPTION DATE_ORDER=MDY  \
		exec CIGActgH.spSOI_Cnsldtd_WRAPPER '223906','2018-01-01','2018-01-01 12:08:15','ACCT','*','DEFAULT','REGULAR','1','0','NONE','*','*','N','0','0','NONE','ALL','0','FULL','NONE','N','ALL','*','0','*','Y','*'"
		
		stmt="""select convert(varchar(30),o.name) AS table_name
from sysobjects o
where type = 'U'
order by table_name
"""
		stmt="""Select distinct sysobjects.name
, case 
 when sysobjects.type = 'TR' then 'TRIGGER' 
 when sysobjects.type = 'P' then 'PROCEDURE' 
 when sysobjects.type = 'V' then 'VIEW' 
 else 'UNKNOWN' end type
from sysobjects inner join syscomments
on sysobjects.id = syscomments.id
where syscomments.text like '%tbl_books%'"""
		cursor.execute(stmt)
		show()
