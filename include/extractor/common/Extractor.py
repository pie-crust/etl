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
from include.fmt import pfmtd, psql

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


import datetime 


class Extractor():
	def __init__(self):
		self.objtype='Extractor'
		
	def set_loader(self, obj):
		self.loader=obj
	def get_creds(self):
		if 0:
			aws_ak, aws_sak=self.cli.aws_keys
		else:
			aws_ak, aws_sak=self.cli.get_aws_keys()
		return aws_ak, aws_sak

	@api
	@ctimeit
	def fetch_many(self, chunk_size,  source , qname, out, skip_header, terminate_line =False):
		assert chunk_size
		cli = self.cli
		chunk_size=self.cli.lame_duck if self.cli.lame_duck and chunk_size>self.cli.lame_duck else chunk_size
		assert chunk_size
		tf = "%Y-%m-%d.%H_%M_%S"
		current_ts = time.strftime(tf)
		id=0
		stmt=self.get_query(source, qname)
		log.debug(stmt)
		if not hasattr(self,'cur') or not self.cur:
			self.cur=self.conn.cursor()
		cur=self.cur
		psql(' \n'.join(stmt.replace(',', ', ').split()), 'Extractor cmd')
		#e()
		
		cur.execute(stmt)
		cols= [c[0] for c in cur.description]
		total_read=0
		if 1:
			apx_cmap,apx_cols, apx=cli.get_appendix2()

		header=None
		first =True
		is_apx=[]
		start_time = time.time()
		while True:
			print ('Elapsed [%d] PRE fetch: %s' % (id, time.time() - start_time))
			start_time = time.time()
			out.data=[]
			if self.cli.lame_duck and self.cli.lame_duck<=total_read: break 
			#decrease chunk size 
			if self.cli.lame_duck and self.cli.lame_duck-total_read <chunk_size: chunk_size=self.cli.lame_duck-total_read
			
			fetch_time = time.time()
			rows = cur.fetchmany(chunk_size)
			print ('Elapsed [%d] FMANY: %s' % (id, time.time() - fetch_time))
			print(len(rows))
			#e()
			data=[]
			append_time = time.time()
			if rows:
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
						#pp(d)
						#print len(d), len(d+apx.split(cli.csep)), apx
						#e()
						cols = cols + apx_cols
						is_apx = ['N'] * len(d) + ['Y'] * len(apx_cols)
						d= d+apx.split(cli.csep.decode())
						data.append(d+[''] if terminate_line else []) #data.append('^'.join(str(v) for v in d+apx))
					else:

						if 1:
							is_apx = ['N'] * len(d) 
							data.append(d)
							#header = [col[:2] for ]
						else:
							assert 3==2
							data.append('^'.join(str(v) for v in d)+os.linesep)
					if first:
						pfmtd([dict(Col=col, Row=d[i], Appendix=is_apx[i]) for i, col in enumerate(cols)], 'First row')
						first = False
						#e()

			else:
				break
			out.data=data
			print ('Elapsed [%d] APPEND: %s' % (id, time.time() - append_time))
			
			out.chunk_id, out.current_ts, out.actor = id, current_ts, self.cln
			if not data: 
				break
			print ('Elapsed [%d] POST fetch: %s' % (id, time.time() - start_time))
			yield out
			id +=1
			total_read +=len(data)
	@api
	@ctimeit
	def fetch_chunk(self, chunk_size,  source , qname, out, skip_header, terminate_line =False):
		assert chunk_size
		cli = self.cli
		chunk_size=self.cli.lame_duck if self.cli.lame_duck and chunk_size>self.cli.lame_duck else chunk_size
		assert chunk_size
		tf = "%Y-%m-%d.%H_%M_%S"
		current_ts = time.strftime(tf)
		id=0
		stmt=self.get_query(source, qname)
		log.debug(stmt)
		if not hasattr(self,'cur') or not self.cur:
			self.cur=self.conn.cursor()
		cur=self.cur
		psql(' \n'.join(stmt.replace(',', ', ').split()), 'Extractor cmd')
		#e()
		
		cur.execute(stmt)
		cols= [c[0] for c in cur.description]
		total_read=0
		if 1:
			apx_cmap,apx_cols, apx=cli.get_appendix2()

		header=None
		first =True
		is_apx=[]
		start_time = time.time()
		while True:
		
			print ('Elapsed [%d] PRE fetch: %s' % (id, time.time() - start_time))
			start_time = time.time()
			out.data=[]
			if self.cli.lame_duck and self.cli.lame_duck<=total_read: break 
			#decrease chunk size 
			if self.cli.lame_duck and self.cli.lame_duck-total_read <chunk_size: chunk_size=self.cli.lame_duck-total_read
			
			fetch_time = time.time()
			data=[]
			row = cur.fetchone()
			rid=0

			while row and rid<chunk_size:
				

			
			
				#if rows:
				#for row in rows:
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
					#pp(d)
					#print len(d), len(d+apx.split(cli.csep)), apx
					#e()
					cols = cols + apx_cols
					is_apx = ['N'] * len(d) + ['Y'] * len(apx_cols)
					d= d+apx.split(cli.csep.decode())
					data.append(d+[''] if terminate_line else []) #data.append('^'.join(str(v) for v in d+apx))
				else:

					if 1:
						is_apx = ['N'] * len(d) 
						data.append(d)
						#header = [col[:2] for ]
					else:
						assert 3==2
						data.append('^'.join(str(v) for v in d)+os.linesep)
				if first:
					pfmtd([dict(Col=col, Row=d[i], Appendix=is_apx[i]) for i, col in enumerate(cols)], 'First row')
					first = False
					#e()
				row = cur.fetchone()
				rid +=1

			#else:
				#break
			out.data=data
			out.chunk_id, out.current_ts, out.actor = id, current_ts, self.cln
			if not data: 
				break
			print ('Elapsed [%d] POST fetch: %s' % (id, time.time() - start_time))
			yield out
			id +=1
			total_read +=len(data)
	@api
	@ctimeit
	def get_query_cur(self, chunk_size,  source , qname, out, skip_header, terminate_line =False):
		assert chunk_size
		cli = self.cli
		chunk_size=self.cli.lame_duck if self.cli.lame_duck and chunk_size>self.cli.lame_duck else chunk_size
		assert chunk_size
		tf = "%Y-%m-%d.%H_%M_%S"
		current_ts = time.strftime(tf)
		id=0
		stmt=self.get_query(source, qname)
		log.debug(stmt)
		if not hasattr(self,'cur') or not self.cur:
			self.cur=self.conn.cursor()
		cur=self.cur
		psql(' \n'.join(stmt.replace(',', ', ').split()), 'Extractor cmd')
		#e()
		
		cur.execute(stmt)
		return cur
	@api
	@ctimeit
	def fetch_row(self, cur,  source , qname, out, skip_header, terminate_line =False):
		cols= [c[0] for c in cur.description]
		total_read=0
		if 1:
			apx_cmap,apx_cols, apx=cli.get_appendix2()

		header=None
		first =True
		is_apx=[]
		start_time = time.time()
		if 1:
		
			print ('Elapsed PRE fetch: %s' % ( time.time() - start_time))
			start_time = time.time()
			out.data=[]

			fetch_time = time.time()

			row = cur.fetchone()
			rid=0
			while row :
				

			
			
				#if rows:
				#for row in rows:
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
					#pp(d)
					#print len(d), len(d+apx.split(cli.csep)), apx
					#e()
					cols = cols + apx_cols
					is_apx = ['N'] * len(d) + ['Y'] * len(apx_cols)
					d= d+apx.split(cli.csep.decode())
					yield d+[''] if terminate_line else []
					#data.append(d+[''] if terminate_line else []) #data.append('^'.join(str(v) for v in d+apx))
				else:

					if 1:
						is_apx = ['N'] * len(d) 
						yield d
						#data.append(d)
						#header = [col[:2] for ]
					else:
						assert 3==2
						yield '^'.join(str(v) for v in d)+os.linesep
						#data.append('^'.join(str(v) for v in d)+os.linesep)
				if first:
					pfmtd([dict(Col=col, Row=d[i], Appendix=is_apx[i]) for i, col in enumerate(cols)], 'First row')
					first = False
					#e()
				row = cur.fetchone()
				rid +=1


			print ('Elapsed POST fetch: %s' % (time.time() - start_time))

			
	@api
	@ctimeit
	def fetch_many_async(self, chunk_map,counter,  source , qname, out, skip_header):
		#self.chunk_size=chunk_size= chunk_map[counter.value()]
		#assert not self.cli.lame_duck
		tf = "%Y-%m-%d.%H_%M_%S"
		current_ts = time.strftime(tf)
		id=0
		stmt=self.get_query(source, qname)
		log.debug(stmt)
		#e()
		if not hasattr(self,'cur') or not self.cur:
			self.cur=self.conn.cursor()
		cur=self.cur
		cur.execute(stmt)
		total_read=0
		if skip_header:
			cur.fetchone()
		apx=self.apx
		while True:
			out.data=[]
			#if self.cli.lame_duck and self.cli.lame_duck<=total_read: continue 
			#if self.cli.lame_duck and self.cli.lame_duck-total_read <chunk_size: chunk_size=self.cli.lame_duck-total_read
			#log.debug(counter.value())
			chunk_size=chunk_map.get(counter.value(), 0)
			if not chunk_size: 
				break				
			else:
				rows = cur.fetchmany(chunk_map[counter.value()])

			data=[]
			if 1:
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
						data.append('^'.join(str(v) for v in d)+'^'+apx+os.linesep)
					else:

						if 1:
							data.append(d)
						else:
							data.append('^'.join(str(v) for v in d)+os.linesep)
			if self.cli.lame_duck:
				out.data=data[:self.cli.lame_duck]
			else:
				out.data=data
			out.chunk_id, out.current_ts, out.actor = id, current_ts, self.cln
			if not data: 
				
				break
			yield out
			counter.increment()
			id +=1
			total_read +=len(data)
