"""
 time ./_dataMigration.sh --config ./config/DBConfig.json --configKey Daily_FinancingPosition  --params 223906 $(date -d '-3 day' +\%m/\%d/\%Y) $(date -d '-3 day' +\%m/\%d/\%Y) EOD EOD '*' '*' '*' NONE '*' NOW 0
  time python cli.py -dcf config/db_config.json -pcf config/proc/Daily_FinancingPosition.json --proc_params  223906 01/01/2018 01/05/2018 EOD EOD HORZ '*' '*' NONE '*' NOW 0

  
"""
(cli, conn_pool)=app_init
import os, sys, time, imp, math, re, json
import pyodbc
import datetime
import collections
#from include.PubSub import PubSub

import pandas as pd
import logging
log=logging.getLogger('cli')

try:
    import cStringIO
except ImportError:
    import io as cStringIO
	
from pprint import pprint as pp

e=sys.exit



from include.utils import timeit, ctimeit, csource

try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=(cli, conn_pool)
builtins.log=log
from include.Db import Db



from include.extractor.common.StreamSlicer import StreamSlicer
from include.extractor.common.FileStreamer import FileStreamer
from include.extractor.common.DbStreamer import DbStreamer

from include.extractor.common.Extractor import Extractor






class SQLServer(Extractor,Db):
	#@csource 
	def __init__(self, **kwargs):
		Db.__init__(self, **kwargs)
		self.apx= self.cli.apx

		self.conn=self.get_connect()
		#pp(self.connStr)
		#e()


	@ctimeit
	def dump_stream(self, _in):
		data=_in.pipe.read()
		print('dump_stream: ',len(data))


	def parse_conn_str(self,connStr):
		self.connStr=connStr.format(DB_READ_SERVER,DB_READ_USER,DB_READ_PWD)

	@ctimeit
	#@csource 
	def open_stream(self,dbcfg, qname, out):
		global actors
		cli=self.cli

		from_cols={}
		for id, col in enumerate(cli.scfg["columnMappings"]):
			if col['value'].upper() in [u'Map'.upper(), u'Param'.upper(),u'Default'.upper()]:
				from_cols[int(id)]=col['columnName'].upper().encode()

		to_cols= self.loader.get_columns()
		assert to_cols
		#pp(to_cols)
		#e()
		assert len(from_cols) == len(to_cols), 'Config vs Target column count mismatch (%d != %d)' % (len(from_cols),len(to_cols))
		miss=0
		for id, col in from_cols.items():
			#print (col, to_cols.keys())
			assert col in to_cols, 'Config column "%s" does not exists in Target table "%s"' % (col, cli.tcfg['targetTable'])
			if not int(id)==int(to_cols[col]):
				print ('Config column "%s" order is wrong (Config# %d != Target# %d)' % (col, id, to_cols[col]))
				miss +=1
		assert miss == 0
		col_map=None
		#Out = collections.namedtuple('Out','pipe actor col_map')
		cli=self.cli
		apx=self.apx
		mock_file=cli.mf
		assert self.conn
		stmt=self.get_query(dbcfg,qname)
		#pp(stmt)
		#e()
		assert stmt
		from collections import OrderedDict
		from_cols=OrderedDict()	
		if 1:
			if mock_file:			
				log.info('%s: Using mock file: %s' % (self.cln,mock_file))
				assert os.path.isfile(mock_file)
				import codecs
				mfh = codecs.open(mock_file, encoding='latin-1')

				#mfh=open(mock_file,'rb')
				if 1:

					header=mfh.readline().strip().split(str(self.cli.csep.decode()))

					for id,column in enumerate(header):
						from_cols[id]=column.encode().upper()
					#pp(from_cols)
					#e()
					col_map=self.get_col_map(from_cols, to_cols)
					
				pipe=FileStreamer(self.cli,fh=mfh)

			else:
				
				pyodbc.pooling = False
				

				cur= self.conn.cursor()
				start_time = time.time()
				if 1:
					
					cur.execute(stmt)


					for id,column in enumerate(cur.description):
						from_cols[id]=column[0].upper().encode()
					#print from_cols
					
					col_map=self.get_col_map(from_cols,to_cols)
					pipe=DbStreamer(self.cli,cur=cur, start_time=start_time)
		
			
		with StreamSlicer(cli, pipe, apx, max_rows_to_read=self.cli.max_rows_to_read, col_map=col_map) as pipe:
			out.pipe, out.actor, out.col_map = pipe, self.cln,col_map
			return out
			

	def get_col_map(self, from_cols, to_cols):
		col_map={}

		conf_cols={}
		alt_cols={}
		pcnt=0
		for id, col in enumerate(self.cli.scfg["columnMappings"]):
			if col['value'].upper() in [u'Map'.upper(), u'Param'.upper(),u'Default'.upper()]:
				if col['value'].upper() not in  [u'Map'.upper()]:
					pcnt +=1
					
				conf_cols[int(id)]=col['columnName'].upper().encode()
				if col.get('altColName'):
					alt_cols[int(id)]=col.get('altColName').upper().encode()
	

		assert len(conf_cols) - pcnt == len(from_cols), 'Source vs Config column count mismatch (%d != %d). (%d are params)\n Are you sure you have header in your MOCK file?' % (len(from_cols), len(conf_cols), pcnt)
		if 1:
			miss=0
			if 0:
				pp(dict(from_cols))
				pp(conf_cols)
				pp(alt_cols)

				#e()
			for id, col in from_cols.items():
				
				if col not in conf_cols.values():
					if col not in alt_cols.values():
						#print id, col, col in alt_cols.values()
						print ('Column "%s"  is NOT in config' % (col,))
						miss +=1
					else:
						print ('Column "%s"  is IN ALT config [%s]' % (col,conf_cols[id]))
						col_map[to_cols[conf_cols[id]]]=id
				else:
					#print 'Column "%s"  is  IN config' % (col,)
					col_map[to_cols[col]]=id
					
			assert miss==0, '[%d] Source columns are not in Config.' % miss 
		sep=str(self.cli.csep.decode())
		apx_len=len(self.apx.split(sep)) if self.apx.split(sep) and self.apx.split(sep)[0] else 0
		#print apx_len, repr(self.apx), sep, self.apx.split(sep)
		#e()
		if apx_len and self.apx.split(sep)[0]:
			log.debug('Increase colmap by apx len [%d]' % apx_len)
			map_len=len(col_map)
			for x in range(map_len,map_len+apx_len):
				col_map[x]=x
			#pp(col_map)
		else:
			print ('APx is empty [%d]' % apx_len)
		#print(len(col_map), apx_len, map_len, self.apx)
		#e()
		return col_map
	def get_connect1(self):	
		conn_key='%s.%s.%s' % (self.cln,self.dbenvars['DB_SERVER'],self.dbenvars['DB_USER'])	
		cli=self.cli
		dbenv=cli.dbcfg['env'][cli.rte][self.cln]
		assert dbenv
		self.set_conn_str(cli.stores[dbenv]['connectionString'])
		#e()
		if conn_key in self.cpool.keys():
			log.debug('%s: Reusing connect.' % self.cln)
			return self.cpool[conn_key]
		else:
			log.debug('%s: New connect.' % self.cln)
			conn=self.cpool[conn_key]= self._connect()
			return conn



			
	def set_conn_str(self,connStr):
		
	
		self.connStr=connStr.format(**self.dbenvars)
		#print self.connStr
		#e()


	@timeit
	def purge_data(self, **kwargs):
		cur=self.cur
		if 1:
			cmd = self.get_query(self.cli.tcfg,'purgeStmt')
			cur.execute(cmd)
			log.info('Records deleted: %s' % cur.rowcount)

	@timeit
	def insert_data(self, **kwargs):
		_in=kwargs.get('_in')
		skip_header=kwargs.get('skip_header')
		pipe=_in.pipe
		skip=str(skip_header).strip()
		if skip_header is not None:
			skip=str(skip_header).strip()
		assert str(skip).strip() in ['0','1'], 'skip_header [%s] should be "0" or "1"' % str(skip).strip()
		if str(skip) == '1':
			pipe.readline()
		assert pipe
		start_time = time.time()
		sql = self.get_query('insertStmt')
		
		cur= self.conn.cursor()
		line=pipe.readline()
		#pp(line)
		i=0

		while line:
			row =[line[x] for x in sorted(line.keys())] +[self.cli.pa[1], self.cli.pa[2]]

			cur.executemany(sql,  [row])
			i +=1
			line=pipe.readline()

		log.info('%s: Read:%d, Inserted: %d,  Skip:%s, Elapsed: %s' % (self.cln, pipe.rid, i,  skip, round((time.time() - start_time),2)))
		pipe.close()

		