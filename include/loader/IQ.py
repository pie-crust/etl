
(cli, conn_pool)=app_init
import os, sys, time, imp, math, re, json
import pyodbc, logging
from datetime import datetime
import collections

log=logging.getLogger('cli')
#import pandas as pd


try:
    import cStringIO
except ImportError:
    import io as cStringIO
	
from pprint import pprint as pp

e=sys.exit



from include.utils import  ctimeit, api,  clierr
from include.fmt import  psql, pfmtd, ppe
try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
builtins.log=log

from include.Db import Db
from include.loader.common.Loader import Loader

class IQ(Db, Loader):
	def __init__(self, **kwargs):
		Db.__init__(self, **kwargs)
		Loader.__init__(self)
		if 0:
			self.conn=self.get_connect()
	def desc_table(self, schema, tbl, col_ord=None):
		stmt = """
SELECT  cname, coltype, nulls, colno, length, in_primary_key as in_pk FROM sys.syscolumns
WHERE  creator='%s' 
       AND tname='%s' 
ORDER  BY %s""" % (schema, tbl, 'cname' if not col_ord else '%s desc' % col_ord)
		#psql(stmt)
		self.cur.execute(stmt)
		out=[]
		rows = {row[1 if col_ord else 0 ]: row for row in self.cur.fetchall()}
		
		for k in sorted(rows.keys()):
			row=rows[k]
			d = collections.OrderedDict()
			for i in zip([col[0] for col in self.cur.description], row):
				x,y = i
				d[x]=y
			out.append(d)
		
		pfmtd(out, '%s.%s' % (schema, tbl))
	def get_columns(self):
		cli=self.cli
		if not self.cur:
			print ('Reopening cursor ', '#'*80)
			self.cur = self.conn.cursor()

			self.cur.execute('SELECT * from %s.%s WHERE 1=2' % (cli.tcfg['targetSchema'],cli.tcfg['targetTable']))

		out={}
		if 1:			
			for id,column in enumerate(self.cur.description):
				out[column[0].encode()]= id
		return out

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

			return stmt

	def get_table_cols(self, schema, tab):
	
		
		stmt='SELECT * FROM %s.%s WHERE 1=2' % (schema, tab)
		
		self.cur.execute(stmt)
		cols=[]
		for id,col in enumerate(self.cur.description):
			cols.append(col[0])
			
		return cols
	def set_conn_str0(self,connStr):
		
	
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
	def bulk_load(self, trans, file_names, qname, cfg, out, header=None):
		#cli=self.cli
		scfg, tcfg = cfg
		skip=scfg['writeHeader']
		assert skip in [0, 1]
		tbl = cli.get_parsed(ckey='targetTable', cfg=tcfg)
		sch = tcfg['targetSchema']
		assert tbl

		fnames=file_names.file_names
		start_time = time.time()
		total_ins =0
		cur= self.conn.cursor()
		cur.execute('SELECT * FROM %s.%s WHERE 1=2' % (sch, tbl))
		from  decimal import Decimal
		#for col in cur.description:
		#	print col[0], col[1],type(col[1]), col[1] == decimal.Decimal, decimal.Decimal
		#e()
		if header:
			clist=',\n '.join([c for c in header])
		else:
			cols = [c[:2] for c in cur.description]
			clist = ',\n '.join([c[0] for c in cur.description])
		
		for path in file_names.file_names:
			#pp(fnamed)
			#_, fnd = fnamed
			#pp(fnd)
			#path = fnd['path']
			assert os.path.isfile(path)
			limit =1000
			rowid=0
			vals=[]
			start_time = time.time()
			
			linesep= scfg['recordDelimiter']
			colsep= scfg['columnDelimiter']
			data=[]
			#print 7777777777777, path
			if 0:
				stmt="""
LOAD TABLE %s.%s (%s)
FROM '%s'
quotes off
escapes off
format ascii

delimited by '%s'
skip %d
row delimited by '%s'
			""" % (sch, tbl,  clist, path, colsep, skip, linesep)
			stmt="""
LOAD TABLE %s.%s (%s)
FROM '%s'
quotes off
escapes off
format ascii

delimited by '%s'
skip %d
			""" % (sch, tbl,  clist, path, colsep, skip)
			
			psql(stmt)
			#e()
			try:
				cnt = cur.execute(stmt)
				
				total_ins +=cur.rowcount
				out[path] = cur.rowcount
			except pyodbc.ProgrammingError as ex:
				log.debug(stmt)
				log.error(ex)
				self.conn.rollback()
				raise
				
			log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))

			self.conn.commit()
			#out[path]=total_ins
			log.info('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, rowid, total_ins, round((time.time() - start_time),2)))
			
	def bulk_load_file(self, trans, file_names, qname, cfg, out, header=None):
		#cli=self.cli
		scfg, tcfg = cfg
		skip=scfg['writeHeader']
		assert skip in [0, 1]
		tbl = cli.get_parsed(ckey='targetTable', cfg=tcfg)
		sch = tcfg['targetSchema']
		assert tbl

		fnames=file_names.file_names
		start_time = time.time()
		total_ins =0
		cur= self.conn.cursor()
		cur.execute('SELECT * FROM %s.%s WHERE 1=2' % (sch, tbl))
		from  decimal import Decimal
		#for col in cur.description:
		#	print col[0], col[1],type(col[1]), col[1] == decimal.Decimal, decimal.Decimal
		#e()
		if header:
			clist=',\n '.join([c for c in header])
		else:
			cols = [c[:2] for c in cur.description]
			clist = ',\n '.join([c[0] for c in cur.description])
		
		for path in file_names.file_names:
			#pp(fnamed)
			#_, fnd = fnamed
			#pp(fnd)
			#path = fnd['path']
			assert os.path.isfile(path)
			limit =1000
			rowid=0
			vals=[]
			start_time = time.time()
			
			linesep= scfg['recordDelimiter']
			colsep= scfg['columnDelimiter']
			data=[]
			#print 7777777777777, path
			if 0:
				stmt="""
LOAD TABLE %s.%s (%s)
FROM '%s'
quotes off
escapes off
format ascii

delimited by '%s'
skip %d
row delimited by '%s'
			""" % (sch, tbl,  clist, path, colsep, skip, linesep)
			stmt="""
LOAD TABLE %s.%s (%s)
FROM '%s'
quotes off
escapes off
format ascii

delimited by '%s'
skip %d
			""" % (sch, tbl,  clist, path, colsep, skip)
			
			psql(stmt)
			#e()
			try:
				cnt = cur.execute(stmt)
				
				total_ins +=cur.rowcount
				out[path] = cur.rowcount
			except pyodbc.ProgrammingError as ex:
				log.debug(stmt)
				log.error(ex)
				self.conn.rollback()
				raise
				
			log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))

			self.conn.commit()
			#out[path]=total_ins
			log.info('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, rowid, total_ins, round((time.time() - start_time),2)))
			

	def bulk_insert(self, trans, file_names, qname, cfg, out):
		#cli=self.cli
		scfg, tcfg = cfg
		skip=scfg['writeHeader']
		assert skip in [0, 1]
		tbl = cli.get_parsed(ckey='targetTable', cfg=tcfg)
		sch = tcfg['targetSchema']
		assert tbl

		fnames=file_names.file_names
		start_time = time.time()
		total_ins =0
		cur= self.conn.cursor()
		cur.execute('SELECT * FROM Position.DY_Position_SD WHERE 1=2')
		from  decimal import Decimal
		#for col in cur.description:
		#	print col[0], col[1],type(col[1]), col[1] == decimal.Decimal, decimal.Decimal
		#e()
		cols=[c[:2] for c in cur.description]

		for fnamed in file_names.file_names:
			_, fnd = fnamed
			path = fnd['path']
			assert os.path.isfile(path)
			limit =1000
			rowid=0
			vals=[]
			start_time = time.time()
			
			linesep= scfg['recordDelimiter']
			colsep= scfg['columnDelimiter']
			data=[]
			with open(path, 'r') as fh:
				
				for line in fh:
					line = line.strip()

					if line:
						if b"'" in line: 
							line=line.strip().replace(b"'",b"''")
						data.append(line)


						v= [("'%s'" % (Decimal(x).quantize(Decimal("0.0000000000001")) if cols[i][1] == Decimal else x)) if x  else 'NULL' for i, x in enumerate(line.split(colsep))]

						vals.append(','.join(v)) 
						rowid +=1
					if len(vals)==limit:
						self.insert_vals(cur, vals, data, sch, tbl, cfg)
						total_ins +=cur.rowcount
						log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))
						vals=[]
						data=[]
					#break
			if vals:
				self.insert_vals(cur, vals, data, sch, tbl,cfg)
				total_ins +=cur.rowcount
				log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))

			self.conn.commit()
			out.inserted_cnt=total_ins
			log.info('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, rowid, total_ins, round((time.time() - start_time),2)))
	def insert_vals(self, cur, vals, data, schema, table, cfg):
		scfg, tcfg = cfg
		for val in vals:
			stmt = 'INSERT INTO %s.%s VALUES (%s)' % (schema, table, val)
			
			try:
				cur.execute(stmt)
			except pyodbc.ProgrammingError as ex:
				log.debug(stmt)
				log.error(ex)
				self.conn.rollback()
				raise
	def insert_bulk_vals(self, cur, vals, data, schema, table, cfg):
		scfg, tcfg = cfg
		
		stmt = 'INSERT INTO %s.%s VALUES (%s)' % (schema, table, '),('.join(vals))	
		log.debug(stmt)
		try:
			cur.execute(stmt)
		except pyodbc.ProgrammingError as ex:
			log.error(ex)
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
		
	@api
	@ctimeit
	def insert_RC_data(self, trans	, target , source, stmt, insert_stats, skip_header=0):
		pipe=source.pipe
		skip=str(skip_header).strip()
		if skip_header is not None:
			skip=str(skip_header).strip()
		assert str(skip).strip() in ['0','1'], 'skip_header [%s] should be "0" or "1"' % str(skip).strip()
		if str(skip) == '1':
			pipe.readline()
		assert pipe

		start_time = time.time()
		xref=self.cli.tcfg["columnMap"]



		cols= [v[0] for _,v in xref.items()] 
		cli.to_cols= ',\n'.join(cols)

		cli.to_quotes = ','.join([x for x in '?'*len(cols)])
		assert cli.to_cols
		sql = self.get_query(target,stmt)
		#cnxn = pyodbc.connect(conn_str, autocommit=True)
		trans.conn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_SERIALIZABLE)
		trans.conn.autocommit = False 
		cur= trans.conn.cursor()
		fline=line=pipe.readline()
		self.rows = rows = []
		#pp(xref)
		apx={x[0]:x[2] for x in xref.values() if len(x)==3}
		apx={x:cli.get_parsed(ckey=x, cfg=apx) for x,v in apx.items()}
		
		#ppe(fline)
		ext_c = list(set(xref.keys())  - set(fline.keys()))
		if ext_c:
			log.warn('Config has extra columns missing in REST')
			#pfmtd([dict(Id=k, DB_ColName=v) for k, v  in enumerate(list(sorted(ext_c)))], 'Defaulting these to nulls')
			
		ext_l = list(set(fline.keys())- set(xref.keys()))
		if ext_l:
			log.warn('REST has extra columns missing in DB')
			#pfmtd([dict(Id=k, RESR_Col=v) for k, v  in enumerate(ext_l)], 'Extra cols in REST')
			#pp(ext_l)
		
		
		ignore=[u'signOffVersion', u'signOffTime', u'RBDate', u'asofDate'] +[u'DataSource', u'GPOSMATTol']+[u'CCY',
 u'DEPolicy',
 u'Price',
 u'UnrealizedPnL',
 u'Fund',
 u'RawUnrealizedPnL',
 u'SwapType'] + [u'SettlementDate']+[u'BuySell',
 u'IndependentAmount',
 u'ConfirmStatus',
 u'RefEntityName',
 u'ReferenceOb',
 u'CounterpartyRefID',
 u'CDSType',
 u'TerminationDateUnadjusted',
 u'TerminationDateAdjusted',
 u'StandardRefObligation',
 u'FixedRate'] + [u'MaturityDate', u'StrikePrice', u'IsSpot'] + [u'Symbol', u'VolatilityStrike']+[u'Direction',
 u'MaturityDateUnadjusted',
 u'TradeCurrency',
 u'ProductType',
 u'UnderlyingSecurity']+[u'MaturityTenor', u'PaymentDate', u'CAP_FLOOR', u'MaturityDateAdjusted'] + \
 [u'IsElectronicallyConfirmed', u'Classification'] + [u'FloatingRateIndex']+[u'IsTodayResetDate']+ \
 [u'FloatRateIndexRec',
 u'IndexTenorRec',
 u'IsOldED',
 u'DayCountFractionPay',
 u'DayCountFractionRec',
 u'PaymentFrequencyPay',
 u'PaymentFrequencyRec',
 u'RollDate']+[u'CCP', u'CCPConfirmRefId'] +[u'IndexTenorPay', u'SpreadPay', u'FloatRateIndexPay']+ \
 [u'TerminationDate', u'FloatingIndex', u'StartFlow', u'CptyRefID'] +[u'Country']+ \
 [u'Barrier1Strike',
 u'Barrier1CCYPair',
 u'bdi',
 u'Barrier2Strike',
 u'Barrier2CCYPair'] + [u'PutCall', u'UnderlyingSymbol', u'OptionStyle']+[u'TerminationDateUnderlyingUnadjusted', u'CallPut', u'PayReceive']+\
 [u'TerminationDateUnderlyingAdjusted']+[u'ProceedsNotional'] +[u'ContractType', u'ExecutingAccount']+[u'SSGClientNote']+[u'Issuer']




		while line:
			line.update(apx)
			ext_s = set(line.keys())- set(xref.keys())
			#pp(ext_s)
			if  ext_s - set(ignore):
				pfmtd([dict(Id=k, REST_Col=v) for k, v  in enumerate(list(ext_s - set(ignore)))], 'Extra cols in REST/IGNORE')
				pp(list( ext_s - set(ignore)))
				ignore = ignore + list(ext_s - set(ignore))
				
			
			
			#rows.append([str(line[x]) if xref[x][1] in ['varchar'] else float(line[x]) if xref[x][1] in ['varchar'] else line[x] for x in xref if x not in ext])
			line=pipe.readline()
		print (123)
		e()
		chunk=3
		total=0
		cid=0
		psql(sql, 'Insert')
		if not rows:
			raise Exception('No data in REST pipe.')
		else:
			
			ignore_cols = target["ignoreSourceColumns"]
			

			if not len(fline)  == len(rows[0]) + len(ignore_cols):
				pp(fline)
				pp(rows[0])
				
				raise Exception ('line %s <> row %s not in xref:%s, not in source:%s' % (len(fline) , len(rows[0]), set(fline.keys()) - set(xref.keys()), set(xref.keys()) - set(fline.keys())))
			
			pfmtd([dict(Col=col, Row=rows[0][i]) for i, col in enumerate([col for col in xref])], 'First row')


		
		while total<len(rows):
			cur.fast_executemany = True
			data = rows[total:][:chunk]
			#ppe(data)
			cur.executemany(sql, data )
			cur.execute("ROLLBACK")
			trans.conn.rollback()
			ins=len(data)
			total +=ins
			cid +=1
			log.info('[{}] [{}] {}: Running: {:,.0f}, Rows: {:,.0f}'.format (self.objtype, cid, self.cln, total, ins))
		
		log.info('[{}]: {}: Inserted: {:,.0f}, To-Schema:{}, To-Table:{}, Skipped: {}, Elapsed: {}'.format (self.objtype, self.cln, len(rows), target['targetSchema'], target["targetTable"] , skip, round((time.time() - start_time),2)))
		pipe.close()
		insert_stats.inserted_cnt = total

	@api
	@ctimeit
	def insert_trans_data(self, trans	, target , source, stmt, skip_header=0):
		pipe=source.pipe
		skip=str(skip_header).strip()
		if skip_header is not None:
			skip=str(skip_header).strip()
		assert str(skip).strip() in ['0','1'], 'skip_header [%s] should be "0" or "1"' % str(skip).strip()
		if str(skip) == '1':
			pipe.readline()
		assert pipe

		start_time = time.time()
		xref=self.cli.tcfg["columnMap"]



		cols= [x for x in xref] 
		cli.to_cols= ',\n'.join(cols)

		cli.to_quotes = ','.join([x for x in '?'*len(cols)])
		assert cli.to_cols
		sql = self.get_query(target,stmt)

		cur= self.conn.cursor()
		line=pipe.readline()
		rows=[]
		while line:
			line.update(dict(AccountingDate=self.cli.pa[1], AsOfDateTime=self.cli.asod))
			rows.append([str(line[xref[x][0]]) if xref[x][1] in ['varchar'] else line[xref[x][0]] for x in xref ])
			line=pipe.readline()
		chunk=300
		total=0
		cid=0
		psql(sql, 'Insert')
		while total<len(rows):
			cur.fast_executemany = True
			data = rows[total:][:chunk]
			cur.executemany(sql, data )
			ins=len(data)
			total +=ins
			cid +=1
			log.info('[{}] [{}] {}: Running: {:,.0f}, Rows: {:,.0f}'.format (self.objtype, cid, self.cln, total, ins))
		
		log.info('[{}]: {}: Inserted: {:,.0f}, To-Schema:{}, To-Table:{}, Skipped: {}, Elapsed: {}'.format (self.objtype, self.cln, len(rows), target['targetSchema'], target["targetTable"] , skip, round((time.time() - start_time),2)))
		pipe.close()