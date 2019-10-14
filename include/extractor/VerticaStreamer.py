"""
 time python cli.py -nopp 2 --dump  -dcf config/db_config.json -pcf config/proc/url/DY_FinancingPosition.json --proc_params Repo '2018-12-31 00:00:00'


export VERTICA_SERVER="VDGMBO1.homegroup.com"
export VERTICA_DATABASE="VDGMBO1"
export VERTICA_SCHEMA="Position"
export VERTICA_USER="s_dev_actwrt"
export VERTICA_KERBEROS_SERVICE_NAME="vertica"

#'Driver=Vertica;ServerName=VDGMBO1.homegroup.com;Database=VDGMBO1;KerberosServiceName=vertica;UID=s_dev_actwrt'


   
"""

(home, app_name, log, actors)=app_init
import os, sys, csv, time
import pyodbc
import collections
from pprint import pprint as pp

e=sys.exit

class DbStreamer:

	def __init__(self, cli, cur, start_time):
		self.cli = cli
		self.cur = cur
		log.debug('Created %s' % self.__class__.__name__)
		self.start_time = start_time
		self.first_row=True
		self.description= self.cur.description
		
	def fetchone(self, *args, **kwargs):
		#print 1
		if self.first_row: 
			log.info('First row elapsed: %s sec' % round((time.time() - self.start_time),2))
			self.first_row=False	
		return self.cur.fetchone(*args, **kwargs)
	def fetchall(self, *args, **kwargs):
		if self.first_row: 
			log.info('First row elapsed: %s sec' % round((time.time() - self.start_time),2))
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

			
	def readline(self, *args, **kwargs):
			#print 'line= ', self.cnt
			if self.cli.lame_duck>0 and self.rid>self.cli.lame_duck-1:  return None
			apx_len=len(self.apx.split(self.cli.csep))
			row=self.cur.fetchone()
			#pp(row)
			if row:
				#e()
				#remap cols
				if self.col_map:
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
					#print 'DONE===========', self.cnt,self.rid,self.max_rows_to_read
					#self.Done=True
					#print len(out)
					#e()
					#self.Done=True
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

class VerticaStreamer(object):
	def __init__(self, **kwargs):
		global actors
		self.cli =cli= kwargs.get('cli', None)
		assert cli
		self.cpool =cpool= kwargs.get('conn_pool', None)
		self.cln=cln= self.__class__.__name__
		env_refs=cli.get_store_env_refs('Vertica')
		pp(env_refs)
		self.dbenvars=dbenvars={}
		for k, v in env_refs.items():
			
			dbenvars[k]=os.environ.get(v)
			assert dbenvars[k], '"%s" is not defined in os environment' % v
		pp(dbenvars)
		self.envars=self.cli.get_runtime_env_vars()
		if 1:
			
			self.conn=self.get_connect()
		#e()
		self.apx= ''
		
		

	def get_connect(self):	
		conn_key='%s.%s.%s' % (self.cln,self.dbenvars['DB_READ_SERVER'],self.dbenvars['DB_READ_USER'])	
		cli=self.cli
		dbenv=cli.dbcfg['env'][cli.rte]['Vertica']
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
	def _connect(self):
		envars=self.envars
		
		if 1:
			
			KEYTABFILE=envars['KRB5_CLIENT_KTNAME']; assert KEYTABFILE

			self.setKeytabCache(KEYTABFILE)
		
		if 1:
			for k, v in envars.items():
				os.environ[k]=v
		pyodbc.pooling = False
		conn= pyodbc.connect(self.connStr)	
		return conn

	def setKeytabCache(self,keyTabFile, keyTabPrincipal='',isVertica=True):
		
		V_USER = self.dbenvars['DB_READ_USER']; assert V_USER
		DEFAULT_DOMAIN = self.envars['DEFAULT_DOMAIN']; assert DEFAULT_DOMAIN
		if isVertica:
			if keyTabFile != '':
				verticakeyTabPrincipal = V_USER + '@' + DEFAULT_DOMAIN
				os.system("kinit -k -t {} {}".format(keyTabFile, verticakeyTabPrincipal))
			else:
				message="keyTabFile {} not defined. Check environ variable KRB5_CLIENT_KTNAME".format(keyTabFile)
				print 'ERROR', message
				raise Exception(message)
		else:
			 if keyTabFile != '' and keyTabPrincipal != '':
				os.system("kinit -k -t {} {}".format(keyTabFile, keyTabPrincipal))
			 else:
				message="keyTabFile {} or keyTabPrincipal not defined. Check environ variable KRB5_CLIENT_KTNAME".format(keyTabFile,keyTabPrincipal)
				print 'ERROR', message
				raise Exception(message)
			
	def set_conn_str(self,connStr):
		print connStr
		self.connStr=connStr.format(**self.dbenvars)
	def get_query(self):
		cli=self.cli
		if 1:
			cfg=cli.scfg

			stmt,pcnt=cli.scfg['sourceStmt']
			import re
			
			pars = re.findall("(\{[0-9a-zA-Z_\'\']+\})", stmt)
			fmt={}
			assert len(pars)==pcnt
			if pars: # "if match was successful" / "if matched"
				for p in [p.strip('}').strip('{') for p in pars if p not in ['sourceStmt']]:
					assert  cfg.has_key(p) or (p.lower().startswith('param_')  and  p.split('_')[1].isdigit()), 'SQL params should be "source" keys or param ids (param_n)'
					fmt[p]= cfg.get(p) if cfg.has_key(p) else cli.pa[int(p.split('_')[1])]
				
			pp(fmt)
			
			if 1:
				
									
				stmt = stmt.format(**fmt) 
				print(stmt)
			
				#e()
			return stmt

				
		if 0:
			return self.mock1()
		if 0:
			return self.mock2()
			
	def open_stream(self, _in):
		global actors
		cli=self.cli
		Out = collections.namedtuple('Out','pipe actor col_map')
		if 1:
			cur= self.conn.cursor()
			start_time = time.time()
			if 1:
				stmt=self.get_query()
				cur.execute(stmt)
				#pp(cur.fetchall())
				#print 1234
				#e()
				if 0:
					from_cols={}
					for id,column in enumerate(cur.description):
						from_cols[id]=str(column[0]).strip().upper()
					print from_cols
				pipe=DbStreamer(self.cli,cur=cur, start_time=start_time)
		col_map={}
		if 1:
			with StreamSlicer(cli, pipe, self.apx, max_rows_to_read=self.cli.max_rows_to_read, col_map=col_map) as pipe:
				return Out(pipe=pipe, actor=self.cln, col_map=col_map)
				
		if 0:
			#pp(actors)
			#e()
			from_cols={}
			for id, col in enumerate(cli.scfg["columnMappings"]):
				from_cols[int(id)]=str(col['columnName']).strip().upper()
			#pp(from_cols)
			to_cols= actors['loader'].get_columns()
			assert to_cols
			
			#pp(to_cols)
			#pp(from_cols)
			#print(len(from_cols),len(to_cols))
			assert len(from_cols) == len(to_cols), 'Config vs Target column count mismatch (%d != %d)' % (len(from_cols),len(to_cols))
			miss=0
			for id, col in from_cols.items():
				assert to_cols.has_key(col), 'Config column "%s" does not exists in Target table "%s"' % (col, cli.tcfg['targetTable'])
				if not int(id)==int(to_cols[col]):
					print 'Config column "%s" order is wrong (Config# %d != Target# %d)' % (col, id, to_cols[col])
					miss +=1
			assert miss == 0

			Out = collections.namedtuple('Out','pipe actor col_map')
			cli=self.cli
			apx=self.apx
			mock_file=cli.mf
			assert self.conn
			stmt=self.get_query()
			assert stmt
			
			from_cols=OrderedDict()	
			if mock_file:			
				log.info('%s: Using mock file: %s' % (self.cln,mock_file))
				assert os.path.isfile(mock_file)
				mfh=open(mock_file,'rb')
				if 1:

					header=mfh.readline().strip().split(self.cli.csep)
					#print(header)
					#e()
					for id,column in enumerate(header):
						from_cols[id]=column.strip().upper()
					#pp(from_cols)
					#e()
					col_map=self.get_col_map(from_cols, to_cols)
				#pp(col_map)
				#e()
				pipe=FileStreamer(self.cli,fh=mfh)
				#with FileSlicer(mfh, apx, chunk_size=self.cli.chunk_size) as pipe:
				#	return Out(pipe=pipe, actor='MOCK')		
			else:
				
				pyodbc.pooling = False
				
				assert not os.getenv('LD_PRELOAD')
				assert os.getenv('LD_LIBRARY_PATH') #pyodbc will fail w/o exception
				assert os.getenv('ODBCINI')
				assert os.getenv('ODBCSYSINI')
				assert os.getenv('PYTHONPATH')
				assert os.getenv('KRB5_CLIENT_KTNAME')
				#log.debug(stmt)
				#pp(stmt)
				#e()
				cur= self.conn.cursor()
				start_time = time.time()
				if 1:
					
					if 1:
						cur.execute(stmt)
					else:
						cur.execute("""""")

					for id,column in enumerate(cur.description):
						from_cols[id]=str(column[0]).strip().upper()
					#print from_cols
					
					col_map=self.get_col_map(from_cols,to_cols)
					pipe=DbStreamer(self.cli,cur=cur, start_time=start_time)

			with StreamSlicer(cli, pipe, apx, max_rows_to_read=self.cli.max_rows_to_read, col_map=col_map) as pipe:
				return Out(pipe=pipe, actor=self.cln, col_map=col_map)

	def _get_col_map(self, from_cols, to_cols):
		col_map={}
		
				
		conf_cols={}
		alt_cols={}
		pcnt=0
		for id, col in enumerate(self.cli.scfg["columnMappings"]):
			if str(col['value']).strip().upper() not in  ['Map'.upper()]:
				pcnt +=1
			conf_cols[int(id)]=str(col['columnName']).strip().upper()
			if col.get('altColName'):
				alt_cols[int(id)]=col.get('altColName')
	
			

		#print(len(conf_cols),len(from_cols), pcnt)
		assert len(conf_cols) - pcnt == len(from_cols), 'Source vs Config column count mismatch (%d != %d). (%d are params)' % (len(from_cols), len(conf_cols), pcnt)
		if 1:
			miss=0
			
			for id, col in from_cols.items():
				
				if col not in conf_cols.values():
					if col not in alt_cols.values():
						#print id, col, col in alt_cols.values()
						print 'Column "%s"  is NOT in config' % (col,)
						miss +=1
					else:
						print 'Column "%s"  is IN ALT config [%s]' % (col,conf_cols[id])
						col_map[to_cols[conf_cols[id]]]=id
				else:
					#print 'Column "%s"  is  IN config' % (col,)
					col_map[to_cols[col]]=id
			assert miss==0, '[%d] Source columns are not in Config.' % miss 

		apx_len=len(self.apx.split(self.cli.csep))
		if apx_len:
			log.debug('Increase colmap by apx len [%d]' % apx_len)
			map_len=len(col_map)
			for x in range(map_len,map_len+apx_len):
				col_map[x]=x
			#pp(col_map)
		else:
			print 'APx is empty [%d]' % apx_len
		return col_map
		


	def mock1(self):
		return open('test/mock/%s/test.sql' % self.cli.proc_key, 'r').read()
	def mock2(self):
		return open('test/mock/spFIRPTAReport/test_exec.sql', 'r').read()
