import os, time, tempfile
import logging
from pprint import pprint
import sys
e=sys.exit
from pprint import pprint as pp
cursor=None

from include.fmt import psql
def show():
	global cursor
	for row in cursor.fetchall():
		print(row)
if 1:
	pid = os.getpid()
	

	tmp_fn = next(tempfile._get_candidate_names())
	
	tmpdir =os.getenv('G3_TEMP_DIR', '/tmp')
	log_dir =os.path.join(tmpdir,'iq')
	latest_dir = os.path.join(log_dir, 'latest')
	ts = time.strftime('%Y%m%d_%H%M%S')
	ts_dir = os.path.join(log_dir, ts)
	if not os.path.exists(ts_dir):
		try:
			os.makedirs(ts_dir)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
			else:
				pass
		
		
	DEBUG = 1
	
	FORMAT = '%(asctime)s|%(levelname)s|%(process)d|%(module)s.py|%(funcName)s|%(lineno)d|  %(message)s'
	lfile = os.path.join(ts_dir, '%s_%d_%s.log' % ('iq', pid, tmp_fn))

	logging.basicConfig(
		filename=lfile,
		level=logging.DEBUG,
		format=FORMAT,
		datefmt="%Y-%m-%d %H:%M")
		
	log =  logging.getLogger('iq')
	#self.log.stream = sys.stderr
	#self.log_handler = logging.StreamHandler(sys.stderr)
	#self.log.addHandler(self.log_handler)
	if 1:
		log.handler = handler=logging.StreamHandler(sys.stdout)
		handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter(FORMAT,datefmt="%Y-%m-%d %H:%M:%S")
		handler.setFormatter(formatter)
		#pprint(dir(handler))
		log.addHandler(handler)
	log.file_name=lfile
	if 0:
		logging.getLogger('boto3').setLevel(logging.WARNING)
		logging.getLogger('boto').setLevel(logging.WARNING)
		logging.getLogger('botocore').setLevel(logging.WARNING)
		logging.getLogger('nose').setLevel(logging.WARNING)
		logging.getLogger('s3transfer').setLevel(logging.WARNING)
		logging.getLogger('urllib3').setLevel(logging.WARNING)
		logging.getLogger('kerberos').setLevel(logging.WARNING)
	
	log.info('Log:'+lfile)
		
def info(msg):
	log.info(msg)
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
		info('Start')
		cursor = conn.cursor()
		dbdata=[]
		if 1:
			stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spSOI_Cnsldtd_WRAPPER '223906','EOD','2019/1/30','DESK','*','DEFAULT','REGULAR','1','0','NONE','*','*','N','0','0','NONE','NONE','ALL','0','MONTH_END','N','ALL','*','0','*','N','*'"
			tbl='DY_FinancingPosition'
			stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spTDPFinancialPosRptCnsldtd_WRAPPER '223907','2019/9/13','2019/9/13','EOD','EOD','*','*','*','NONE','*','NOW','0'"
			tbl='ME_FinancingPosition'
			stmt="SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgH.spTDPFinancialPosRptCnsldtd_WRAPPER '223906','2019/8/01','2019/8/31','EOD','EOD','*','*','*','NONE','*','NOW','0'"
			stmt="select * from  Position.ME_FinancingPosition where AccountingDate='2019-08-31' and client=223906"
			tbl='DY_FinancingPosition'
			stmt="select * from  Position.%s where AccountingDate='2019-09-13' and client=223906" % tbl
			psql(os.linesep.join(stmt.split()),tbl)
			cursor.execute(stmt)

			t=0
			i=1
			eol='\n'
			colsep='|'
			
			start_time = time.time()
			fn='%s.csv'% (tbl)
			info(fn)
			with open(fn , 'w') as fh:
				fh.write(colsep.join([c[0] for c in cursor.description])+eol)
				row=cursor.fetchone()
				if row:
					info('First row: %s' % row)
					fh.write(colsep.join([c if isinstance(c, unicode) else str(c).encode() for c in row])+eol)
					
				else:
					info('no data')			
				
				while row:
					
					row=cursor.fetchone()
					if row :
						fh.write(colsep.join([c if isinstance(c, unicode) else str(c).encode() for c in row])+eol)
						i +=1
					if 0:
						dbdata.append(row)
						i +=1
						if i ==25000:
							t +=i
							
							
							if 1:

								fh.write(eol.join([colsep.join([c if isinstance(c, unicode) else str(c).encode() for c in r]) for r in dbdata])+eol)
							dbdata=[]
							info('Elapsed %s' % (time.time() - start_time))
							start_time = time.time()
							i=0
			print i
			
