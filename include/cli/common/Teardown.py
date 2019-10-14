
import os, sys, re, time, csv 
import json, logging
from datetime import datetime
import traceback
import tempfile
from include.fmt import get_formatted
from pprint import pprint as pp
from include.utils import awscreds 
log=logging.getLogger('cli')
e=sys.exit

from include.utils import ctimeit, clierr


class Teardown(object):
	#@ctimeit
	def __init__(self,*args,**kwargs):

		self.to_file=[]
		self.report={}

	def exec_report(self, db, compare):
		
		for rname, stmt in compare.items():
			if not rname.startswith('_'):
				cur=db.exec_ddl(stmt)
				self.report[rname] = [[x[0] for x in cur.description], list(cur)]
			log.debug('Ignoring report [%s]' % rname)

		#pp(self.report)
		self.extract_report()
	def extract_report(self):
		assert self.report
		#pp(self.tearcfg)
		
		csv_dir= self.get_parsed(ckey='targetCsvDir', cfg=self.tearcfg)
		#print csv_dir
		if not os.path.isdir(csv_dir):
			os.makedirs(csv_dir)
		
		#colsep= str(self.tearcfg['columnDelimiter'])
		
		#linesep=str(self.tearcfg['recordDelimiter'])
		for rname, rdata in self.report.items():
			#print rname
			#pp(rdata)
			#e()
			if rdata[1]:
				to_file = os.path.join (csv_dir, '%s.csv' % rname)
				self.to_file.append(to_file)
				
				log.info(to_file)
				with open(to_file, mode='w') as fh:
					csvw = csv.writer(fh, delimiter = ',', quotechar = '"', lineterminator = '\r\n',  quoting=csv.QUOTE_MINIMAL)

					#for row in rdata:
					csvw.writerow(rdata[0])
				
					csvw.writerows(rdata[1])
				

	@ctimeit
	def get_log_stats(self, ll):
		cli=self
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
		#print iq_stats


		#print stats
		headers=['env','schema','table', 'sql_ins']
		data=[[stats.get(h) for h in headers ]]
		ptitle='SQLServer'

		snow_stats=get_formatted(ptitle,data,headers,join = True)
		#print snow_stats

		#pp(cli.scfg)
		#e()
		html_body="""
Parameters provided:	%s<br>
Sources:	%s <br>
Started On:	%s<br>
Ended On:	%s<br>
Records Added:	%s<br>
Logs Path:	%s<br>
""" % (	sys.argv, cli.tear['source'].keys(), 
		cli.asod, time.strftime("%Y-%m-%d %H:%M:%S"),
		stats['sql_ins'], log.file_name)
		out={}
		for rname, rdata in self.report.items():
			#out[rname] = get_formatted(rname,rdata[1],rdata[0],join = True)
			#print out[rname]
			headers=['env','Source 1','Source 2', 'NumOfDiffs']
			out[rname]=get_formatted(rname,[[cli.rte]+ cli.tear['source'].keys()+[len(rdata[1])]],headers,join = True) 
			print out[rname]


		return html_body, out, self.to_file