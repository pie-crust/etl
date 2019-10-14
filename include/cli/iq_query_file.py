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
from include.fmt import get_formatted
from include.cli.common.Cli import Cli
e=sys.exit

from include.utils import ctimeit
try:
	import cStringIO
except ImportError:
	import io as cStringIO
	
log=logging.getLogger('cli')
		
class iq_query_file(Cli):
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
			
			#self.scfg=scfg=cfg['source']
			#self.tcfg=tcfg=cfg['target']
	
			
		self.proc_key = os.path.basename(self.pcf).split('.')[0]
		#self.sqf_path = self.get_parsed(ckey='sourceQueryFile', cfg=scfg)
		#self.sqf_name = os.path.basename(self.sqf_path)
		if 0:
			self.tdir_path= self.get_parsed(ckey='targetDir', cfg=tcfg)
			if not os.path.isdir(self.tdir_path):
				os.makedirs(self.tdir_path)
			
		if 0: #populate sourceStmt
			stmt=None
			with open(self.sqf_path, 'r') as fh:
				stmt=fh.read().strip()
			assert stmt
			
			self.scfg['sourceStmt'] =[ stmt, 0]
			
		self.max_rows_to_read=10<30
			
		if self.lame_duck and self.lame_duck<self.max_rows_to_read:
			self.max_rows_to_read=self.lame_duck
		assert self.max_rows_to_read
	def exec_config(self):
		self.sqf_path = self.get_parsed(ckey='sourceQueryFile', cfg=self.scfg)
		self.sqf_name = os.path.basename(self.sqf_path)
		if 1:
			self.tdir_path= self.get_parsed(ckey='dumpDir', cfg=self.dcfg)
			if not os.path.isdir(self.tdir_path):
				os.makedirs(self.tdir_path)
			
		if 1: #populate sourceStmt
			stmt=None
			with open(self.sqf_path, 'r') as fh:
				stmt=fh.read().strip()
			assert stmt
			
			self.scfg['sourceStmt'] =[ stmt, 0]
			
	def get_log_stats(self, ll):

		stats={}
		regs=[
		('total_elapsed', 'Cli: Total elapsed: (?P<total_elapsed>[0-9., ]+sec/[0-9., ]+min)'),
		('env', 'Env: \[(?P<env>[A-Z]+)\]'),
		('table',', To-Table:(?P<table>[a-zA-Z_]+)'),
		('schema', ', To-Schema:(?P<schema>[a-zA-Z_\.]+)'),
		('cli_elapsed', 'Cli: Total elapsed: (?P<cli_elapsed>[0-9., ]+sec/[0-9., ]+min)'),
		('sql_ins', 'SQLServer: Inserted:(?P<sql_ins>[0-9,.]+)'),
		]	
		logdata=os.linesep.join(ll)
		for reg in regs:
			group, regexp = reg
			m = re.search(regexp, logdata)
			try:
				stats[group]= m.group(group)
			except:
				stats[group]='n/a'
			
		
		
		#print stats
		headers=['env'] 
		data=[[stats.get(h) for h in headers ]]
		ptitle='IQ'
		
		iq_stats=get_formatted(ptitle,data,headers,join = True)
		print iq_stats


		#print stats
		headers=['env','schema','table', 'sql_ins']
		data=[[stats.get(h) for h in headers ]]
		ptitle='Snowflake'

		snow_stats=get_formatted(ptitle,data,headers,join = True)
		print snow_stats

	
		html_body="""
Parameters provided:	%s<br>
Source:	%s - %s<br>
Target:	%s - %s<br>
Filter:	%s<br>
Started On:	%s<br>
Ended On:	%s<br>
Records Added:	%s<br>
Logs Path:	%s<br>
""" % (	sys.argv, cli.scfg["sourceDb"], cli.pa[0],
		cli.tcfg["targetDb"], cli.pa[2],cli.pa[1],
		cli.asod, time.strftime("%Y-%m-%d %H:%M:%S"),
		stats['sql_ins'], log.file_name)

		return html_body, {'IQ':iq_stats,'SQLServer':snow_stats}


