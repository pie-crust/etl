"""


"""
(home, app_name, log,_)=app_init
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

		
		
class iq_mem_s3_snow(Cli):
	def __init__(self,*args, **kwargs):
		Cli.__init__(self, *args, **kwargs)

		#self.proc_config()
		log.info('Env: [%s]' % self.rte)
		self.start_time = time.time()
		#self.apx_cmap,self.apx=self.get_appendix()
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


	@ctimeit
	def email_init(self):
		if 1:
			lll=open(log.file_name, 'r').read().split(os.linesep)
			
			
			from operator import itemgetter 
			b = [6,]
			
			ll= [' '.join([itemgetter(*b)(x.split('|'))]) for x in lll if x]
			

		if 1:
			ecfg.subject="IQ->Snowflake[%s][%s]." % (proc_key,','.join(pa))
			ecfg.body= '<br>'.join(ll)
	
			send_email(ecfg )
			log.info('Email sent.')			


