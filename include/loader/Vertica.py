"""
 time ./_dataMigration.sh --config ./config/DBConfig.json --configKey Daily_FinancingPosition  --params 223906 $(date -d '-3 day' +\%m/\%d/\%Y) $(date -d '-3 day' +\%m/\%d/\%Y) EOD EOD '*' '*' '*' NONE '*' NOW 0
  time python cli.py -dcf config/db_config.json -pcf config/proc/Daily_FinancingPosition.json --proc_params  223906 01/01/2018 01/05/2018 EOD EOD HORZ '*' '*' NONE '*' NOW 0

  
"""
(cli, conn_pool)=app_init
import os, sys, time, imp, math, re, json
import pyodbc, logging
from datetime import datetime
import collections
import binascii
from collections import OrderedDict

log=logging.getLogger('cli')



try:
    import cStringIO
except ImportError:
    import io as cStringIO
	
from pprint import pprint as pp

e=sys.exit



from include.utils import  ctimeit, api,  clierr
from include.fmt import  psql, pfmtd,  pfmt

try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
builtins.log=log

from include.Db import Db
from include.loader.common.Loader import Loader
from include.fmt import get_formatted


class Vertica(Db, Loader):
	def __init__(self, **kwargs):
		Db.__init__(self, **kwargs)
		if 0:
			self.conn=self.get_connect(env=self.cln)

		
	def _get_columns(self):
		cli=self.cli
		if not self.cur:
			print ('Reopening cursor ', '#'*80)
			self.cur = self.conn.cursor()

		
		self.cur.execute('SELECT * from %s.%s LIMIT 0' % (cli.tcfg['targetSchema'],cli.tcfg['targetTable']))
		#from collections import OrderedDict
		out={}
		if 1:			
			for id,column in enumerate(self.cur.description):
				out[column[0]]= id
		return out
		
	def get_create_col_list(self, cols, apx =[]):
		return ', \n'.join(['%s %s null' % (col[0], 'DOUBLE PRECISION' if col[1] =='double' else col[1]) for  col in cols+apx])
		
	def get_columns(self, table):
		cli=self.cli
		if not self.cur:
			self.cur = self.conn.cursor()

		
		self.cur.execute('SELECT * from %s LIMIT 0' % table)
		#from collections import OrderedDict
		out={}
		if 1:			
			for id,column in enumerate(self.cur.description):
				out[id]= column[0]
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
	def desc_table(self, schema, tbl, col_ord=None):
		stmt = """
SELECT  ordinal_position as id, column_name, data_type,
data_type_length as dt_len, is_nullable as nullable, column_default as default
FROM   v_catalog.columns 
WHERE  table_schema='%s' 
       AND table_name='%s' 
ORDER  BY %s""" % (schema, tbl, 'ordinal_position' if not col_ord else '%s desc' % col_ord)
		self.cur.execute(stmt)
		#psql(stmt)
		out=[]
		rows = {row[0 if col_ord else 1 ]: row for row in self.cur.fetchall()}
		
		for k in sorted(rows.keys()):
			row=rows[k]
			d = OrderedDict()
			for i in zip([col[0] for col in self.cur.description], row):
				x,y = i
				d[x]=y
			out.append(d)
		
		pfmtd(out, '%s.%s' % (schema, tbl))
	def get_col_types(self, schema, tbl):
		stmt = """
SELECT  column_name, data_type
FROM   v_catalog.columns 
WHERE  table_schema='%s' 
       AND table_name='%s' 
ORDER  BY ordinal_position""" % (schema, tbl)
		self.cur.execute(stmt)
		psql(stmt)
		out=[]

		return self.cur.fetchall()
		
		
	def desc_tmp_table(self, tbl, cols):
		
		d= {col[0]:col for col in cols}
		
		pfmtd([dict(Column=d[k][0], Data_type=d[k][1]) for k in sorted(d.keys())], tbl)
		
	def get_table_cols(self, tab):
	
		
		stmt='SELECT * FROM %s WHERE 1=2' % tab
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
		start_time = time.time()
		if data:
			if 1:
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
	def bulk_load(self, trans, file_names, qname, cfg, out):
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
		cols = [c[:2] for c in cur.description]
		clist = ','.join([c[0] for c in cur.description])
		pp(file_names.file_names)
		for path in file_names.file_names:

			assert os.path.isfile(path)
			limit =1000
			rowid=0
			vals=[]
			start_time = time.time()
			
			linesep= scfg['recordDelimiter']
			colsep= scfg['columnDelimiter']
			data=[]
			#print 7777777777777, path
			

			stmt="""
LOAD TABLE %s.%s (%s)
FROM '%s'
quotes off
escapes off
format ascii
delimited by '%s' NULL ''
row delimited by '%s'
			""" % (sch, tbl,  clist, path, colsep, linesep)
			#print stmt
			#e()
			try:
				cnt = cur.execute(stmt)
				
				total_ins +=cur.rowcount
			except pyodbc.ProgrammingError as ex:
				log.debug(stmt)
				log.error(ex)
				self.conn.rollback()
				raise
				
			log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))

			self.conn.commit()
			out.inserted_cnt=total_ins
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
			with open(path, 'rb') as fh:
				
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


	def insert_data(self, trans,  table, data,cfg):
		scfg, tcfg = cfg
		if data:
			conn, cur = trans.conn, trans.cur
			
			vals=[]
			colsep= scfg['columnDelimiter']
			for line in data:
				#print line
				#if b"'" in line: 
				#	line=line.strip().replace(b"'",b"''")
				vals.append(','.join(["'%s'" % x if x else 'NULL' for x in line])) 
			
			stmt = 'INSERT INTO %s VALUES (%s)' % (table, '),('.join(vals))	
			pp(stmt)
			#e()
			cur.execute(stmt)
			log.debug('[Retry] Inserted: %d ' % (len(vals)))
	def insert_data_byrow(self, trans,  table, data, cfg, file_cols):
		scfg, tcfg = cfg
		if data:
			conn, cur = trans.conn, trans.cur
			
			vals=[]
			colsep= scfg['columnDelimiter']
			for line in data:
				row=','.join(["'%s'" % x if x else 'NULL' for x in line])
				vals.append(line) 
				cols = ','.join([col[0] for col in file_cols])
				if table in ['Tx']:
					if [col[0] for col in file_cols][1] in [u'TxMasterGUID']:
						line[1]='test'
						row=','.join(["'%s'" % x if x else 'NULL' for x in line])
					pp([col[0] for col in file_cols])
					if [col[0] for col in file_cols][21] in [u'SwapEventGUID']:
						line[21]=0
						row=','.join(["'%s'" % x if x else 'NULL' for x in line])
						
				stmt = 'INSERT INTO %s (%s) VALUES (%s)' % (table, cols,row)	
				pp(stmt)
				#e()
				cur.execute(stmt)
			log.debug('[Retry] Inserted: %d ' % (len(vals)))
	def q_insert_data(self,trans, table, data):
		if data:
			conn, cur = trans.conn, trans.cur
			qmarks=('?,' * len(data[0])).strip(',')
			print ('INSERT INTO %s VALUES (%s)' % (table, qmarks))
			
			self.cur.executemany('INSERT INTO %s VALUES (%s)' % (table, qmarks), data)
			self.conn.commit()
		else:
			log.warn('Empty data set. Passing...')
			
	@api
	@ctimeit
	def load_file_0( self, trans, file_obj, table_name, qname, cfg, create_table=False):

		scfg, tcfg = cfg
		file_name = file_obj.file_name
		pp(file_obj.cols)
		
		if 1:
			assert os.path.isfile(file_name)
			with open(file_name, 'r') as fh:
				colsep= scfg['columnDelimiter']
				assert colsep
				if create_table:
					self.create_table( fh, cfg, table_name)
				else:
					fh.readline()
					fh.readline()
				data=[]
				for line in [x.strip()  for x in  fh]:
					#print line
					data.append(line.split(colsep)[:-1])
				self.insert_data_byrow(trans, table_name, data, cfg, file_obj.cols)
	@api
	@ctimeit
	def __load_file_2( self, trans, file_obj, table_name, qname, cfg, create_table=False):

		scfg, tcfg = cfg
		file_name = file_obj.file_name
		#pp(file_obj.cols)
		fmt_cols=['TxMasterGUID', 'SwapEventGUID']
		if 1:
			assert os.path.isfile(file_name)
			with open(file_name, 'r') as fh:
				colsep= scfg['columnDelimiter']
				assert colsep
				if create_table:
					self.create_table( fh, cfg, table_name)
				else:
					fh.readline()
					fh.readline()
				data=[]
				intdata=[[]]
				intcols=[]
				for line in [x.strip()  for x in  fh]:

					data.append([x if x else None for i, x in enumerate(line.split(colsep)[:-1])])


				if 1:
					cols = ','.join([col[0] for col in file_obj.cols])
					assert len(file_obj.cols) == len(data[0])

					if 0:
						tmpTbl = 'tmp_%s' % table_name
						stmt='CREATE LOCAL TEMPORARY TABLE %s AS SELECT * FROM %s WHERE 1=2' % (tmpTbl,table_name);
						#print(stmt)
						trans.cur.execute(stmt)
						#e()
					assert len(intdata[0]) == len(intcols)

					trans.conn.autocommit = False
					if 0:
						stmt = "COPY %s FROM LOCAL '/home/s_dev_rdm/ab_gtx/iris.csv' DELIMITER '|'" % tmpTbl
					
					copyfmt=',\n'.join(["%s FORMAT 'hex'" % col[0] if col[0] in fmt_cols else "%s" % col[0]  for col in file_obj.cols])
					stmt="COPY %s (%s) FROM LOCAL'/home/s_dev_rdm/ab_gtx/iris.csv' DELIMITER '|'"  % (table_name, copyfmt)
					trans.cur.execute(stmt)
					pfmt(trans.cur.execute('SELECT GET_NUM_ACCEPTED_ROWS(),GET_NUM_REJECTED_ROWS()').fetchall(), ['Accepted','Rejected'], 'Load stats')

					if fmt_cols:
						
						show=[]
						for row in  trans.cur.execute('select TO_HEX(%s) from %s LIMIT 5' % ('), TO_HEX('.join(fmt_cols), table_name)).fetchall():
							show.append( row)
							#print binascii.hexlify(row[0])
						pfmt(show, fmt_cols, 'Sample')
					#trans.conn.commit()
	@api
	@ctimeit
	def load_gtx_file( self, trans, file_obj, schema, table_name, qname, fmt_cols, cfg, skip=0, apx = None, stats=None):

		scfg, tcfg = cfg
		file_name = file_obj.file_name
		
		
		
		

		assert os.path.isfile(file_name)
		if 1:
			colsep= scfg['columnDelimiter']
			assert colsep

			lcnt = file_obj.line_count(file_name)
			

			if 1:
				cols = ','.join([col[0] for col in file_obj.cols])

				trans.conn.autocommit = False

				copyfmt=',\n'.join(["%s FORMAT 'hex'" % col[0] if col[0] in fmt_cols else "%s" % col[0]  for col in file_obj.cols])
				assert os.path.isfile( file_obj.file_name)
				#print (table_name, apx)
				#e()
				apxq= ',\n'.join(['']+["%s AS '%s'" % (k,v) for k, v in apx.items() ]) if apx else ''
				stmt="""
COPY %s (%s %s) 
FROM LOCAL '%s' 
DELIMITER '|' ESCAPE AS '^' NULL '' 
SKIP %d ABORT ON ERROR NO COMMIT """  % (table_name, copyfmt, apxq, file_obj.file_name, skip)
				try:
					psql(stmt, 'Load')
					trans.cur.execute(stmt)
					
				except:
					trans.conn.rollback()
					pfmt([[stmt]])
					
					raise
					
				accepted, rejected = trans.cur.execute('SELECT GET_NUM_ACCEPTED_ROWS(),GET_NUM_REJECTED_ROWS()').fetchall()[0]
				pfmt([[lcnt-skip, accepted, rejected]], ['Line count', 'Accepted','Rejected'], 'Load stats')
				assert lcnt - skip == accepted
				
				out=OrderedDict()
				out['table_name'] = table_name
				out['accepted'] = accepted
				out['rejected'] = rejected
				out['linecount']= lcnt
				out['skip'] 	= skip
				out['diff'] 	= lcnt - skip - accepted
				stats[table_name]=out
	@api
	@ctimeit
	def load_grds_file( self, trans, file_obj, schema, table_name, qname, fmt_cols, cfg, skip=0, apx = None, stats=None):

		scfg, tcfg = cfg
		file_name = file_obj.file_name
		
		
		
		

		assert os.path.isfile(file_name)
		if 1:
			colsep= scfg['columnDelimiter']
			assert colsep

			lcnt = file_obj.line_count(file_name)
			

			if 1:
				cols = ','.join([col[0] for col in file_obj.cols])

				trans.conn.autocommit = False

				copyfmt=',\n'.join(["%s FORMAT 'hex'" % col[0] if col[0] in fmt_cols else "%s" % col[0]  for col in file_obj.cols])
				assert os.path.isfile( file_obj.file_name)
				#print (table_name, apx)
				#e()
				apxq= ',\n'.join(['']+["%s AS '%s'" % (k,v) for k, v in apx.items() ]) if apx else ''
				stmt="""
COPY %s (%s %s) 
FROM LOCAL '%s' 
DELIMITER '|' ESCAPE AS '^' NULL '' 
SKIP %d ABORT ON ERROR NO COMMIT """  % (table_name, copyfmt, apxq, file_obj.file_name, skip)
				try:
					psql(stmt, 'Load')
					trans.cur.execute(stmt)
					
				except:
					trans.conn.rollback()
					pfmt([[stmt]])
					
					raise
					
				accepted, rejected = trans.cur.execute('SELECT GET_NUM_ACCEPTED_ROWS(),GET_NUM_REJECTED_ROWS()').fetchall()[0]
				pfmt([[lcnt-skip, accepted, rejected]], ['Line count', 'Accepted','Rejected'], 'Load stats')
				assert lcnt - skip == accepted
				
				out=OrderedDict()
				out['table_name'] = table_name
				out['accepted'] = accepted
				out['rejected'] = rejected
				out['linecount']= lcnt
				out['skip'] 	= skip
				out['diff'] 	= lcnt - skip - accepted
				stats[table_name]=out
	@api
	@ctimeit
	def load_gfin_file( self, trans, file_obj, schema, table_name, qname, fmt_cols, cfg, skip=0, apx = None, stats=None):

		scfg, tcfg = cfg
		file_name = file_obj.file_name
		
		
		
		

		assert os.path.isfile(file_name)
		if 1:
			colsep= scfg['columnDelimiter']
			assert colsep

			lcnt = file_obj.line_count(file_name)
			

			if 1:
				cols = ','.join([col[0] for col in file_obj.cols])

				trans.conn.autocommit = False

				copyfmt=',\n'.join(["%s FORMAT 'hex'" % col[0] if col[0] in fmt_cols else "%s" % col[0]  for col in file_obj.cols])
				assert os.path.isfile( file_obj.file_name)
				#print (table_name, apx)
				#e()
				apxq= ',\n'.join(['']+["%s AS '%s'" % (k,v) for k, v in apx.items() ]) if apx else ''
				stmt="""
COPY %s (%s %s) 
FROM LOCAL '%s' 
DELIMITER '|' ESCAPE AS '^' NULL '' 
SKIP %d ABORT ON ERROR NO COMMIT """  % (table_name, copyfmt, apxq, file_obj.file_name, skip)
				try:
					psql(stmt, 'Load')
					trans.cur.execute(stmt)
					
				except:
					trans.conn.rollback()
					pfmt([[stmt]])
					
					raise
					
				accepted, rejected = trans.cur.execute('SELECT GET_NUM_ACCEPTED_ROWS(),GET_NUM_REJECTED_ROWS()').fetchall()[0]
				pfmt([[lcnt-skip, accepted, rejected]], ['Line count', 'Accepted','Rejected'], 'Load stats')
				assert lcnt - skip == accepted
				
				out=OrderedDict()
				out['table_name'] = table_name
				out['accepted'] = accepted
				out['rejected'] = rejected
				out['linecount']= lcnt
				out['skip'] 	= skip
				out['diff'] 	= lcnt - skip - accepted
				stats[table_name]=out
				
	@api
	@ctimeit
	def load_file( self, trans, file_obj, schema, table_name, qname, fmt_cols, cfg, skip=0, apx = None, stats=None):

		scfg, tcfg = cfg
		file_name = file_obj.file_name
		
		
		
		

		assert os.path.isfile(file_name)
		if 1:
			colsep= scfg['columnDelimiter']
			assert colsep

			lcnt = file_obj.line_count(file_name)
			

			if 1:
				pp(file_obj.cols)
				
				#cols = ','.join([col.decode() for col in file_obj.cols])
				#pp(cols)
				
				trans.conn.autocommit = False
				
				copyfmt=',\n'.join(["%s FORMAT 'hex'" % col[0] if col[0] in fmt_cols else "%s" % col  for col in file_obj.cols_alt])

				assert os.path.isfile( file_obj.file_name)
				
				stmt="""
COPY %s.%s (%s ) 
FROM LOCAL '%s' 
DELIMITER '|' ESCAPE AS '^' NULL '' 
SKIP %d ABORT ON ERROR NO COMMIT """  % (schema, table_name, copyfmt, file_obj.file_name, skip)
				try:
					self.desc_table(schema, table_name)
					psql(stmt, 'Load')
					trans.cur.execute(stmt)
					
				except:
					trans.conn.rollback()
					psql(stmt)
					
					raise
					
				accepted, rejected = trans.cur.execute('SELECT GET_NUM_ACCEPTED_ROWS(),GET_NUM_REJECTED_ROWS()').fetchall()[0]
				pfmtd([dict(Line_count=lcnt-skip, Accepted= accepted, Rejected=rejected)], 'Load stats')
				assert lcnt - skip == accepted
				
				out=OrderedDict()
				out['table_name'] = table_name
				out['accepted'] = accepted
				out['rejected'] = rejected
				out['linecount']= lcnt
				out['skip'] 	= skip
				out['diff'] 	= lcnt - skip - accepted
				stats[table_name] = out
	@api
	@ctimeit
	def load_md5( self, trans, file_obj, table_name, qname, fmt_cols, cfg, skip=0, apx = None, stats=None):

		scfg, tcfg = cfg
		file_name = file_obj.file_name
		
		
		
		

		assert os.path.isfile(file_name)
		if 1:
			colsep= scfg['columnDelimiter']
			assert colsep

			lcnt = file_obj.line_count(file_name)
			

			if 1:
				cols = ','.join([col[0] for col in file_obj.cols])

				trans.conn.autocommit = False

				copyfmt=',\n'.join(["%s FORMAT 'hex'" % col[0] if col[0] in fmt_cols else "%s" % col[0]  for col in file_obj.cols])
				assert os.path.isfile( file_obj.file_name)
				#print (table_name, apx)
				#e()
				apxq= ',\n'.join(['']+["%s AS %s" % (k,v) for k, v in apx.items() ]) if apx else ''
				stmt="""
COPY %s (%s %s) 
FROM LOCAL '%s' 
DELIMITER '|' ESCAPE AS '^' NULL '' 
SKIP %d ABORT ON ERROR NO COMMIT """  % (table_name, copyfmt, apxq, file_obj.file_name, skip)
				try:
					psql(stmt, 'Load')
					trans.cur.execute(stmt)
					
				except:
					trans.conn.rollback()
					pfmt([[stmt]])
					
					raise
					
				accepted, rejected = trans.cur.execute('SELECT GET_NUM_ACCEPTED_ROWS(),GET_NUM_REJECTED_ROWS()').fetchall()[0]
				pfmt([[lcnt-skip, accepted, rejected]], ['Line count', 'Accepted','Rejected'], 'Load stats')
				assert lcnt - skip == accepted
				
				out=OrderedDict()
				out['table_name'] = table_name
				out['accepted'] = accepted
				out['rejected'] = rejected
				out['linecount']= lcnt
				out['skip'] 	= skip
				out['diff'] 	= lcnt - skip - accepted
				stats.append(out)

					
	def show_row(self, data, file_cols):	
		if 1:
			from include.fmt import get_formatted
			cols=[]
			for i, col in enumerate(file_cols):
				cols.append(col[0]) 
			print (get_formatted('',[[j,cols[j],file_cols[j][1], d, type(d)] for j, d in enumerate(data[0])

			],['id','col', 'type','data', 'dtype'],join = True))
			
			