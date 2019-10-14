"""
 time python cli.py -nopp 4 --dump  -dcf config/db_config.json -pcf config/proc/snow_url_sql/DY_FinancingPosition.json \
 --proc_params  Repo '2018-12-31 00:00:00' "$(date +"%Y-%m-%d %H:%M:%S")" e5569eb7-e333-4e28-ad77-0f224a7d2499@1
#
# pa[0] = ReferenceType
# pa[1] = AccountingDate
# pa[2] = AsOfDateTime
# pa[3] = gatoken
#


"""
(cli, conn_pool)=app_init
import os, sys, re, time
import json
from datetime import datetime
import tempfile, traceback
from pprint import pprint as pp

from include.cli.common.Cli import Cli
e=sys.exit

from include.utils import ctimeit
try:
	import cStringIO
except ImportError:
	import io as cStringIO
	

		
class iq_mem_sql(Cli):
	@ctimeit
	def __init__(self,*args, **kwargs):
		Cli.__init__(self, *args, **kwargs)

		self.proc_config()
		log.info('Env: [%s]' % self.rte)
		self.start_time = time.time()
		#self.apx=''
	def get_appendix(self):
		return '', ''
	@ctimeit
	def proc_config(self):
		pcf=self.pcf
		log.info('Proc conf: %s' % pcf)	
		#pp(self.pa)
		
		self.paramlist = "','".join(self.pa)
		
		with open(pcf, 'r') as f:
		
			
			try:
				cfg = json.loads(f.read())
			except:
				if 1:
					
					err_log = cStringIO.StringIO()
					traceback.print_exc(file=err_log)
					error = err_log.getvalue()
					print '#' * 80
					print 'ERROR when parsing proc json file', pcf
					print '#' * 80
					print(error)
					print '#' * 80
					print '#' * 80
					e()
			
			self.scfg=scfg=cfg['source']
			self.tcfg=tcfg=cfg['target']
			
			self.rcfg=ccfg=cfg['rest']
			
		self.proc_key=os.path.basename(self.pcf).split('.')[0]
		
		self.max_rows_to_read=10<30
			
		if self.lame_duck and self.lame_duck<self.max_rows_to_read:
			self.max_rows_to_read=self.lame_duck
		assert self.max_rows_to_read



