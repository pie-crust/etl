import os, sys
import pyodbc
import traceback
from pprint import pprint as pp
e=sys.exit
DB_READER_DATA_DIR = 'dump'

if 1:

	if 1:

		pyodbc.pooling = False
		
		connString = 'DSN=IQDEV9;uid=CIGActgDownload;pwd=m0n3ybuck3t;db=CIGActgH'
	
		#pp(connString)
		#e(0)
		assert not os.getenv('LD_PRELOAD')
		assert os.getenv('LD_LIBRARY_PATH') #pyodbc will fail w/o exception
		assert os.getenv('ODBCINI')
		assert os.getenv('ODBCSYSINI')
		assert os.getenv('PYTHONPATH')
		#assert os.getenv('KRB5_CLIENT_KTNAME')

		
		
		if 0:
			with pyodbc.connect(connString) as conn:
				if 0:
					with con.cursor() as cur:
						cur.fast_executemany = True
						cur.executemany(sql, data)
						con.commit()
		print 333
		#e()
		print(connString)
		conn = pyodbc.connect('DSN=IQDEV9;uid=CIGActgDownload;pwd=m0n3ybuck3t;db=CIGActgH')
		print(conn) 
		cur = conn.cursor()
		print(123)
		#proc =  procConfig['procName']
		#paramlist = str(params).strip('[]')
		#stmt = 'SET TEMPORARY OPTION DATE_ORDER=MDY exec {} {}'.format(proc, paramlist) if DB_READ_SERVER.find('IQ') != -1 else 'exec {} {}'.format(proc, paramlist)
		stmt="""
SET TEMPORARY OPTION DATE_ORDER=MDY 
exec CIGActgH.spTDPFinancialPosRptCnsldtd_WRAPPER 
'223906'
, '05/12/2019'
, '05/12/2019'
, 'EOD', 'EOD'
, '*'
, '*'
, '*'
, 'NONE'
, '*'
, 'NOW'
, '0'
		"""
		if 0:
			stmt = """SET TEMPORARY OPTION DATE_ORDER=MDY  exec CIGActgH.spFIRPTAReport_WRAPPER	
 @pClientID=223906 
, @pStartDate='01/01/2018'
, @pEndDate='01/01/2018'
, @pEndStage='EOD'
, @pFund='*'
, @pAccount='*'
, @pPosType='ACCT'
, @pDesk='*'
, @pPosBlock='*'
, @pInstrument='*'"""
		
		print('-'*80)
		pp(stmt)
		#e()
		cur.execute(stmt)
 
		field_names = [val[0] for val in cur.description]
		rows = cur.fetchall()
		logging.info('{} rows returned by executing proc: {}'.format(len(rows), proc))
		
		cur.close()
		conn.close()
		pp(dir(rows))
		print(len(rows))
