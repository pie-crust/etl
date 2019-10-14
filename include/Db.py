(cli, conn_pool)=app_init
import os, sys,re, pyodbc, platform
from pprint import pprint as pp
e=sys.exit
import logging
log=logging.getLogger('cli')
from include.utils import  slogger, ctimeit, clierr, api
from include.fmt import pfmt, psql
pid=None



def close_cons(conn_pool):
	keys= [k for k in conn_pool.keys()]
	for k in keys:
		con= conn_pool[k]
		cn=con.__class__.__name__
		if  cn in ['Connection']:
			try:
				print ('Closing conn ' + k)
				con.rollback()
				conn_pool.pop(k)
			except Exception as ex:
				raise
						
def appexit():
	global pid
	if pid==0:
		print ('<<child atexit>>')
	else:
		close_cons(conn_pool)		
		print ('<<parent atexit>>')
import atexit
atexit.register(appexit)

class Db(object):
	@ctimeit
	def __init__(self, *args, **kwargs):
		#print connStr
		self.cli =cli= kwargs.get('cli', None)
		assert cli
		self.cpool =cpool= kwargs.get('conn_pool', None)
		self.cln=cln= self.__class__.__name__
		#print (11111111111111,kwargs.get('env'))
		#e()
		self.dbenvars=dbenvars={}
		if 0:
			self.env_key =env_key= kwargs.get('env', self.cln)
			assert env_key
			print(env_key)
			env_vars=cli.get_store_env_refs(env_key)
			pp(env_vars)

			
			
			
			for k, v in env_vars.items():
				#print 11111, k, v,  env_vars.keys()[env_vars.values().index(v)]
				dbenvars[k]=os.environ.get(v)
				if 0:
				
					if not dbenvars[k] and cli.rte in ['DEV']:
						envf= os.path.join(home, '.envs', '.%s.%s' % (cli.rte, self.cln))
						assert os.path.isfile (envf)
						with open(envf, 'r') as fh:
							
								line=fh.readline()
								line=line.strip().strip(r'\n').strip(os.linesep)
								while line:
									#pp(line)
									if  line.strip().startswith('export'):
										exp, kvals=line.split()
										
										kval= kvals.strip().split('=')
										#print kval[0], '='.join(kval[1:])
										dbenvars[kval[0]]='='.join(kval[1:])
										
									line=fh.readline()
				if not dbenvars[k] and k == 'DB_READ_WSID':
					dbenvars[k]= platform.uname()[1]
				assert dbenvars[k], '"%s" is not defined in os environment' % v
			
		if 0:

			self.set_conn_str(cli.stores[dbenv]['connectionString'])
		self.envars=self.cli.get_runtime_env_vars()
		#pp(self.envars)
		#e()
		self.cur=self.conn=None
		self.apx_cmap,self.apx=self.cli.get_appendix()
		
	def get_cols(self):
		cli=self.cli
		if not self.cur:
			print ('Reopening cursor ', '#'*80)
			self.cur = self.conn.cursor()

		
		self.cur.execute('SELECT * from %s.%s WHERE 1=2' % (cli.tcfg['targetSchema'],cli.tcfg['targetTable']))

		return [col[0] for col in self.cur.description]
	def get_columns(self):
		cli=self.cli
		if not self.cur:
			print ('Reopening cursor ', '#'*80)
			self.cur = self.conn.cursor()

		
		self.cur.execute('SELECT * from %s.%s LIMIT 0' % (cli.tcfg['targetSchema'],cli.tcfg['targetTable']))
		#from collections import OrderedDict
		out={}
		if 1:			
			for id,column in enumerate(self.cur.description):
				out[column[0].encode()]= id
		return out
	def get_tab_cols(self, tab):
		cli=self.cli
		if not self.cur:
			print ('Reopening cursor ', '#'*80)
			self.cur = self.conn.cursor()
		self.cur.execute('SELECT * from %s LIMIT 0' % tab )
		out=[]
		for id,column in enumerate(self.cur.description):
			out.append((column[0].encode(), column[1]))
		return out
		
	def get_header(self):
		return list(self.cur.description)
	@ctimeit
	def set_conn_str(self,connStr):
	
		self.connStr=connStr.format(**self.dbenvars)

		#log.debug(self.connStr)
	def set_dbenvars(self, env):
		env_vars=cli.get_store_env_refs(env)
		#print env
		#pp(env_vars)
		#e()
		
		dbenvars={}
		
		for k, v in env_vars.items():
			#print 11111, k, v,  env_vars.keys()[env_vars.values().index(v)]
			dbenvars[k]=os.environ.get(v)
			if 0:
			
				if not dbenvars[k] and cli.rte in ['DEV']:
					envf= os.path.join(home, '.envs', '.%s.%s' % (cli.rte, self.cln))
					assert os.path.isfile (envf)
					with open(envf, 'r') as fh:
						
							line=fh.readline()
							line=line.strip().strip(r'\n').strip(os.linesep)
							while line:
								#pp(line)
								if  line.strip().startswith('export'):
									exp, kvals=line.split()
									
									kval= kvals.strip().split('=')
									#print kval[0], '='.join(kval[1:])
									dbenvars[kval[0]]='='.join(kval[1:])
									
								line=fh.readline()
			if not dbenvars[k] and k == 'DB_READ_WSID':
				dbenvars[k]= platform.uname()[1]
			assert dbenvars[k], '"%s" is not defined in os environment' % v
		#pp(dbenvars)
		self.dbenvars[env] = dbenvars
		#e()
	def get_conn_str(self, env):
		
		dbenv=cli.dbcfg['env'][cli.rte][env]
		assert dbenv
		#print dbenv, cli.rte, env
		connStr= cli.stores[dbenv]['connectionString']
		#print 6678, connStr
		#e()
		#pp(self.dbenvars)
		if env not in self.dbenvars:
			self.set_dbenvars(env)
		return connStr.format(**self.dbenvars[env])
		
	@ctimeit
	def get_connect(self, env, use_pool=True):	
		if env not in self.dbenvars:
			self.set_dbenvars(env)	
		conn_key='%s.%s.%s.%s' % (self.cln,env,self.dbenvars[env].get('DB_READ_SERVER', 'NA'),self.dbenvars[env].get('DB_READ_USER','NA'))	
		cli=self.cli

		#e()
		if conn_key in self.cpool.keys() and use_pool:
			log.debug('%s: Reusing connect.' % self.cln)
			return self.cpool[conn_key]
		else:
			log.debug('%s: New connect.' % self.cln)
			conn=self.cpool[conn_key]= self._connect(env)
			return conn

	@ctimeit
	def _connect(self, env):
		if 1:
			envars=self.envars
			for k in envars:
				_= os.getenv(k)
		pyodbc.pooling = False
		connStr=self.get_conn_str(env)
		try:
			log.info('Connecting...')
			conn= pyodbc.connect(connStr, autocommit=False)
			log.info('Post connect.')
			
		except Exception as err:
			log.debug(connStr)
			log.error(err)
			raise

		if 0:		
			#conn.setdecoding(pyodbc.SQL_CHAR, encoding='latin-1')
			conn.setdecoding(pyodbc.SQL_CHAR, encoding='latin-1')
			#conn.setdecoding(pyodbc.SQL_WCHAR, encoding='latin-1')
			#conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='latin-1')
			
			#conn.setdecoding(pyodbc.SQL_WCHAR, encoding='latin-1')
		if 0:		
			conn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
			conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
		if 0:		
			conn.setdecoding(pyodbc.SQL_CHAR, encoding='ascii')
			conn.setdecoding(pyodbc.SQL_WCHAR, encoding='ascii')			
		return conn
	@ctimeit
	def begin_transaction(self, env, out, reset_conn=False):
		if reset_conn:
			self.conn=self._connect(env)
			assert self.conn
		if not self.conn:
			self.conn=self.get_connect(env)
		
		self.cur=cur=self.conn.cursor()
		out.conn, out.cur = self.conn, cur
		return out 
	def exec_query(self, stml, show=False):		
		cur=self.conn.cursor()
		if show: psql(stml)
		return cur.execute(stml)
	@ctimeit
	def commit_transaction(self, trans, close_conn=False):
		trans.conn.commit()
		if close_conn:
			trans.conn.close()
	@api
	@ctimeit			
	def truncate_table(self, table):
		self.exec_ddl('TRUNCATE TABLE %s' % table)			
	def exec_ddl(self, ddl):		
		psql(ddl)
		try:
			return self.cur.execute(ddl)
		except Exception as ex:
			
			raise
		
	def exec_dml(self, dml, trans, commit=False):
		#log.debug(dml)
		try:
			out = trans.cur.execute(dml).rowcount
			if commit:
				trans.conn.commit()
				pfmt([[dml]],['DML'],'Commited'.upper())
			return out
		except:			
			trans.conn.rollback()
			pfmt([[dml]],['DML'],'Rolled back'.upper())
			raise
		
		
	def get_query(self,cfg, qname):
		cli=self.cli
		if 1:
			stmt,pcnt=cfg[qname]
			pars = re.findall("(\{[0-9a-zA-Z_\'\'\.\*]+\})", stmt)
			fmt={}
			assert len(pars)==pcnt, '[%s]: Number of params in statement (%s) does not match declarent params count (%s).' % (qname, len(pars), pcnt)
			
			if pars: # "if match was successful" / "if matched"
				for p in [p.strip('}').strip('{') for p in pars if p not in [qname]]:
					try:
						assert  p in cfg or p.lower().startswith('colparam_') or p.lower().startswith('cli*')  or (p.lower().startswith('optparam_')  and  p.split('_')[1].isdigit()), '[%s]: SQL params should be json section keys or opt/proc param ids (optparam_nnn) or column param names (colparam_xxx) or cli atributes (cli*xxx)' % p
					except:
						pp(cfg)
						pp(stmt)
						pp(p)
						raise
					if p in cfg: fmt[p]= cfg.get(p); continue
					if p.lower().startswith('optparam_'): fmt[p]= cli.pa[int(p.split('_')[1])]; continue
					if p.lower().startswith('colparam_'): 
						pp(self.apx_cmap)
						assert self.apx_cmap, 'Colparam_* [%s] is used but "apx_cmap" is empty' % p
						fmt[p]= self.apx_cmap[p.split('_')[1]]; 
						continue
					
					if p.lower().startswith('cli*'):
						attr=p.split('*')[1]
						assert hasattr(cli, attr), 'Cli has no attribute "%s" used in "%s":\n%s' % (attr, qname,stmt)
						fmt[p]=getattr(cli, attr)
						continue
					raise Exception(slierr.E_WRONG_PARAM_FORMAT[0]+': [%s]' % p)
					
			if 1:
				stmt = stmt.format(**fmt) 
			return stmt
	
	def reload(self):
		r, w = os.pipe() 
		#print r, w

		#Creating child process using fork 
		pid = os.fork() 
		if not pid: 
			# This is the child process 
			os.close(r) 
			w = os.fdopen(w, 'w') 
			log.debug ("%s:CHILD:Pyodbc connect test."  % self.cln) 
			 
			try:
				pyodbc.pooling = False
				
				
				self.conn= pyodbc.connect(self.connStr)
				w.write('CONNECTED') 
				#discarding
			except:
				w.write('ERROR') 
				raise
			w.close() 
			sys.exit()
		else:
			# This is the parent process 
			# Closes file descriptor w 
			os.close(w) 
			r = os.fdopen(r) 
			str = r.read() 
			if not str:
				log.debug("%s:PARENT:Pyodbc status test: FAILED" % self.cln) 
				pyok =False
			if  str.upper() in ['ERROR']:
				log.info('Pyodbc test error. Exiting...')
				e()
				


		if not pyok:
			if 0 and not reload:
				raise Exception('Cannot connect to IQ because of pyodbc misconfiguration (LD_LIBRARY_PATH)')
			else:
				log.debug('PYODBC connect failed, reloading python.')
				import psutil
				try:
					p = psutil.Process(os.getpid())
					of= p.as_dict(attrs=['open_files','connections'])
					#pp(of)
					#e()
					for handler in of['open_files']: os.close(handler.fd)
					for handler in of['connections']: os.close(handler.fd)
				except Exception:
					raise
				python=sys.executable
				os.execv(python, [python] + sys.argv)

		else:
			pyodbc.pooling = False
			conn= pyodbc.connect(self.connStr)	

			log.debug("%s:PARENT:Pyodbc status test: CONNECTED" % self.cln) 	
			

		