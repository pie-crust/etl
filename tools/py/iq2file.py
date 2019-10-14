import os, sys, io, csv, time, boto, gzip, math
import pyodbc
e=sys.exit
from pprint import pprint as pp



file_rows=500000
write_file='prod_07_03012016_dump.csv'
if __name__=="__main__":


		
	import pyodbc
	sconn = pyodbc.connect('DSN=IQPROD9;uid=CIGActgDownload;pwd=m0n3ybuck3t;db=CIGActgH')	
	scur = sconn.cursor()
	scur.arraysize=file_rows
	

	
	stmt="""SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spDeskPLBUC_Inner_Range_01_WRAPPER '223907','03/01/2016',
'03/01/2016','EOD','*','*','*','*','*','*','*','ALL','TABLE_EDITOR_DEFAULT','TABLE_EDITOR_DEFAULT','DESK_PL_RANGE_03',
'FUND','ABOVE_THE_WALL','s_prod_racct'"""

	scur.execute(stmt)

	with open(write_file, 'wb') as fh:
		writer = csv.writer(fh, dialect='excel', delimiter=',')
		while True:
			rows = scur.fetchmany(file_rows)
			print len(rows)
			writer.writerows(rows)
			if not rows:
				break;

	
