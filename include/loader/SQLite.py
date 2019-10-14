(cli, conn_pool)=app_init
import os, sys, time, imp, math, re, json
import pyodbc, logging
from datetime import datetime
import collections
from pprint import pprint as pp

e=sys.exit
log=logging.getLogger('cli')

from pysqlite2 import dbapi2 as sqlite
from include.utils import  ctimeit, api,  clierr

try:
	import __builtin__ as builtins
except:
	import builtins

builtins.app_init=app_init
builtins.log=log
from include.Db import Db
from include.loader.common.Loader import Loader

class SQLite(Db, Loader):
	def __init__(self, **kwargs):
		Db.__init__(self, **kwargs)
		self.conn=self.get_connect(self.cln)
		self.cur=self.conn.cursor()
	@ctimeit
	def _connect(self, env):
		lite_dir= self.cli.get_parsed(ckey='targetLiteDir', cfg=self.cli.tcfg)
		assert lite_dir
		if not os.path.isdir(lite_dir):
			os.makedirs(lite_dir)
		db= '%s_%s.db' % (self.cli.tcfg ['targetDb'], cli.tss)
		db= '%s.db' % self.cli.tcfg ['targetDb']
		self.localdb=os.path.join(lite_dir, db)
		
		conn= sqlite.connect(self.localdb)

		return conn

	@api
	@ctimeit			
	def truncate_table(self, table):
		stmt = 'DELETE FROM %s' % table
		self.cur.execute(stmt)
		self.conn.commit()
		
	def get_table_cols(self, tab):	
		stmt='SELECT * FROM %s WHERE 1=2' % tab
		self.cur.execute(stmt)
		cols=[]
		for id,col in enumerate(self.cur.description):
			cols.append(col[0])
		return cols
		
	def set_conn_str(self,connStr):
		self.connStr=''


	def insert_data(self,trans, table, data):
		if data:
			conn, cur = trans.conn, trans.cur
			qmarks=('?,' * len(data[0])).strip(',')
			self.cur.executemany('INSERT INTO %s VALUES (%s)' % (table, qmarks), data)
			self.conn.commit()
		else:
			log.warn('Empty data set. Passing...')
	@api
	@ctimeit
	def show_data(self,  table):
		sql='SELECT * FROM %s' % table
		for row in self.exec_ddl(sql):
			print(row)

	def get_header_cols(self, fh, scfg):
		colsep= scfg['columnDelimiter']
		assert colsep
		hsize= int(scfg['writeHeader'])
		if hsize in [1]:
			header= fh.readline().strip()
			dtsep=':'
			cols=[col.split(dtsep) for col in header.split(colsep)]
			assert len(cols)
			assert dtsep in header, 'SQlite file must have header column.\n>>>%s<<<' % header
			assert len(cols[0]) == 2, 'Wrong header format. Expecting: COLUMN_NAME:DATATYPE'
		elif hsize in [2]:
			header= fh.readline().strip()
			cnames=[col for col in header.strip().split(colsep)][:-1]
			assert len(cnames)
			if 1:
				header2= fh.readline().strip()
				ctypes=[col for col in header2.strip().split(colsep)][:-1]
				assert len(ctypes)

			return [(nm, ctypes[i]) for i, nm in enumerate(cnames)]
		else:
			raise Exception('Wrong header size: [%d]' % hsize)
		return cols
	def create_table(self, fh, cfg, table_name):
		scfg, tcfg = cfg
		cols = self.get_header_cols(fh,scfg)


		clist = ',"'. join('" '.join(col) for col in cols)
		ddl='CREATE TABLE %s ("%s)' % (table_name,clist )

		try:
			self.exec_ddl(ddl)
		except:
			raise

	def drop_table(self,   table_name):

		ddl='DROP TABLE %s' % (table_name )

		try:
			self.exec_ddl(ddl)
		except sqlite.OperationalError as ex:
			if not str(ex).startswith('no such table:'):
				raise

	@api
	@ctimeit
	def bulk_insert(self, trans, file_names, qname, cfg, create_table=False, strip_line_term = False):
		scfg, tcfg = cfg
		tbl = cli.get_parsed(ckey='targetTable', cfg=tcfg)
		fnames=file_names.file_names
		for path in file_names.file_names:
			assert os.path.isfile(path)
			tbl = path.split('.')[-2]
			with open(path, 'r') as fh:
				colsep= scfg['columnDelimiter']
				assert colsep
				if create_table:
					self.drop_table(  tbl)
					self.create_table( fh, cfg, tbl)
				data=[]
				for line in [x.strip()  for x in  fh]:
					data.append(line.strip()[:-1].split(colsep) if strip_line_term else line.split(colsep) )
				self.insert_data( trans, tbl, data)
	@api
	@ctimeit
	def load_file( self, trans, file_name, table_name, qname, cfg, create_table=False):
		scfg, tcfg = cfg
		assert os.path.isfile(file_name)
		with open(file_name, 'r') as fh:
			colsep= scfg['columnDelimiter']
			assert colsep
			if create_table:
				self.create_table( fh, cfg, table_name)
			data=[]
			for line in [x.strip()  for x in  fh]:

				data.append(line.split(colsep)[:-1])
			self.insert_data(trans, table_name, data)
