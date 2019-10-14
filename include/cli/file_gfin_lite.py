(cli, conn_pool)=app_init
import os, sys, re, time
import json, logging
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
	
log=logging.getLogger('cli')

class file_gfin_lite(Cli):
	@ctimeit
	def __init__(self,*args, **kwargs):
		Cli.__init__(self, *args, **kwargs)
		
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
				print ('#' * 80)
				print ('ERROR when parsing proc json file', pcf)
				print ('#' * 80)
				print (error)
				print ('#' * 80)
				print ('#' * 80)
				e(1)
			
			#self.scfg=scfg=cfg['source']
			#pp(scfg)
			#e()
			#self.tcfg=tcfg=cfg['target']
	
			
		self.proc_key = os.path.basename(self.pcf).split('.')[0]


			
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




