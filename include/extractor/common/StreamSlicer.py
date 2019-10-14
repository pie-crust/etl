import os, sys, time, datetime
try:
	import cStringIO
except ImportError:
	import io as cStringIO	
import logging
import traceback
from include.utils import timeit, ctimeit, csource
log= logging.getLogger('cli')

import csv
class StreamSlicer:
	rid=0
	cnt=0
	
	def __init__(self, cli, cur, apx,  col_map, max_rows_to_read, stmt=None):
		self.cli=cli
		self.cur = cur
		self.apx = apx
		self.max_rows_to_read=max_rows_to_read
		
		self.col_map=col_map
		self.stmt=stmt
		self.si = cStringIO.StringIO()
		log.debug('Created %s' % self.__class__.__name__)
		self.Done=False
		if cli.dump:			
			dn=os.path.dirname(cli.proc_key)
			
			dump_dir=os.path.join('dump',cli.proc_key)	
			fn='raw_dump.%s.csv' % (cli.filter)
			if not os.path.isdir(dump_dir):
				os.makedirs(dump_dir)
			dump_fn= os.path.join(dump_dir,fn )
			print('ORIG: %s' % dump_fn)
			self.dfh=open(dump_fn, 'w')
			if self.cli.dump:
				if cli.mf:
					self.dfh.write(open(cli.mf,'r').readline())
				else:
					sep=str(self.cli.csep.decode())
					self.dfh.write(sep.join([c[0] for c in self.cur.description])+'\r\n')
					
	def show(self, row):
		if row: 
			for id,column in enumerate(self.cur.description):
				print ('%d: %s: [%s]' % (id, column[0],row[id]))

			
	def readline(self, *args, **kwargs):
			if self.cli.lame_duck>0 and self.rid>self.cli.lame_duck-1:  return None
			apx_len=0
			if self.apx:
				sep=str(self.cli.csep.decode())
				apx_len=len(self.apx.split(sep))

			row=self.cur.fetchone()
			if row:

				if 0:
					assert self.col_map
					remapped=[]
					orig=list(row)

					assert len(orig)==(len(self.col_map)-apx_len), 'Row col count (%d) does not math column map length (%d) minus params (%d).' % (len(orig), len(self.col_map),apx_len)
					
					for cid in range(len(orig)):
						remapped.append( orig[self.col_map[cid]])
				else:
					remapped=row
				
				
				if 1:
					if self.cli.dump:
						if 1:
							sep=str(self.cli.csep.decode())
							tod=sep.join([str(b'' if x==None else unicode(x).encode('utf-8')) for x in list(row)])
						else:
							si=self.si
							si.seek(0)
							si.truncate(0)
							
							if 1:				
								import locale
								myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_US.UTF-8");
								cw = csv.writer(si,delimiter=self.cli.csep, quoting=csv.QUOTE_NONE, lineterminator='', escapechar='\\')
								cw.writerow(row)
								tod= si.getvalue()

						self.dfh.write(tod+os.linesep)
						
					if 1:

						out=[]
						for x in remapped:
							if x==None: out.append(b''); continue;
							if isinstance(x, datetime.date) or isinstance(x, datetime.datetime): out.append(str(x).encode('utf-8')); continue;
							if isinstance(x, int) or isinstance(x, float) : out.append(repr(x)); continue;
							if sys.version_info[0] <3:
								out.append(x) 
							else:
								out.append(x.encode())

						self.rid +=1
						self.cnt +=1

						return self.cli.csep.join(out)+self.cli.csep+self.apx.encode()+b'\r\n'
					else:

						si=self.si
						si.seek(0)
						si.truncate(0)
						
						if 1:				
							sep=str(self.cli.csep.decode())

							cw = csv.writer(si,delimiter=str(self.cli.csep.decode()),  quoting=csv.QUOTE_NONE, lineterminator='', escapechar='\\') #'latin-1')

							try:
								
								cw.writerow(remapped)

							except UnicodeEncodeError:
								
								pp(remapped)
	
								if 1:
									
									err_log = cStringIO.StringIO()
									traceback.print_exc(file=err_log)
									error = err_log.getvalue()
									print ('#' * 80)
									print ('ERROR while parsing a row with unicode')
									print ('#' * 80)
									print(error.encode('utf-8'))
									print ('#' * 80)
									print ('#' * 80)
								raise

							self.rid +=1
							self.cnt +=1

							out=si.getvalue().strip()+self.cli.csep+self.apx.encode()

							return out +b'\n'

					
			else:
				return None

	#@ctimeit
	def read(self, *args, **kwargs):
		rows_to_read=args[0] if args else 0
		if not rows_to_read:
			rows_to_read=self.max_rows_to_read
		else:
			if rows_to_read>self.max_rows_to_read:
				rows_to_read=self.max_rows_to_read
		out=[]
		 
		if 1 or self.cnt<rows_to_read:

			for id in range(rows_to_read):
				if  self.cnt>=self.max_rows_to_read: 
					if out:
						return b''.join(out)
					else:
						return b''
				
				data=self.readline()

				if data:
				
					out.append(data)
				else:
					self.Done=True
					break;
			if out:

				return b''.join(out)
			else:
				self.Done=True
				return b''
				
		else:
			
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


