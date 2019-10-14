"""
 time ./_dataMigration.sh --config ./config/DBConfig.json --configKey Daily_FinancingPosition  --params 223906 $(date -d '-3 day' +\%m/\%d/\%Y) $(date -d '-3 day' +\%m/\%d/\%Y) EOD EOD '*' '*' '*' NONE '*' NOW 0
  time python cli.py -dcf config/db_config.json -pcf config/proc/Daily_FinancingPosition.json --proc_params  223906 01/01/2018 01/05/2018 EOD EOD HORZ '*' '*' NONE '*' NOW 0

  
"""
(cli, conn_pool)=app_init
import os, sys, time, imp, math, re, json
import pyodbc, logging
from datetime import datetime
import collections

log=logging.getLogger('cli')
import pandas as pd


try:
    import cStringIO
except ImportError:
    import io as cStringIO
	
from pprint import pprint as pp

e=sys.exit



from include.utils import  ctimeit, api,  clierr

try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
builtins.log=log

from include.Db import Db
from include.loader.common.Loader import Loader

class SQLServer(Db, Loader):
	def __init__(self, **kwargs):
		Db.__init__(self, **kwargs)
		if 0:
			
			KEYTABFILE=self.envars['KRB5_CLIENT_KTNAME']; assert KEYTABFILE

			self.setKeytabCache(KEYTABFILE, self.dbenvars['DB_USER'], None)
			
		self.conn=self.get_connect()
		

	def get_query(self,cfg, qname):
		cli=self.cli
		if 1:
			#cfg=cli.tcfg

			stmt,pcnt=cfg[qname]
			
			
			pars = re.findall("(\{[0-9a-zA-Z_\'\'\*]+\})", stmt)
			fmt={}
			
			assert len(pars)==pcnt, '[%s]: Number of params in statement (%s) does not match declarent params count (%s).' % (qname, len(pars), pcnt)
			
			if pars: # "if match was successful" / "if matched"
				for p in [p.strip('}').strip('{') for p in pars if p not in [qname]]:
					try:
						#print p
						assert  p in cfg or p.lower().startswith('colparam_') or p.lower().startswith('cli*')  or (p.lower().startswith('optparam_')  and  p.split('_')[1].isdigit()), '[%s]: SQL params should be json section keys or opt/proc param ids (optparam_nnn) or column param names (colparam_xxx) or cli atributes (cli_xxx)' % p
					except:
						pp(cfg)
						pp(stmt)
						pp(p)
						raise
					if p in cfg: fmt[p]= cfg.get(p); continue
					if p.lower().startswith('optparam_'): fmt[p]= cli.pa[int(p.split('_')[1])]; continue
					if p.lower().startswith('colparam_'): 
						assert cli.apx_cmap, 'Colparam_* [%s] is used but "apx_cmap" is empty' % p
						fmt[p]= cli.apx_cmap[p.split('_')[1]]; 
						continue
					
					if p.lower().startswith('cli*'):
						attr=p.split('*')[1]
						assert hasattr(cli, attr), 'Cli has no attribute "%s" used in "%s":\n%s' % (attr, qname,stmt)
						fmt[p]=getattr(cli, attr)
						continue
					raise Exception(clierr.E_WRONG_PARAM_FORMAT[0]+': [%s]' % p)
					
			if 1:
				stmt = stmt.format(**fmt) 
				#pp(stmt)
				#pp(fmt)

				#e()
			return stmt

	def get_table_cols(self, tab):
	
		
		stmt='SELECT * FROM %s WHERE 1=2' % tab
		#print 123, stmt
		self.cur.execute(stmt)
		cols=[]
		for id,col in enumerate(self.cur.description):
			cols.append(col[0])
			
		return cols
	def set_conn_str(self,connStr):
		
	
		self.connStr=connStr.format(**self.dbenvars)
		#print self.connStr
		#e()

	@api
	@ctimeit
	def purge_data(self, **kwargs):
		cur=self.cur
		if 1:
			cmd = self.get_query(self.cli.tcfg,'purgeStmt')
			cur.execute(cmd)
			log.info('Records deleted: %s' % cur.rowcount)
	@api
	@ctimeit
	def insert_data(self, **kwargs):
		source=kwargs.get('source')
		skip_header=kwargs.get('skip_header', 0)
		pipe=source.pipe
		skip=str(skip_header).strip()
		if skip_header is not None:
			skip=str(skip_header).strip()
		assert str(skip).strip() in ['0','1'], 'skip_header [%s] should be "0" or "1"' % str(skip).strip()
		if str(skip) == '1':
			pipe.readline()
		assert pipe
		start_time = time.time()
		sql = self.get_query(self.cli.tcfg,'insertStmt')
		
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
		if 0:
			rows=[]

			while line:
				rows.append([line[x] for x in sorted(line.keys())] +[self.cli.pa[1], self.cli.pa[2]])
				line=pipe.readline()
			chunk=10
			total=0
			pp(rows)
			while total<len(rows):
				cur.fast_executemany = True
				#pp(sql)
				#e()
				cur.executemany(sql,  rows[total:][:chunk])
				ins=len(rows[total:][:chunk])
				total +=ins
				log.info('{}: Total:{:,.0f}, Chunk: {:,.0f}'.format (self.cln, total, ins))
			log.info('{}: Read:{:,.0f}, Inserted: {:,.0f},  Skip:{}, Elapsed: {}'.format (self.cln, pipe.rid, len(rows),  skip, round((time.time() - start_time),2)))
			pipe.close()

	@ctimeit
	def insert_array(self, **kwargs):
		indata=kwargs.get('data')
		skip_header=kwargs.get('skip_header', 0)
		data=indata.data
		skip=str(skip_header).strip()
		if skip_header is not None:
			skip=str(skip_header).strip()
		assert str(skip).strip() in ['0','1'], 'skip_header [%s] should be "0" or "1"' % str(skip).strip()
		if str(skip) == '1':
			pipe.readline()
		
		start_time = time.time()
		sql = self.get_query(self.cli.tcfg,'insertStmt')
		self.cur.executemany(sql,  data)
		log.debug('%s: Read:%d, Inserted: %d,  Skip:%s, Elapsed: %s' % (self.cln, len(data), self.cur.rowcount,  skip, round((time.time() - start_time),2)))
	@api
	@ctimeit
	def insert_data_chunk(self,table, data):

		start_time = time.time()
		if data:
			qmarks=('?,' * len(data[0])).strip(',')
			stmt = 'INSERT INTO %s VALUES (%s)' % (table, qmarks)
			pp(stmt)
			#e()
			self.cur.executemany(stmt , data)
			self.conn.commit()
			log.debug('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, len(data), self.cur.rowcount, round((time.time() - start_time),2)))
		else:
			log.warn('Empty data chunk. Passing...')
			
	def bulk_insert(self, trans, file_names, qname, cfg):

		scfg, tcfg = cfg
		skip=scfg['writeHeader']
		assert skip in [0, 1]
		tbl = cli.get_parsed(ckey='targetTable', cfg=tcfg)
		assert tbl
		fnames=file_name.file_names
		start_time = time.time()
		total_ins =0
		for fnamed in file_names.file_names:
			_, fnd = fnamed
			path = fnd['path']
			assert os.path.isfile(path)
			with open(path, 'r') as fh:
				colsep= scfg['columnDelimiter']
				assert colsep
				if skip:
					_ = fh.readline()
				data=[]
				for line in [x.strip()  for x in  fh]:
					#print line
					data.append(line.split(colsep))
				#pp(data)
				#e()
				self.insert_data_chunk(table=tbl, data=data)
				total_ins += len(data)

			break
		log.info('%s: Read:%d, Inserted: %d,  Skip:%s, Elapsed: %s' % (self.cln, total_ins, total_ins,  skip, round((time.time() - start_time),2)))
