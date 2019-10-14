"""

   
"""

(cli, conn_pool)=app_init
import os, sys, csv, time
import pyodbc
import collections
from pprint import pprint as pp

e=sys.exit
from include.utils import timeit

try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
from include.Db import Db, Extractor

from include.utils import ctimeit, api

import logging
log=logging.getLogger('cli')
	
class DbStreamer:
	def __init__(self, cli, cur, start_time):
		self.cli = cli
		self.cur = cur
		self.cln=self.__class__.__name__
		log.debug('Created %s' % self.cln)
		self.start_time = start_time
		self.first_row=True
		self.description= self.cur.description
		
	def fetchone(self, *args, **kwargs):
		#print 1
		if self.first_row: 
			sec=round((time.time() - self.start_time),2)
			log.info('[%s] First row elapsed: %s sec/%s min' % (self.cln, sec, round(sec/60,2)))
			self.first_row=False	
		return self.cur.fetchone(*args, **kwargs)
	def fetchall(self, *args, **kwargs):
		if self.first_row: 
			sec=round((time.time() - self.start_time),2)
			log.info('[%s] First row elapsed: %s sec/%s min' % (self.cln, sec, round(sec/60,2)))
			self.first_row=False	
		return self.cur.fetchall(*args, **kwargs)

	def write(self, data, *args, **kwargs):
		pass
	def reset(self):
		self.cnt=0
	def __enter__(self):
		return self
	def close(self):
		self.cur.close()
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass
	
try:
    import cStringIO
except ImportError:
    import io as cStringIO	
class StreamSlicer:
	rid=0
	cnt=0
	def __init__(self, cli, cur, apx,  col_map, max_rows_to_read):
		self.cli=cli
		self.cur = cur
		self.apx = apx
		self.max_rows_to_read=max_rows_to_read
		self.col_map=col_map
		self.si = cStringIO.StringIO()
		log.debug('Created %s' % self.__class__.__name__)
		self.Done=False
		if cli.dump:			
			dn=os.path.dirname(cli.proc_key)
			
			dump_dir=os.path.join('dump',cli.proc_key)	
			fn='ORIG.ALL.%s.csv' % (cli.filter)
			if not os.path.isdir(dump_dir):
				os.makedirs(dump_dir)
			dump_fn= os.path.join(dump_dir,fn )
			print('ORIG: %s' % dump_fn)
			self.dfh=open(dump_fn, 'w')
			if self.cli.dump:
				if cli.mf:
					self.dfh.write(open(cli.mf,'r').readline())
				else:
				
					self.dfh.write(self.cli.csep.join([c[0] for c in self.cur.description])+'\r\n')
					
	def show(self, row):
		if row: #for i, row in enumerate(self.cur.fetchall()):
			for id,column in enumerate(self.cur.description):
				print '%d: %s: [%s]' % (id, column[0],row[id])

	#@ctimeit
	def readline(self, *args, **kwargs):
			#print 'line= ', self.cnt
			if self.cli.lame_duck>0 and self.rid>self.cli.lame_duck-1:  return None
			apx_len=len(self.apx.split(self.cli.csep))
			row=self.cur.fetchone()
			#pp(row)
			if row:
				#e()
				#remap cols
				if 'columnMappings' in self.cli.scfg:
					assert self.col_map
					remapped=[]
					orig=list(row)
					#pp(orig)
					assert len(orig)==(len(self.col_map)-apx_len), 'Row col count (%d) does not math column map length (%d) minus params (%d).' % (len(orig), len(self.col_map),apx_len)
					
					for cid in range(len(orig)):
						remapped.append(orig[self.col_map[cid]])
					#pp(remapped)
					#e()
				else:
					remapped=row
				
				if 1:
					if self.cli.dump:
						if 1:
							tod=self.cli.csep.join([str('' if x==None else x) for x in list(row)])
						else:
							si=self.si
							si.truncate(0)
							
							if 1:				
								#print 'delim =', self.cli.csep
								cw = csv.writer(si,delimiter=self.cli.csep, quoting=csv.QUOTE_NONE, lineterminator='', escapechar='\\')
								cw.writerow(row)
								tod= si.getvalue()
							
						#print 'writing to dump'
						#print tod
						#e()
						self.dfh.write(tod+os.linesep)
						
					if 0:
						out=self.cli.csep.join([str('' if x==None else x) for x in list(row)]) +'\r\n'
						self.rid +=1
						self.cnt +=1			
						return out
					else:
						#print 'ROW #%d length: %d' % (self.rid, len(list(remapped))), 'COMA cnt:',str(remapped).count(self.cli.csep),'APPX len:', len(self.apx.split(self.cli.csep)), self.apx
						#print remapped
						si=self.si
						si.truncate(0)
						
						if 1:				
							#cw = csv.writer(si,delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC, lineterminator='')
							cw = csv.writer(si,delimiter=self.cli.csep,  quoting=csv.QUOTE_NONE, lineterminator='', escapechar='\\')
							cw.writerow(remapped)
							self.rid +=1
							self.cnt +=1
							out=si.getvalue().strip()
							#print 'OUT comas:', out.count(self.cli.csep)
							#print 'OUT: ', out
							#e()
							return out 

					
			else:
				return None

	def _read(self, *args, **kwargs):
		chunk_size=args[0]
		if not chunk_size:
			chunk_size=self.chunk_size
		#print 'ARGS==', args
		out=[]
		if self.cnt<self.chunk_size:
			for id in range(self.chunk_size):
				data=self.readline()
				if data:
				
					out.append(data)
				else:
					break;
			if out:
				return ''.join(out)
			else:
				return ''
		else:
			return ''
	@ctimeit
	def read(self, *args, **kwargs):
		rows_to_read=args[0] if args else 0
		if not rows_to_read:
			rows_to_read=self.max_rows_to_read
		else:
			if rows_to_read>self.max_rows_to_read:
				rows_to_read=self.max_rows_to_read
		#print 'ARGS==', args
		out=[]
		 
		if 1 or self.cnt<rows_to_read:
			#print '$$$', self.cnt, rows_to_read,'rid=', self.rid, self.max_rows_to_read

			for id in range(rows_to_read):
				if  self.cnt>=self.max_rows_to_read: 

					if out:
						#print 'returning out 555: ', len(out)
						return ''.join(out)
					else:
						##print '555'
						return ''
				
				data=self.readline()
				if data:
				
					out.append(data)
				else:
					self.Done=True
					break;
			if out:
				#print 'returning out: ', len(out)
				return ''.join(out)
			else:
				self.Done=True
				return ''
				
		else:
			#print '444'
			return ''
				
	def _readline(self, *args, **kwargs):
		return self.cli.csep.join (self.cur.fetchone())
	def _read(self, *args, **kwargs):
		return os.linesep.join([self.cli.csep.join (row) for row in self.cur.fetchall()])
	def write(self, data, *args, **kwargs):
		pass
	def reset(self):
		self.cnt=0
	def __enter__(self):
		return self
	def close(self):
		self.cur.close()
		if self.cli.dump:
			self.dfh.close()
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass
		


class Snowflake(Db, Extractor):
	@ctimeit
	def __init__(self, **kwargs):		
		Db.__init__(self, **kwargs)
		Extractor.__init__(self)
		cli=self.cli

		#e()
		if 1:
			assert 'sourceWarehouse' in cli.scfg, 'Target config missing "sourceWarehouse":\n%s' % cli.pcf
			assert 'sourceRole' in cli.scfg, 'Target config missing "sourceRole":\n%s' % cli.pcf
			assert 'sourceDatabase' in cli.scfg, 'Target config missing "sourceDatabase":\n%s' % cli.pcf
			assert 'sourceSchema' in cli.scfg, 'Target config missing "sourceSchema":\n%s' % cli.pcf
			
			self.conn=self.get_connect()
			self.cur = self.conn.cursor()



			self.cur.execute("USE WAREHOUSE %s" % cli.scfg['sourceWarehouse'])
			self.cur.execute("USE ROLE %s" % cli.scfg['sourceRole'])
			self.cur.execute("USE DATABASE %s" % cli.scfg['sourceDatabase'])
			self.cur.execute("USE SCHEMA %s" % cli.scfg['sourceSchema'])
		#e()
		self.apx= self.cli.apx
	@api
	@ctimeit
	def open_stream(self, dbcfg, qname, out):
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

