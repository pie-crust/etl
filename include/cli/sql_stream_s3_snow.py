(cli, conn_pool)=app_init
import os, sys, re, time
import json, logging
from datetime import datetime
import tempfile, traceback
from pprint import pprint as pp
from include.fmt import get_formatted
from include.cli.common.Cli import Cli
e=sys.exit
log=logging.getLogger('cli')
from include.utils import ctimeit
try:
	import cStringIO
except ImportError:
	import io as cStringIO

		
		
class sql_stream_s3_snow(Cli):
	def __init__(self,*args, **kwargs):
		Cli.__init__(self, *args, **kwargs)
		log.info('ClientId: %s' % self.pa[0])
		log.info('AsOfDate: %s' % self.pa[1])
		#self.proc_config()
		log.info('Env: [%s]' % self.rte)
		self.start_time = time.time()
		#self.apx_cmap,self.apx=self.get_appendix()
	@ctimeit
	def db_config(self):
		dcf=self.dcf
		log.info('Db conf: %s' % dcf)
		try:
			with open(dcf, 'r') as f:
				self.dbcfg = json.loads(f.read())
				self.stores = self.dbcfg["stores"]
		except Exception, ex:
			log.error(str(ex))
			raise
	@ctimeit
	def proc_config(self):
		pcf=self.pcf
		log.info('Proc conf: %s' % pcf)		
		with open(pcf, 'r') as f:
			cfg = json.loads(f.read())
			self.scfg=scfg=cfg['source']
			self.tcfg=tcfg=cfg['target']
			self.s3cfg=s3cfg=cfg['s3']
			#self.ccfg=ccfg=cfg['cli']
			
		self.proc =  scfg['procName']

		self.paramlist = "','".join(self.pa)

		self.to_dir=s3cfg['targetDir']
		self.proc_key=os.path.basename(self.pcf).split('.')[0]

		log.info("Procedure: %s '%s'" % (self.proc, "','".join(self.pa)))
		if not int(s3cfg["maxRecordsInFile"])>= int(s3cfg["writeBufferSize"]):
			s3cfg["writeBufferSize"]=s3cfg["maxRecordsInFile"]
		if 1:
			###############
			self.max_rows_to_read=int(s3cfg["maxRecordsInFile"])
			#self.max_rows_to_read=65000
			###############
			if self.lame_duck and self.lame_duck<self.max_rows_to_read:
				self.max_rows_to_read=self.lame_duck
		assert self.max_rows_to_read

		log.debug('Starting [%s].' % self.proc_key)

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




	def get_log_stats(self, ll):

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
		#pp(ll)
		logdata=os.linesep.join(ll)
		#pp(logdata)
		for reg in regs:
			group, regexp = reg
			m = re.search(regexp, logdata)
			try:
				stats[group]= m.group(group)
			except:
				stats[group]='n/a'
			
		
		
		#print stats
		headers=['env', 'proc', 'client','asof_dt', 'first_row'] 
		data=[[stats.get(h) for h in headers ]]
		ptitle='SQLServer'
		
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
		ptitle='SnowFlake'

		snow_stats=get_formatted(ptitle,data,headers,join = True)
		print snow_stats
		if 0:
			#print stats
			headers=['cli_elapsed']
			data=[[stats.get(h) for h in headers ]]
			ptitle='Cli'

			cli_stats=get_formatted(ptitle,data,headers,join = True)
	
	
		return iq_stats,s3_stats,snow_stats
