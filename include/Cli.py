
import os, sys, re, time
import json
from datetime import datetime
import tempfile
from pprint import pprint as pp

e=sys.exit



class Cli(object):
	def __init__(self,*args,**kwargs):
		self.dcf = kwargs.get('db_config_file', None)
		self.pcf = kwargs.get('proc_config_file', None)
		print self.pcf
		e()
		self.rte = kwargs.get('runtime_environment', None)	
		self.pa = kwargs.get('proc_params', None)	
		self.mf = kwargs.get('mock_file', None)
		self.dump = kwargs.get('dump', None)
		self.lame_duck=kwargs.get('lame_duck', None)
		self.dd=kwargs.get('dump_dir', None)
		self.sr=kwargs.get('skip_rows', None)
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
		log.info('Env: [%s]' % self.rte)
		self.start_time = time.time()

	def get_aws_keys(self):
		SUCCESS=200
		if 1:
			response = requests.post('https://datakeep.homegroup.com/api/v2/create_access_credentials', auth=HTTPKerberosAuth())
			print response.status_code
			assert response.status_code == SUCCESS, 'Create creds failed'
		data = None
		while not data:
			if not data: time.sleep(2)
			res = requests.get('https://datakeep.homegroup.com/api/v2/get_access_credentials', auth=HTTPKerberosAuth())
			assert res.status_code == SUCCESS, 'Get creds failed'
			if res.status_code == SUCCESS:
				data = res.json()[0]
				length = len(data)
				pp(data)
				assert 'access_key_id' in data
				assert 'secret_access_key' in data
				e()
		return None, None
			
			
	def db_config(self):
		dcf=self.dcf
		log.info('Db conf: %s' % dcf)
		with open(dcf, 'r') as f:
			self.dbcfg = json.loads(f.read())
			self.stores = self.dbcfg["stores"]
	def get_db_env_vars(db='IQ')
		dbenv=self.dbcfg['env'][self.rte][db]
		return self.stores[dbenv]['env_vars'])
