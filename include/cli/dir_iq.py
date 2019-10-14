"""


"""
(cli, conn_pool)=app_init
import os, sys, re, time
import json, logging
from datetime import datetime
import tempfile, traceback
from pprint import pprint as pp
from include.fmt import get_formatted
from include.cli.common.Cli import Cli
e=sys.exit

from include.utils import ctimeit
try:
	import cStringIO
except ImportError:
	import io as cStringIO

log=logging.getLogger('cli')
		
class dir_iq(Cli):
	def __init__(self,*args, **kwargs):
		Cli.__init__(self, *args, **kwargs)
		#self.proc_config()
		log.info('Env: [%s]' % self.rte)
		self.start_time = time.time()
	@ctimeit
	def db_config(self):
		dcf=self.dcf
		log.info('Db conf: %s' % dcf)
		with open(dcf, 'r') as f:
			self.dbcfg = json.loads(f.read())
			self.stores = self.dbcfg["stores"]

	@ctimeit
	def proc_config(self):
		pcf=self.pcf
		#log.info('Proc conf: %s' % pcf)		
		with open(pcf, 'r') as f:
			try:
				self.cfg = cfg = json.loads(f.read())
			except Exception:
				log.error('Cannot parse proc JSON [%s]' % pcf)
				raise
			#self.scfg=cfg['source']
			#self.tcfg={} #tcfg=cfg['target']
			
			


			
			
		#self.proc =  scfg['procName']

		self.paramlist = "','".join(self.pa)

		self.proc_key=os.path.basename(self.pcf).split('.')[0]

		if 1:
			self.tab_root	= self.get_tab_root()
			#self.db	= self.pa[1]
		assert os.path.isdir(self.tab_root),  'Dir [%s] doet not exists.' % self.tab_root
		#check if table exists

		
		log.debug('Starting [%s].' % self.proc_key)
	def get_tab_root(self):
		return self.pa[0]
	@ctimeit
	def get_purge_filter(self):
		
		cmaps = self.scfg["columnMappings"]
		ins={map['sourceParam']: re.sub('[\'" ]', '', self.pa[map['sourceParamIndex']]) for map in cmaps if map['value'] == b'Param'}
		pfilter=''
		for map in cmaps:
			if map['value'] == 'Param':
				
				pfilter += " AND {} = '{}'".format(map['columnName'], ins[map['sourceParam']])
				
		log.debug('Purge filter: [%s]' % pfilter)
		return pfilter		
		

			
	def loop(self):
		pass
	
	@ctimeit
	def purge(self):
		loader.purge(scfg, cs, '%s.%s' % (sch,tbl), currentTimeStamp, filterForPurge = filterForPurge)

	def get_appendix(self):
		return None, None


	def get_log_stats(self, ll, stats):

		stats={}
		regs=[('first_row', 'First row elapsed: (?P<first_row>[0-9., ]+sec/[0-9., ]+min)'),
		('s3_loaded','S3: Loaded:(?P<s3_loaded>[0-9,]+), '),
		('s3_read','S3: Loaded:[0-9,]+, Read:(?P<s3_read>[0-9,]+), '),
		('s3_raw','S3: Total:(?P<s3_raw>[0-9., A-Z]+),'),
		('snow_del', 'Records deleted: (?P<snow_del>[0-9]+)'),
		('snow_ins', 'Snowflake: Inserted:(?P<snow_ins>[0-9,.]+),'),
		('s3_files', ', Files:(?P<s3_files>[0-9]+)'),
		('s3_compressed','Compressed \(gz\)\:(?P<s3_compressed>[0-9., A-Z]+)'),
		('total_elapsed', 'Cli: Total elapsed: (?P<total_elapsed>[0-9., ]+sec/[0-9., ]+min)'),
		('env', 'Env: \[(?P<env>[A-Z]+)\]'),
		('table',', To-Table:(?P<table>[a-zA-Z_]+)'),
		('schema', ', To-Schema:(?P<schema>[a-zA-Z_\.]+)'),
		('cli_elapsed', 'Cli: Total elapsed: (?P<cli_elapsed>[0-9., ]+sec/[0-9., ]+min)'),
		('proc','Procedure: [a-zA-Z]+\.(?P<proc>[0-9a-zA-Z]+_WRAPPER) '),
		('client','ClientId: (?P<client>[0-9]+)'),
		('asof_dt','AsOfDate: (?P<asof_dt>[0-9/]+)')]
		logdata=os.linesep.join(ll)
		for reg in regs:
			group, regexp = reg
			m = re.search(regexp, logdata)
			try:
				stats[group]= m.group(group)
			except:
				stats[group]='n/a'
			
		
		
		#print stats
		headers=['env', 'proc', 'client','asof_dt', 'first_row'] #,'s3_files','s3_read','s3_loaded','s3_raw','s3_compressed','snow_del', 'snow_ins','total_elapsed']
		data=[[stats.get(h) for h in headers ]]
		ptitle='IQ'
		
		iq_stats=get_formatted(ptitle,data,headers,join = True)
		print iq_stats
		#print stats
		headers=['env','s3_files','s3_read','s3_loaded','s3_raw','s3_compressed']
		data=[[stats.get(h) for h in headers ]]
		ptitle='S3'

		
		s3_stats=get_formatted(ptitle,data,headers,join = True)
		print s3_stats
		#print stats
		headers=['env','schema','table', 'snow_del', 'snow_ins']
		data=[[stats.get(h) for h in headers ]]
		ptitle='Snowflake'

		snow_stats=get_formatted(ptitle,data,headers,join = True)
		print snow_stats

	
		html_body="""
Parameters provided:	%s<br>
Source:Dir - %s<br>
Target:	%s - %s<br>
Started On:	%s<br>
Ended On:	%s<br>
Records Added:	%s<br>
Logs Path:	%s<br>
""" % (	sys.argv,  cli.tcfg["targetDb"],
		cli.tcfg["targetDb"], cli.tcfg["targetTable"],
		cli.asod, time.strftime("%Y-%m-%d %H:%M:%S"),
		stats['snow_ins'], log.file_name)

		return html_body, {'IQ':iq_stats,'S3':s3_stats,'Snowflake':snow_stats}
