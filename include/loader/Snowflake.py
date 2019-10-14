"""
 time ./_dataMigration.sh --config ./config/DBConfig.json --configKey Daily_FinancingPosition  --params 223906 $(date -d '-3 day' +\%m/\%d/\%Y) $(date -d '-3 day' +\%m/\%d/\%Y) EOD EOD '*' '*' '*' NONE '*' NOW 0
  time python cli.py -dcf config/db_config.json -pcf config/proc/Daily_FinancingPosition.json --proc_params  223906 01/01/2018 01/05/2018 EOD EOD HORZ '*' '*' NONE '*' NOW 0

  
"""
(cli, conn_pool)=app_init
import os, sys, time, imp, math, re
import pyodbc
from datetime import datetime
import collections
try:
    import cStringIO
except ImportError:
    import io as cStringIO
	
from pprint import pprint as pp

e=sys.exit
import logging
log=logging.getLogger('cli')
from include.utils import  slogger, csource, ctimeit, api
try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
builtins.log=log
from include.Db import Db
from include.loader.common.Loader import Loader

class Snowflake(Db, Loader):
	@csource
	def __init__(self, **kwargs):		
		Db.__init__(self, **kwargs)
		Loader.__init__(self)
		cli=self.cli
		#pp(cs)
		if 1:
			assert 'targetWarehouse' in cli.tcfg, 'Target config missing "targetWarehouse":\n%s' % cli.pcf
			assert 'targetRole' in cli.tcfg, 'Target config missing "targetRole":\n%s' % cli.pcf
			assert 'targetDatabase' in cli.tcfg, 'Target config missing "targetDatabase":\n%s' % cli.pcf
			assert 'targetSchema' in cli.tcfg, 'Target config missing "targetSchema":\n%s' % cli.pcf
			self.conn=self.get_connect(self.cln)
			self.cur = self.conn.cursor()

			self.cur.execute("USE WAREHOUSE %s" % cli.tcfg['targetWarehouse'])
			self.cur.execute("USE ROLE %s" % cli.tcfg['targetRole'])
			self.cur.execute("USE DATABASE %s" % cli.tcfg['targetDatabase'])
			self.cur.execute("USE SCHEMA %s" % cli.tcfg['targetSchema'])


	@api
	@ctimeit
	def insert_data(self, trans	, target , source, stmt, skip_header=0):
		pipe=source.pipe
		skip=str(skip_header).strip()
		if skip_header is not None:
			skip=str(skip_header).strip()
		assert str(skip).strip() in ['0','1'], 'skip_header [%s] should be "0" or "1"' % str(skip).strip()
		if str(skip) == '1':
			pipe.readline()
		assert pipe
		start_time = time.time()
		sql = self.get_query(target,stmt)
		
		cur= self.conn.cursor()
		line=pipe.readline()
		rows=[]
		#pp(line)

		while line:
			rows.append([line[x] for x in sorted(line.keys())] +[self.cli.pa[1], self.cli.asod])
			line=pipe.readline()
		chunk=300
		total=0
		cid=0
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
	@api
	@ctimeit
	def insert_sql_data(self, **kwargs):
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
		sql = self.get_query(self.cli.tcfg,'insertStmt')
		
		cur= self.conn.cursor()
		#line=pipe.cur.fetchone()
		rows=[]
		
		
		print self.cli.apx
		i=0
		if 0:
			while line:
				rows.append(line)
				line=pipe.cur.fetchone()
				i+=1
				#if i>100:
				#	break
		many=900
		pipe.cur.cur.arraysize=many
		rows=pipe.cur.cur.fetchmany(many)
		while rows:
			print i, len(rows)
			if 1:
				cur.fast_executemany = True
				print(sql)
				e()
				cur.executemany(sql,  rows)
				rows=pipe.cur.cur.fetchmany(many)
				i +=1

		log.info('[{}]: {}: Inserted: {:,.0f}, Read: {:,.0f},  Skipped: {}, Elapsed: {}'.format (self.objtype, self.cln, len(rows), pipe.rid,   skip, round((time.time() - start_time),2)))
		pipe.close()

	@api
	@ctimeit
	def get_creds_str(self):
		aws_ak, aws_sak = self.cli.get_aws_keys()
		return "credentials=(aws_key_id='%s' aws_secret_key='%s')" % (aws_ak, aws_sak)
	@api
	@ctimeit

	def bulk_copy_chunk(self,  trans,  target, qname):
		
		start_time=time.time()

		stmt=self.get_query(target, qname)
		stmt="""
%s
%s
""" % (stmt, self.get_creds_str())
		
		#print(stmt)
		#e(0)
		if 1:
			
			try:
				out=trans.cur.execute(stmt) 
			except:
				print(stmt)
				raise
			#pp(out)
			#self.check_status()
			match=0
			status='START'
			for id, row in enumerate(trans.cur.fetchall()):
				status, cnt = row[1:3]
				log.debug('[%s] %s: Insert #%d, status: [%s], row count: [%s]' % (self.objtype, self.cln, id, status, cnt))
				if status not in ['LOADED']:
					match +=1
			if match:
				raise Exception('Unexpected load status [%s]' % status)

			if 0:
				trans.cur.execute("SELECT count(1) from DY_FinancingPosition")
				for row in trans.cur.fetchall():
					print(row)
			
				
	def bulk_copy(self,  trans, file_names, target, qname):
		cli=self.cli

		tbl=cli.tcfg['targetTable']
		stg=cli.tcfg['targetStage']
		sch=cli.tcfg['targetSchema']
		#to_dir=cli.pcfg['targetDir']
		assert tbl and  stg and sch
		if 0:
			cli.file_location=os.sep.join(file_names.file_location.split(os.sep)[1:])
			assert cli.file_location

		chunk=1000
		fnames=file_names.file_names
		total=len(fnames)
		tot_ins = 0
		cid=0
		before=self.get_cnt()
		start_time=time.time()
		while tot_ins<total:
			start_time2=time.time()
			file_group = fnames[tot_ins:][:chunk]
			cli.files="','".join(file_group)
			assert file_group and len(file_group)
			self.bulk_copy_chunk(trans,  target, qname)
			ins=len(file_group)
			tot_ins +=ins
			cid +=1
			#
			
			sec=round((time.time() - start_time2),2)
			log.info('[{}] [{}] {}: Running: {:,.0f}, Rows: {:,.0f}, Elapsed:{} sec/{} min'.format (self.objtype, cid, self.cln, tot_ins, ins, sec, round(sec/60,2)))

		#log.info('Log: %s' % log.file_name)
		sec=round((time.time() - start_time),2)
		log.info('[{}] {}: Inserted:{:,.0f}, To-Schema:{}, To-Table:{} Elapsed:{} sec/{} min'.format(self.objtype, self.cln, self.get_cnt()-before, sch, tbl, sec, round(sec/60,2)))		
		#log.info('Total elapsed: %s sec/%s min' % (sec, round(sec/60,2)))
		#log.debug('"%s" is done.' % cli.proc_key)
	@api
	@ctimeit
	def purge_data(self, **kwargs):

		cur=self.cur
		if 1:
			start_time = time.time()
			cmd = self.get_query(self.cli.tcfg,'purgeStmt')
			log.debug(cmd)
			#e()
			cur.execute(cmd)
			sec=round((time.time() - start_time),2)
			log.info('[%s] %s: Records deleted: %s, Elapsed: %s sec/%s min' % (self.objtype,self.cln,    cur.rowcount, sec, round(sec/60,2)))
			cur.execute('commit')

	@api			
	@ctimeit
	def file_copy(self, **kwargs):
		cli=self.cli
		_in=kwargs.get('_in')
		#pp(_in)
		#e()
		tbl=cli.tcfg['targetTable']
		stg=cli.tcfg['targetStage']
		sch=cli.tcfg['targetSchema']
		#to_dir=cli.pcfg['targetDir']
		assert tbl and  stg and sch
		assert _in.file_cnt 
		assert isinstance(_in.file_cnt, int)
		assert _in.file_filter
		filter=_in.file_filter
		assert _in.file_names
		s3files=_in.file_names
		if 1:
			assert _in.col_map
			#print(_in.col_map)
			#e()

			
		remapped=','.join(['$%s' % (int(col)+1) for col in _in.col_map.values()])
		#print(remapped)
		cols=','.join(['$%d' % (int(cid)+1) for cid in _in.col_map])
		#pp(s3files)
		if 1:
			self.cur = self.conn.cursor()

		#log.info('Files uploaded to S3: %d' % len(s3files))
		before=self.get_cnt()
		start_time=time.time()
		for i, fname in enumerate(s3files):
			
			furl='@%s/%s/%s.gz' % (stg,  cli.proc_key, fname)
			cmd="COPY INTO %s FROM '%s' %s" % (tbl,  furl, self.get_creds_str())
			#print(cmd)
			#e()
			if 1:

				
				self.ex(cmd) 
				#self.check_status()
				match=0
				for id, row in enumerate(self.cur.fetchall()):
					status, cnt = row[1:3]
					log.debug('[%s] %s: Insert #%d, status: [%s], row count: [%s]' % (self.objtype,self.cln, id, status, cnt))
					if status not in ['LOADED']:
						match +=1
				if match:
					raise Exception('Unexpected load status')
					
				self.ex('commit')
		sec=round((time.time() - start_time),2)
		log.info('[{}] {}: {:,.0f} rows inserted into {} in {} sec/{} min'.format (self.objtype,self.cln, self.get_cnt()-before, tbl, sec, round(sec/60,2)))

		log.info('Log: %s' % log.file_name)
		sec=round((time.time() - cli.start_time),2)
		log.info('Total elapsed: %s sec/%s min' % (sec, round(sec/60,2)))
		log.debug('"%s" is done.' % cli.proc_key)
		

				
	def get_cnt(self):
		self.cur.execute("SELECT count(1) from %s" % self.cli.tcfg['targetTable'])
		return self.cur.fetchone()[0]

	def ex(self, cmd):
		log.debug(cmd)
		#print cmd
		self.cur.execute(cmd)
	def show(self):
		#pp(self.cur.description)
		for i, row in enumerate(self.cur.fetchall()):
			
			if 0:
				for id,column in enumerate(self.cur.description):
					print ('%s: [%s]' % (column[0],row[id]))
					break
				
			#e()
	def check_status(self):
		for id, row in enumerate(self.cur.fetchall()):
			status, cnt = row[1:3]
			log.debug('[%s] %s: Insert #%d, status: [%s], row count: [%s]' % (self.objtype,self.cln, id, status, cnt))
		#assert status in [u'LOADED']	

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
		cols=[c[0] for c in cur.description]

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
						v= ["'%s'" % x if x else 'NULL' for x in line.split(colsep)]
						pp(v)
						print len(cols), len(v)
						e()
						vals.append(','.join(v)) 
						rowid +=1
					if len(vals)==limit:
						self.insert_vals(cur, vals, data, sch, tbl, cfg)
						total_ins +=cur.rowcount
						log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))
						vals=[]
						data=[]
					break
			if vals:
				self.insert_vals(cur, vals, data, sch, tbl,cfg)
				total_ins +=cur.rowcount
				log.debug('Read: %d, Inserted: %d ' % (rowid, len(vals)))

			self.conn.commit()
			out.inserted_cnt=total_ins
			log.info('%s: Read:%d, Inserted: %d,  Elapsed: %s' % (self.cln, rowid, total_ins, round((time.time() - start_time),2)))
	def insert_vals(self, cur, vals, data, schema, table, cfg):
		scfg, tcfg = cfg
		stmt = 'INSERT INTO %s.%s VALUES (%s)' % (schema, table, '),('.join(vals))	
		log.debug(stmt)
		try:
			cur.execute(stmt)
		except pyodbc.ProgrammingError, err:
			log.error(err)
			self.conn.rollback()
			raise




