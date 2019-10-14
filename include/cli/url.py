(home, app_name, log)=app_init
import os, sys, re, time
import json
from datetime import datetime
import tempfile
from pprint import pprint as pp

from include.cli.common.Cli import Cli
e=sys.exit

class source_cfg():
	def __init__(self,cfg):
		self.cfg=cfg['source']

		
class target_cfg():
	def __init__(self,cfg):
		self.cfg=cfg
		
class s3_cfg():
	def __init__(self,cfg):
		self.cfg=cfg
		
		
class url(Cli):
	def __init__(self,*args, **kwargs):
		Cli.__init__(self, *args, **kwargs)

		#self.wflow=kwargs.get('work_flow', None)
		self.csep='^'
		pp( self.lame_duck)
		#e()
		if 1:
			temp_name = next(tempfile._get_candidate_names())
			tss=datetime.now().strftime('%Y%m%d_%H%M%S')
			self.filter='%s.%s' % (temp_name,tss)
		assert self.dcf, 'Provide db config file name [-dcf]'
		assert self.dcf, 'Provide proc config file name [-pcf]'
		self.db_config()
		self.proc_config()
		log.info('Env: [%s]' % self.rte)
		self.start_time = time.time()
	def get_runtime_env_vars(self):
		return self.dbcfg['env'][self.rte]['env_vars']
		
	def proc_config(self):
		pcf=self.pcf
		log.info('Proc conf: %s' % pcf)	
		pp(self.pa)
		
		self.paramlist = "','".join(self.pa)
		
		with open(pcf, 'r') as f:
			cfg = json.loads(f.read())
			self.scfg=scfg=cfg['source']
			self.tcfg=tcfg=cfg['target']
			self.s3cfg=s3cfg=cfg['s3']
			self.ucfg=ccfg=cfg['url']


		self.to_dir=s3cfg['targetDir']

		self.proc_key=os.path.basename(self.pcf).split('.')[0]
		
		assert int(s3cfg["maxRecordsInFile"])>= int(s3cfg["writeBufferSize"])
		if 1:
			###############
			self.max_rows_to_read=int(s3cfg["maxRecordsInFile"])
			#self.max_rows_to_read=65000
			###############
			if self.lame_duck and self.lame_duck<self.max_rows_to_read:
				self.max_rows_to_read=self.lame_duck
		assert self.max_rows_to_read

			

		
		

