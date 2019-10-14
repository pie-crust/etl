
(cli, conn_pool)=app_init
import os, sys, time
import pyodbc
import collections
from subprocess import Popen, PIPE
from pprint import pprint as pp
e=sys.exit
import logging
DB_READER_DATA_DIR = 'dump'
from include.utils import ctimeit, csource, api

try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
from include.Db import Db
log=logging.getLogger('cli')

try:
	import cStringIO
except ImportError:
	import io as cStringIO	

import locale
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_US.UTF-8");
import datetime 


from include.extractor.common.StreamSlicer import StreamSlicer
from include.extractor.common.FileStreamer import FileStreamer
from include.extractor.common.DbStreamer import DbStreamer



from include.extractor.common.Extractor import Extractor

from include.utils import  InOut
from include.fmt import  pfmtd





class IQ(Db, Extractor):
	#@csource 
	def __init__(self, **kwargs):
		Db.__init__(self, **kwargs)
		#self.apx= self.cli.apx
		
		#self.conn=self.get_connect()
	def desc_cur0(self, cur, colord=True):
		rows ={}
		for col in cur.description:
			rows[col[0]]=[col[0], str(col[1]).split("'")[1]	, col[3]]
		out=[]
		for k in sorted(rows.keys()) if colord else rows.keys():
			row=rows[k]
			d = collections.OrderedDict()
			for i in zip(['Column', 'Type', 'Length'], row):
				x,y = i
				d[x]=y
			out.append(d)
		
		pfmtd(out, 'Procedure')		
	def desc_cur(self, cur, colord=True):
		rows ={}
		for col in cur.description:
			rows[col[0]]=[col[0], str(col[1]).split("'")[1]	, col[3]]
		out=[]
		for k in sorted(rows.keys()) if colord else rows.keys():
			row=rows[k]
			d = collections.OrderedDict()
			for i in zip(['Column', 'Type', 'Length'], row):
				x,y = i
				d[x]=y
			out.append(d)
		
		pfmtd(out, 'Procedure')

	def setKeytabCache(self, *args, **kwargs):
		pass

	def parse_conn_str(self,connStr):
		self.connStr=connStr.format(DB_READ_SERVER,DB_READ_USER,DB_READ_PWD)

	@api
	@ctimeit
	def fetch_stream(self, chunk_size,  source , qname, out, skip_header):
		assert chunk_size
		chunk_size=self.cli.lame_duck if self.cli.lame_duck and chunk_size>self.cli.lame_duck else chunk_size
		assert chunk_size
		tf = "%Y-%m-%d.%H_%M_%S"
		current_ts = time.strftime(tf)
		id=0
		cur=InOut()
		self.open_stream(source, qname, out=cur)
		#e()
		return None
		

	@api
	@ctimeit
	def fetch_many0(self, chunk_size,  source , qname, out, skip_header):
		self.chunk_size=chunk_size
		tf = "%Y-%m-%d.%H_%M_%S"
		current_ts = time.strftime(tf)
		self.id=0
		stmt=self.get_query(source, qname)
		if not hasattr(self,'cur'):
			self.cur=cur=self.conn.cursor()
		cur=self.cur
		cur.execute(stmt)
		self.total_read=0
		if skip_header:
			cur.fetchone()
		apx=self.apx
		while True:
			out.data=[]
			if self.cli.lame_duck and self.cli.lame_duck<self.total_read: break 
			if self.cli.lame_duck and self.cli.lame_duck-self.total_read <chunk_size: chunk_size=self.cli.lame_duck-self.total_read
			
			rows = cur.fetchmany(chunk_size)
			self.total_read +=len(rows)
			data=[]
			for row in rows:
				d=[]
				for x in row:
					if x==None: d.append(b''); continue;
					if isinstance(x, datetime.date) or isinstance(x, datetime.datetime): d.append(str(x).encode('utf-8')); continue;
					if isinstance(x, int) or isinstance(x, float) : d.append(repr(x)); continue;
					if sys.version_info[0] <3:
						d.append(x) 
					else:
						d.append(x.encode())
						
				if apx:
					data.append('^'.join(d)+'^'+apx+os.linesep)
				else:
					data.append('^'.join(d)+os.linesep)
			out.data=data
			out.chunk_id, out.current_ts, out.actor = self.id, current_ts, self.cln
			if not data: break
			return out

	@api
	@ctimeit
	def fetch_next(self, out):
		self.id +=1
		chunk_size=self.chunk_size
		apx=self.apx
		while True:
			out.data=[]
			if self.cli.lame_duck and self.cli.lame_duck<self.total_read: break 
			if self.cli.lame_duck and self.cli.lame_duck-self.total_read <chunk_size: chunk_size=self.cli.lame_duck-self.total_read
			rows = self.cur.fetchmany(chunk_size)
			self.total_read +=len(rows)
			data=[]
			for row in rows:
				d=[]
				for x in row:
					if x==None: d.append(b''); continue;
					if isinstance(x, datetime.date) or isinstance(x, datetime.datetime): d.append(str(x).encode('utf-8')); continue;
					if isinstance(x, int) or isinstance(x, float) : d.append(repr(x)); continue;
					if sys.version_info[0] <3:
						d.append(x) 
					else:
						d.append(x.encode())
						
				if apx:
					data.append('^'.join(d)+'^'+apx+os.linesep)
				else:
					data.append('^'.join(d)+os.linesep)
			out.data=data
			out.chunk_id = self.id
			if not data: break
			return out
	@api
	@ctimeit
	def open_query_stream(self, dbcfg, qname, out):
		global actors
		cli=self.cli
		#Out = collections.namedtuple('Out','pipe actor col_map')
		if 1:
			cur= self.conn.cursor()
			start_time = time.time()
			if 1:
				stmt=self.get_query(dbcfg,qname)
				cur.execute(stmt)

				if 0:
					from_cols={}
					for id,column in enumerate(cur.description):
						from_cols[id]=str(column[0]).strip().upper()
					#print from_cols
				pipe=DbStreamer(self.cli,cur=cur, start_time=start_time)
		col_map={}
		if 1:
			
			with StreamSlicer(cli, pipe, self.apx, max_rows_to_read=self.cli.max_rows_to_read, col_map=col_map) as pipe:
				out.pipe, out.actor, out.col_map= pipe, self.cln, col_map
				return out 
	@api
	@ctimeit
	def open_query_cur(self, dbcfg, qname, out):
		global actors
		cli=self.cli
		#Out = collections.namedtuple('Out','pipe actor col_map')
		if 1:
			cur= self.conn.cursor()
			start_time = time.time()
			if 1:
				stmt=self.get_query(dbcfg,qname)
				cur.execute(stmt)

				if 0:
					from_cols={}
					for id,column in enumerate(cur.description):
						from_cols[id]=str(column[0]).strip().upper()
					#print from_cols
				pipe=DbStreamer(self.cli,cur=cur, start_time=start_time)
		out.pipe=pipe
		
	@api
	@ctimeit
	def open_stream(self,dbcfg, qname, out):
		global actors
		cli=self.cli
		alt_cols={}
		from_cols={}
		for id, col in enumerate(cli.scfg["columnMappings"]):
			from_cols[int(id)]=col['columnName'].upper().encode()
			if col.get('altColName'):
				alt_cols[int(id)]= col['columnName'].upper().encode()
		


				
		assert hasattr(self,'loader'), 'You must call "set_loader" first'
		
		if self.loader.cln not in ['Dir']:
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
					log.error ('Config column "%s" order is wrong (Config# %d != Target# %d)' % (col, id, to_cols[col]))
					miss +=1
			assert miss == 0
		else:
			to_cols= {}
	
		col_map=None
		#Out = collections.namedtuple('Out','pipe actor col_map')
		cli=self.cli
		apx=self.apx
		mock_file=cli.mf
		if not self.conn:
			self.begin_transaction  ( env =cli.scfg['sourceDb'] , out = InOut() )
		assert self.conn
		stmt=self.get_query(dbcfg, qname)
		#pp(stmt)
		
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
						to_cols[to_cols] = id
					#to_cols=from_cols
					#pp(from_cols)
					#e()
					col_map=self.get_col_map(from_cols, to_cols)

				pipe=FileStreamer(self.cli,fh=mfh)

			else:
				
				pyodbc.pooling = False


				cur= self.conn.cursor()
				start_time = time.time()
				if 1:
					
					if 1:
						log.debug(stmt)
						cur.execute(stmt)


					for id,column in enumerate(cur.description):
						from_cols[id]=column[0].upper().encode()
						if self.loader.cln  in ['Dir']:
							if id in alt_cols:
								cname= alt_cols[id]
							else:
								cname=column[0].upper().encode()
							to_cols[cname] = id

					col_map=self.get_col_map(from_cols,to_cols)
					pipe=DbStreamer(self.cli,cur=cur, start_time=start_time)
		
			
		with StreamSlicer(cli, pipe, apx, max_rows_to_read=self.cli.max_rows_to_read, col_map=col_map, stmt=stmt) as pipe:
			out.pipe, out.actor, out.col_map = pipe, self.cln,col_map
			return out
	@api
	@ctimeit
	def dump_stream(self, _in):
		data=_in.pipe.read()
		#print(len(data))

	def get_col_map(self, from_cols, to_cols):
		col_map={}

		conf_cols={}
		alt_cols={}
		pcnt=0
		for id, col in enumerate(self.cli.scfg["columnMappings"]):
			if col['value'].upper() not in  [u'Map'.upper()]:
				pcnt +=1
			conf_cols[int(id)]=col['columnName'].upper().encode()
			if col.get('altColName'):
				alt_cols[int(id)]=col.get('altColName').upper().encode()
	

		assert len(conf_cols) - pcnt == len(from_cols), 'Source vs Config column count mismatch (%d != %d). (%d are params)\n Are you sure you have header in your MOCK file?' % (len(from_cols), len(conf_cols), pcnt)
		if 1:
			miss=0

			for id, col in from_cols.items():
				
				if col not in conf_cols.values():
					if col not in alt_cols.values():
						#print id, col, col in alt_cols.values()
						log.info ('Column "%s"  is NOT in config' % (col,))
						miss +=1
					else:
						log.info ('Column "%s"  is IN ALT config [%s]' % (col,conf_cols[id]))
						col_map[to_cols[conf_cols[id]]]=id
				else:
					#print 'Column "%s"  is  IN config' % (col,)
					col_map[to_cols[col]]=id
					
			assert miss==0, '[%d] Source columns are not in Config.' % miss 
		sep=str(self.cli.csep.decode())
		apx_len=len(self.apx.split(sep))
		if apx_len:
			log.debug('Increase colmap by apx len [%d]' % apx_len)
			map_len=len(col_map)
			for x in range(map_len,map_len+apx_len):
				col_map[x]=x
			#pp(col_map)
		else:
			print ('APx is empty [%d]' % apx_len)
		print(len(col_map), apx_len, map_len, self.apx)
		#e()
		return col_map
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
