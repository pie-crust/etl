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
from include.fmt import psql
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
		self.conn=self.get_connect(env=self.cln)

	def get_query(self,cfg, qname):
		cli=self.cli

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
			#pp(rows)
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
		

		#e()
		start_time = time.time()
		if data:

			if 1:
				#self.cur.fast_executemany = True
				
				start=0 
				limit =1000
				vals=[]
				stmt=''
				while start<len(data):
					
					for row in data[start:][:limit]:
						vals.append(','.join(["'%s'" % x if x else 'NULL' for x in row])) 
						#pp(vals)
					log.debug('Start: %d, limit: %d ' % (start, limit))
					assert vals
					stmt = 'INSERT INTO %s VALUES (%s)' % (table, '),('.join(vals))

					self.cur.execute(stmt)
					vals=[]
					
					
					start +=limit
				self.conn.commit()


			log.debug('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, len(data), self.cur.rowcount, round((time.time() - start_time),2)))
		else:
			log.warn('Empty data chunk. Passing...')
			
	def bulk_insert(self, trans, file_names, qname, cfg, out):
		#cli=self.cli
		scfg, tcfg = cfg
		skip=scfg['writeHeader']
		assert skip in [0, 1]
		tbl = cli.get_parsed(ckey='targetTable', cfg=tcfg)
		assert tbl

		fnames=file_names.file_names
		start_time = time.time()
		total_ins =0
		cur= self.conn.cursor()
		for path in file_names.file_names:
			#_, fnd = fnamed
			#path = fnd['path']
			assert os.path.isfile(path)
			limit =1000
			rowid=0
			vals=[]
			start_time = time.time()
			
			linesep= scfg['recordDelimiter']
			colsep= scfg['columnDelimiter']
			data=[]
			with open(path, 'r') as fh:
				if skip:
					for x in range(skip):
						fh.readline()
				for line in fh:
					line = line.strip()

					if line:
						if b"'" in line: 
							line=line.strip().replace(b"'",b"''")
						data.append(line)

						vals.append(','.join(["'%s'" % x if x else 'NULL' for x in line.split(colsep)])) 
						rowid +=1
					if len(vals)==limit:
						self.insert_vals(cur, vals, data, tbl, cfg)
						total_ins +=cur.rowcount
						log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))
						vals=[]
						data=[]
			if vals:
				self.insert_vals(cur, vals, data, tbl,cfg)
				total_ins +=cur.rowcount
				log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))

			self.conn.commit()
			out.inserted_cnt=total_ins
			log.info('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, rowid, total_ins, round((time.time() - start_time),2)))
	def insert_vals(self, cur, vals, data, table, cfg):
		scfg, tcfg = cfg
		stmt = 'INSERT INTO %s VALUES (%s)' % (table, '),\n('.join(vals))	
		#psql(stmt)
		try:
			cur.execute(stmt)
		except pyodbc.ProgrammingError, err:
			log.error(err)
			self.conn.rollback()
			raise



	def insert_data(self, cur, data, table, cfg):
		scfg, tcfg = cfg
		log.debug('Retrying same set with re.escape')
		vals=[]
		colsep= scfg['columnDelimiter']
		for line in data:
			if b"'" in line: 
				line=line.strip().replace(b"'",b"''")
			vals.append(','.join(["'%s'" % x if x else 'NULL' for x in line.split(colsep)])) 
		
		stmt = 'INSERT INTO %s VALUES (%s)' % (table, '),('.join(vals))	
		#pp(stmt)
		cur.execute(stmt)
		log.debug('[Retry] Inserted: %d ' % (len(vals)))

		