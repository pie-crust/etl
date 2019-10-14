(cli, conn_pool)=app_init
import os, sys, re, time
import json, logging
from datetime import datetime
import tempfile, traceback
from pprint import pprint as pp
from include.fmt import get_formatted
from include.cli.common.db_dir import db_dir
e=sys.exit

from include.utils import ctimeit
try:
	import cStringIO
except ImportError:
	import io as cStringIO

log=logging.getLogger('cli')
		
class iq_proc_dir_lite(db_dir):
	def __init__(self,*args, **kwargs):
		db_dir.__init__(self, *args, **kwargs)
		log.info('ClientId: %s' % self.pa[0])
		log.info('AsOfDate: %s' % self.pa[1])
	@ctimeit
	def db_config0(self):
		dcf=self.dcf
		log.info('Db conf: %s' % dcf)
		with open(dcf, 'r') as f:
			self.dbcfg = json.loads(f.read())
			self.stores = self.dbcfg["stores"]
	@ctimeit
	def get_appendix0(self):
		apx= super(iq_proc_dir_lite, self).get_appendix()
		return apx[0], apx[1]
	@ctimeit
	def proc_config(self):
		super(iq_proc_dir_lite, self).proc_config()
		#self.tcfg=tcfg=self.cfg['target']

		self.proc_key=os.path.basename(self.pcf).split('.')[0]

		log.debug('Starting [%s].' % self.proc_key)
	def usage(self):
		if not self.pa:
			
			print 
			print '#'*80
			print '#'*80
			print '#'*80
			print """Usage:
		

	"""
			print '#'*80
			print '#'*80
			print '#'*80
			e(clierr.E_WRONG_PARAM_COUNT[1])
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
		

	@ctimeit
	def purge(self):
		loader.purge(scfg, cs, '%s.%s' % (sch,tbl), currentTimeStamp, filterForPurge = filterForPurge)



