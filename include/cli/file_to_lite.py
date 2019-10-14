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
import json, logging
from datetime import datetime
import tempfile, traceback
from pprint import pprint as pp

from include.cli.common.Cli import Cli
from include.cli.common.Teardown import Teardown
e=sys.exit

from include.utils import ctimeit
try:
	import cStringIO
except ImportError:
	import io as cStringIO
	
log=logging.getLogger('cli')

class file_to_lite(Cli, Teardown):
	@ctimeit
	def __init__(self,*args, **kwargs):
		Cli.__init__(self, *args, **kwargs)
		Teardown.__init__(self, *args, **kwargs)
		self.proc_config()
		log.info('Env: [%s]' % self.rte)
		self.start_time = time.time()
		
		self._source=None

	def get_appendix(self):
		return '', ''
	@ctimeit
	def proc_config(self):
		pcf=self.pcf
		self.paramlist = "','".join(self.pa)
		with open(pcf, 'r') as f:
			
			try:
				self.cfg=cfg = json.loads(f.read())
			except:
				
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
			#pp(scfg)
			#e()
			self.tcfg=tcfg=cfg['target']
	
			
		self.proc_key = os.path.basename(self.pcf).split('.')[0]
		self.tearcfg=tearcfg=cfg['teardown']
		tearfn=self.get_parsed(ckey='teardownQueryFile', cfg=tearcfg) 
		assert os.path.isfile(tearfn)
		
		assert tearfn.endswith('.py')
		tearpy=None
		with open(tearfn,'r') as fh:
			tearpy=fh.read()
		self.tear=tear=eval(tearpy)
		assert 'source' in tear
		self.sqf_name=self.tdir_path=self.sqf_path={}
		for src in tear['source']:
			#print src
			self.sqf_name[src]	= None
			self._source=src
			self.tdir_path[src] = self.get_parsed(ckey='targetDir', cfg=tcfg[src])
			if not os.path.isdir(self.tdir_path[src]):
				os.makedirs(self.tdir_path[src])
			stmt = tear['source'][src]
			self.scfg[src]['sourceStmt'] =[ stmt, 0]
			
		self._source=None
		#pp(self.scfg)


			
		
			
		self.max_rows_to_read=10<30
			
		if self.lame_duck and self.lame_duck<self.max_rows_to_read:
			self.max_rows_to_read=self.lame_duck
		assert self.max_rows_to_read
		if 1:
			self.tab_root	= self.get_tab_root()
			#self.db	= self.pa[1]
			if not  os.path.isdir(self.tab_root):
				os.makedirs(self.tab_root)


		
		log.debug('Starting [%s].' % self.proc_key)
	def get_tab_root(self):	
		
		return self.pa[1]
	def set_source(self, key):
		self._source=key

	def get_tcfg(self):
		assert self._source
		return self.tcfg[self._source]
	def get_scfg(self):
		assert self._source
		return self.scfg[self._source]
	
	def get_sqf_name(self):
		assert self._source
		return self.sqf_name[self._source]
	def get_cfg(self, key):
		return self.cfg[key][self._source]



