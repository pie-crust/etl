
import os, sys, re, time
import json, logging
from datetime import datetime
import traceback
import tempfile
import multiprocessing
from pprint import pprint as pp
from include.utils import awscreds 
log=logging.getLogger('cli')
e=sys.exit

from include.utils import create_reader

from include.utils import ctimeit, clierr
try:
	import cStringIO
except ImportError:
	import io as cStringIO


if sys.version_info[0] >= 3:
	unicode=bytes

class Cli(object):
	#@ctimeit
	def __init__(self,*args,**kwargs):
		self.cli_kwargs=kwargs
		self.dcf  = kwargs.get('db_config_file', None)
		self.pcf  = kwargs.get('proc_config_file', None)
		self.rte  = kwargs.get('runtime_environment', None)	
		self.pa   = list(kwargs.get('proc_params', None)	)
		self.mf   = kwargs.get('mock_file', None)
		self.dump = kwargs.get('dump', None)
		self.lame_duck = kwargs.get('lame_duck', None)
		self.dd	 = kwargs.get('dump_dir', None)
		self.sr	 = kwargs.get('skip_rows', None)
		self.dop = kwargs.get('degree_of_parallelism', None)
		self.skew_pct = kwargs.get('skew_pct', None)
		self.asod= time.strftime("%Y-%m-%d %H:%M:%S") 
		self.csep= b'^'
		self._source=self._src_class=self._trg_class=self._dmp_class=None
		assert self.dop< multiprocessing.cpu_count() * 4
		if 0:
			self.aws_keys=self.get_aws_keys()
		if 1:
			temp_name = next(tempfile._get_candidate_names())
			self.tss=datetime.now().strftime('%Y%m%d_%H%M%S')
			self.filter='%s.%s' % (temp_name,self.tss)
		assert self.dcf, 'Provide db config file name [-dcf]'
		assert self.dcf, 'Provide proc config file name [-pcf]'
		self.cfg=self.scfg=self.tcfg=self.dcfg=self.s3cfg=None
		self.db_config()
		self.proc_config()
		if 0:
			self.apx_cmap,self.apx=self.get_appendix()
		else:
			self.apx_cmap,self.apx = None,None
		self.start_time = time.time()
	def set_source(self, key):
		self._source=key
		
	@ctimeit
	def get_aws_keys(self):
		log.debug('First try to get keys.')
		aws_keys=awscreds.get_aws_keys(max_tries=1)
		if not aws_keys[0] or not aws_keys[1]:
			log.debug('Creating keys.')
			aws_keys=awscreds.create_aws_keys()
			log.debug('Second try to get keys after create.')
			aws_keys=awscreds.get_aws_keys(max_tries=10)
		if not aws_keys[0] or not aws_keys[1]:
			log.error('Cannot get aws keys')
			raise Exception(clierr.E_GET_AWS_KEYS_FAILED[0])
		return aws_keys
		
	@ctimeit
	def db_config(self):
		dcf=self.dcf
		assert os.path.isfile(dcf), 'DB config file does not exists:\n%s' % dcf
		with open(dcf, 'r') as f:
			try:
				self.dbcfg = json.loads(f.read())
			except:
				err_log = cStringIO.StringIO()
				traceback.print_exc(file=err_log)
				error = err_log.getvalue()
				print ('#' * 80)
				print ('ERROR when parsing DBconfig json file', dcf)
				print ('#' * 80)
				print(error)
				print ('#' * 80)
				print ('#' * 80)
				e()
		
				
			self.stores = self.dbcfg["stores"]
	def get_alt_cols(self, cfg):
		return {c["altColName"]:c["columnName"] for c in cfg["columnMappings"] if c.get("altColName", None)}
	def header_size(self, cfg):
		return cfg["writeHeader"]
		
	def get_load_cols(self, toDB, cfg, data_files):
		scfg, dir_scfg = cfg 
		acols= self.get_alt_cols(scfg)
		tcols=toDB.get_cols()
		fcols_alt=[]
		for data_file in data_files.file_names:
			dataFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=data_file, scfg=dir_scfg)
			dataFile.describe()
			fcols_alt=[acols.get(x,x) for x in  dataFile.get_header(data_file, dir_scfg)]
			assert not set(fcols_alt) -set(tcols), 'File has columns missing in table.'
			assert not set(tcols) -set(fcols_alt), 'Table has columns missing in file.'
		assert fcols_alt
		return fcols_alt

				
	def get_store_env_refs(self,db):
		#db=db.split('_')[0]
		#print db
		dbenv=self.dbcfg['env'][self.rte][db]
		return self.stores[dbenv]['env_refs']
	def get_runtime_env_vars(self):
		return self.dbcfg['env'][self.rte]['env_vars']
	def get_appendix(self):
		scfg, params=self.scfg, self.pa
		columnMappings = scfg["columnMappings"]
		apx_pmap={map['sourceParam']: re.sub('[\'" ]', '', params[map['sourceParamIndex']]) for map in columnMappings if map['value'].encode() == b'Param'}
		apx_cmap={map['columnName']: re.sub('[\'" ]', '', params[map['sourceParamIndex']]) for map in columnMappings if map['value'].encode() == b'Param'}
		sep=str(self.csep.decode())
		apx=sep.join([apx_pmap[map['sourceParam']] if map['value'] == 'Param' else self.asod for map in columnMappings  
						if map['value'] == 'Param' or (map['value'] == 'Default' and map['valueType'] == 'TimeStamp') ] )

		return apx_cmap, apx
	def get_appendix2(self):
		scfg, params=self.scfg, self.pa
		if self.scfg.get('columnMappings', None):
			columnMappings = scfg["columnMappings"]
			apx_pmap={map['sourceParam']: re.sub('[\'" ]', '', params[map['sourceParamIndex']]) for map in columnMappings if map['value'].encode() == b'Param'}
			apx_cmap={map['columnName']: re.sub('[\'" ]', '', params[map['sourceParamIndex']]) for map in columnMappings if map['value'].encode() == b'Param'}
			sep=str(self.csep.decode())
			apx=sep.join([apx_pmap[map['sourceParam']] if map['value'] == 'Param' else self.asod for map in columnMappings  
							if map['value'] == 'Param' or (map['value'] == 'Default' and map['valueType'] == 'TimeStamp') ] )
			apx_cols=[map['columnName'] if map['value'] == 'Param' else map['columnName'] for map in columnMappings  
							if map['value'] == 'Param' or (map['value'] == 'Default' and map['valueType'] == 'TimeStamp') ] 
			return apx_cmap,apx_cols, apx
		else:
			return {}, [], None
		
	def done(self):
		sec=round((time.time() - self.start_time),2)
		log.info('Total elapsed: %s sec/%s min' % (sec, round(sec/60,2)))
	def set_dcfg(self, cname):
		assert self._source
		self.dcfg= self.cfg['dump'][self._source][cname]
	def set_tcfg(self, cname):
		assert self._source
		self.tcfg= self.cfg['target'][self._source][cname]
	def set_scfg(self, cname):
		assert self._source
		self.scfg= self.cfg['source'][self._source][cname]
			
	def get_scfg(self, cname=None):
		if not cname:
			if self._source:
				return self.cfg['source'][self._source]
			else:
				return self.cfg['source']		
		else:
			assert cname
			assert  self._source
			self._src_class = cname
			return self.cfg['source'][self._source][self._src_class]

	def get_dcfg(self, cname=None):
		if not cname:
			if self._source:
				return self.cfg['dump'][self._source]
			else:
				return self.cfg['dump']		
		else:
			assert cname
			assert  self._source
			self._dmp_class = cname
			return self.cfg['dump'][self._source][self._dmp_class]

	def get_tcfg(self, cname=None):
		if not cname:
			if self._source:
				return self.cfg['target'][self._source]
			else:
				return self.cfg['target']		
		else:
			assert cname
			assert  self._source
			self._trg_class = cname
			return self.cfg['target'][self._source][self._trg_class]
			
	def get_sval(self, key):
		scfg=self.scfg
		if self._source:
			return scfg[self._source][key]
		else:
			assert key in scfg.keys(), 'Key "%s" is not in %s' % (key, scfg.keys())
			return scfg[key]

		
	def get_cfg(self, key):

		assert self._source
		class_map={'source':self._src_class, 'dump': self._dmp_class, 'target': self._trg_class}
		#for k,v in class_map.items():
		#		assert v, 'cli.%s config is not set' %k
		
		if self._source:
			return self.cfg[key][self._source][class_map[key]]
		else:
			assert key in self.cfg.keys(), 'Key "%s" is not in %s' % (key, scfg.keys())
			return self.cfg[key]

	def set_target_table(self, tcfg, acct_date, fmt='%Y/%m/%d'):
		#//set acct_year, acct_mon for new target table naming
		if 'accountingDate' in tcfg and 'targetTableFmt' in tcfg:
			assert not tcfg["targetTable"], 'If "targetTable" is set - you cannot  set "accountingDate" and "targetTableFmt"'
			assert acct_date
			self.acct_year = self.get_acct_year(acct_date, fmt)
			self.acct_mon = self.get_acct_mon(acct_date, fmt) 
			assert len(self.acct_year) == 4 
			assert len(self.acct_mon) == 2
			tcfg["targetTable"] = self.get_parsed(ckey='targetTableFmt', cfg=tcfg)
			assert tcfg["targetTable"]
		else:

			assert "targetTable" in tcfg
			assert tcfg["targetTable"] , 'If "targetTable" is not set - you have to set "accountingDate" and "targetTableFmt"'
		

	def get_acct_mon(self, acct_date, fmt):
		assert acct_date
		do = datetime.strptime(acct_date, fmt)
		return str(do.month).zfill(2)
	def get_acct_year(self, acct_date, fmt):
		assert acct_date
		do = datetime.strptime(acct_date, fmt)
		return str(do.year)
	def get_parsed(self, ckey, cfg):
		cli=self

		assert ckey
		assert cfg
		assert ckey in cfg, 'Key "%s" is not in cfg [%s]' % (ckey, cfg.keys())
		val= cfg.get(ckey, None)
		assert val , 'Key [%s] is not set in %s' % (ckey, cfg)
		if isinstance (val, (str, unicode)):
			return val
		else:
			assert isinstance (val, list), 'Key [%s] value [%s] is not a list.' % (ckey, val)
			stmt, pcnt = val
			pars = re.findall("(\{[0-9a-zA-Z_\'\'\.\*\(\)]+\})", stmt)
			fmt={}
			assert len(pars)==pcnt, '[%s]: Number of params in statement (%s) does not match declared params count (%s).' % (ckey, len(pars), pcnt)
			if pars:
				for p in [p.strip('}').strip('{') for p in pars if p not in [ckey]]:
					try:
						assert  p in cfg \
						or p.lower().startswith('cli*')  \
						or p.split('*')[0] in cli.cfg \
						or (p.lower().startswith('optparam_')  and  p.split('_')[1].isdigit()), \
						'[%s]: SQL params should be json section keys or opt/proc param ids (optparam_nnn) or column param names (colparam_xxx) or cli atributes (cli*xxx)' % p
					except:
						pp(cfg)
						pp(stmt)
						pp(p)
						raise
					if p in cfg: 
						
						fmt[p]= self.get_parsed(p, cfg=cfg); continue
					if p.lower().startswith('optparam_'): fmt[p]= cli.pa[int(p.split('_')[1])]; continue
					if p.split('*')[0] in cli.cfg:
						cname, key= p.split('*')
						assert cname
						assert key
						fmt[p]=cli.get_cfg(cname)[key]
						assert fmt[p]
						continue
					if p.lower().startswith('cli*'):
						attr=p.split('*')[1]
						if attr.endswith('()'): #it's a method
							api=attr[:-2]
							assert hasattr(cli, api), 'Cli has no attribute "%s" used in "%s":\n%s' % (api, ckey,stmt)
							fmt[p]=eval('self.%s()' % api)
						else:
							
							assert hasattr(cli, attr), 'Cli has no attribute "%s" used in "%s":\n%s' % (attr, ckey,stmt)
							fmt[p]=getattr(cli, attr)
						continue

				
				stmt = stmt.format(**fmt) 
				
			else:
				pass
			
			return stmt

