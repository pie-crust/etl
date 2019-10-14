(cli, conn_pool)=app_init
import os, sys, re, time
import json
from datetime import datetime
import tempfile, traceback
from pprint import pprint as pp


from include.cli.common.Cli import Cli
e=sys.exit
import logging

from include.utils import ctimeit, clierr
from include.fmt import pfmt

try:
	import cStringIO
except ImportError:
	import io as cStringIO
	
	
	
log=logging.getLogger('cli')
		
		
class iq_rest_iq(Cli):
	def __init__(self,*args, **kwargs):
		Cli.__init__(self, *args, **kwargs)

		#self.proc_config()
		log.info('Env: [%s]' % self.rte)
		self.start_time = time.time()
		self.apx=''
		self._rest = self._rest_class= None
	def set_rest(self, key):
		self._rest=key		
	def set_rcfg(self, cname):
		assert self._rest
		self.rcfg= self.cfg['rest'][self._rest][cname]
	def get_rcfg(self, cname=None):
		if not cname:
			if self._rest:
				return self.cfg['rest'][self._rest]
			else:
				return self.cfg['rest']		
		else:
			print (cname)
			assert cname
			assert  self._rest
			self._rest_class = cname
			return self.cfg['rest'][self._rest][self._rest_class]
	def usage(self):
		if 1:
			
			 
			print ('#'*80)
			print ('#'*80)
			print ('#'*80)
			print ("""Usage:
  time python cli.py -nopp 4  -dcf config/db_config.json -pcf config/proc/snow_url_sql/DY_FinancingPosition.json \
 --proc_params  Repo '2018-12-31 00:00:00' "$(date +"%Y-%m-%d %H:%M:%S")"  $GA_TOCKEN
#
# pa[0] = ReferenceType
# pa[1] = AccountingDate
# pa[2] = AsOfDateTime
# pa[3] = gatoken
#

	""")
			print ('#'*80)
			print ('#'*80)
			print ('#'*80)
			e(clierr.E_WRONG_PARAM_COUNT[1])
			
	def get_appendix(self):
		return '', ''		
	@ctimeit
	def proc_config(self):
		pcf=self.pcf
		log.info('Proc conf: %s' % pcf)	
		#pp(self.pa)
		
		self.paramlist = "','".join(self.pa)
		
		with open(pcf, 'r') as f:
		
			
			try:
				self.cfg=cfg = json.loads(f.read())
			except:
				if 1:
					
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
			self.tcfg=tcfg=cfg['target']
			
			self.rcfg=ccfg=cfg['rest']
			
		self.proc_key=os.path.basename(self.pcf).split('.')[0]
		
		self.max_rows_to_read=10<30
			
		if self.lame_duck and self.lame_duck<self.max_rows_to_read:
			self.max_rows_to_read=self.lame_duck
		assert self.max_rows_to_read
	def get_log_stats(self, ll):
		#pp(ll)
		stats={}
 
		regs=[('src_first_row', '\[DbStreamer\] First row elapsed: (?P<src_first_row>[0-9., ]+sec/[0-9., ]+min)'),
		('RefIDs_count','REST: Read:(?P<RefIDs_count>[0-9]+)'),
		('rest_first_row', '\[DataStreamer\] First row elapsed: (?P<rest_first_row>[0-9., ]+sec)'),
		('rest_status','Response received from FICC: (?P<rest_status>[0-9]+)'),
		
		('rest_recs','Records: (?P<rest_recs>[0-9]+)'),
		('snow_del', 'Records deleted: (?P<snow_del>[0-9]+)'),
		('snow_ins', 'Snowflake: Inserted: (?P<snow_ins>[0-9,.]+),'),
		('cli_elapsed', 'Cli: Total elapsed: (?P<cli_elapsed>[0-9., ]+sec/[0-9., ]+min)'),
		('env', 'Env: \[(?P<env>[A-Z]+)\]'),
		('from_table','From-Table:(?P<from_table>[a-zA-Z_]+)'),
		('from_schema', 'From-Schema:(?P<from_schema>[a-zA-Z_\.]+)'),		
		('to_table','To-Table:(?P<to_table>[a-zA-Z_]+)'),
		('to_schema', 'To-Schema:(?P<to_schema>[a-zA-Z_\.]+)')
		]
 
		logdata=os.sep.join(ll)
		for reg in regs:
			group, regexp = reg
			m = re.search(regexp, logdata)
			try:
				stats[group]= m.group(group)
			except:
				stats[group]='n/a'
			
		
		
		#print stats
		headers=['env', 'from_schema','from_table','src_first_row','RefIDs_count']
		data=[[stats.get(h) for h in headers ]]
		ptitle='Ref IDs'
		
		refs_stats=get_formatted(ptitle,data,headers,join = True)
		print refs_stats
		#print stats
		headers=['env', 'rest_first_row','rest_status','rest_recs']
		data=[[stats.get(h) for h in headers ]]
		ptitle='Rest'

		
		rest_stats=get_formatted(ptitle,data,headers,join = True)
		print rest_stats
		#print stats
		headers=['env','to_schema', 'to_table', 'snow_del', 'snow_ins']
		data=[[stats.get(h) for h in headers ]]
		ptitle='Snowflake'

		snow_stats=get_formatted(ptitle,data,headers,join = True)
		print snow_stats
		html_body="""
Parameters provided:	%s<br>
Source:	%s - %s<br>
REST:	%s<br>
Target:	%s - %s<br>
Started On:	%s<br>
Ended On:	%s<br>
Records Added:	%s<br>
Logs Path:	%s<br>
""" % (	sys.argv, cli.scfg["sourceDb"], cli.scfg["sourceTable"],cli.rcfg["sourceUrl"],
		cli.tcfg["targetDb"], cli.tcfg["targetTable"],
		cli.asod, time.strftime("%Y-%m-%d %H:%M:%S"),
		stats['snow_ins'], log.file_name)

		return html_body, {'Ref IDs':refs_stats,'Rest':rest_stats,'Snowflake':snow_stats}
		



