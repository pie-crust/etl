"""
 time ./_dataMigration.sh --config ./config/DBConfig.json --configKey Daily_FinancingPosition  --params 223906 $(date -d '-3 day' +\%m/\%d/\%Y) $(date -d '-3 day' +\%m/\%d/\%Y) EOD EOD '*' '*' '*' NONE '*' NOW 0
  time python cli.py -dcf config/db_config.json -pcf config/proc/Daily_FinancingPosition.json --proc_params  223906 01/01/2018 01/05/2018 EOD EOD HORZ '*' '*' NONE '*' NOW 0

  
"""
(cli, conn_pool)=app_init
import os, sys, time, imp, math, re, json
import pyodbc, logging
from datetime import datetime
import collections

log=logging.getLogger('cli')



try:
    import cStringIO
except ImportError:
    import io as cStringIO
	
from pprint import pprint as pp

e=sys.exit



from include.utils import  ctimeit, api,  clierr

try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
builtins.log=log

from include.Db import Db
from include.loader.common.Loader import Loader
from include.fmt import get_formatted

def pfmt(data, header=['Col_1'], title=''):
	print get_formatted(title,data,header,join = True)
						
						
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
				out[column[0].encode()]= id
		return out
	def get_columns(self, table):
		cli=self.cli
		if not self.cur:
			self.cur = self.conn.cursor()

		
		self.cur.execute('SELECT * from %s LIMIT 0' % table)
		#from collections import OrderedDict
		out={}
		if 1:			
			for id,column in enumerate(self.cur.description):
				out[id]= column[0].encode()
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

	def get_table_cols(self, tab):
	
		
		stmt='SELECT * FROM %s WHERE 1=2' % tab
		#print 123, stmt
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
		for fnamed in file_names.file_names:
			pp(fnamed)
			_, fnd = fnamed
			pp(fnd)
			path = fnd['path']
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
delimited by '%s'
row delimited by '%s'
			""" % (sch, tbl,  clist, path, colsep, linesep)
			#print stmt
			#e()
			try:
				cnt = cur.execute(stmt)
				
				total_ins +=cur.rowcount
			except pyodbc.ProgrammingError, err:
				log.debug(stmt)
				log.error(err)
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
			with open(path, 'r') as fh:
				
				for line in fh:
					line = line.strip()

					if line:
						if b"'" in line: 
							line=line.strip().replace(b"'",b"''")
						data.append(line)
						if 0:
							for i, v in enumerate(line.split(colsep)):
								if cols[i][1] == Decimal:
									print i,v, cols[i][0],  cols[i][1] == Decimal, Decimal(v).quantize(Decimal("0.0000000000001")), float(v)

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
			except pyodbc.ProgrammingError, err:
				log.debug(stmt)
				log.error(err)
				self.conn.rollback()
				raise
	def insert_bulk_vals(self, cur, vals, data, schema, table, cfg):
		scfg, tcfg = cfg
		
		stmt = 'INSERT INTO %s.%s VALUES (%s)' % (schema, table, '),('.join(vals))	
		log.debug(stmt)
		try:
			cur.execute(stmt)
		except pyodbc.ProgrammingError, err:
			log.error(err)
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
			print 'INSERT INTO %s VALUES (%s)' % (table, qmarks)
			
			self.cur.executemany('INSERT INTO %s VALUES (%s)' % (table, qmarks), data)
			self.conn.commit()
		else:
			log.warn('Empty data set. Passing...')
			
	@api
	@ctimeit
	def load_file( self, trans, file_obj, table_name, qname, cfg, create_table=False):

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
	def load_file_2( self, trans, file_obj, table_name, qname, cfg, create_table=False):

		scfg, tcfg = cfg
		file_name = file_obj.file_name
		#pp(file_obj.cols)
		
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
					#print line
					#data.append([x  for x in line.split(colsep)[:-1]])
					data.append([x if x else None for i, x in enumerate(line.split(colsep)[:-1])])
					for i, x in enumerate(line.split(colsep)[:-1]):
						if file_obj.cols[i][1] in ['binary(16)']: 
							intdata[0].append(x if x else None)
							intcols.append(file_obj.cols[i])
					#break
				#print (intdata) 
				#pp(data)
				#self.insert_data_byrow(trans, table_name, data, cfg, file_obj.cols)
				if 1:
					cols = ','.join([col[0] for col in file_obj.cols])
					assert len(file_obj.cols) == len(data[0])
					trans.cur.fast_executemany = True
					#trans.cur.fast_executemany = False
					qmarks='?,'*len(file_obj.cols)
					#data[0][1]='test'
					#data[0][21]='0'
					#import uuid
					#intdata[0][0]= '12957e5c1a49d09d30c2469eb1c60400' #bytearray(b'12957e5c1a49d09d30c2469eb1') #u'00000000-0000-0000-0000-000000000000' #unicode(uuid.uuid4())
					#pp(data[0])
					if 1:
						tmpTbl = 'tmp_%s' % table_name
						stmt='CREATE LOCAL TEMPORARY TABLE %s AS SELECT * FROM %s WHERE 1=2' % (tmpTbl,table_name);
						print(stmt)
						trans.cur.execute(stmt)
						#e()
					#print 777, len(intdata)
					assert len(intdata[0]) == len(intcols)
					#pp(intcols)
					#pp(intdata)
					#e()
					if 0:
						intTbl = 'int_%s' % table_name
						stmt='CREATE LOCAL TEMPORARY TABLE %s AS SELECT * FROM %s WHERE 1=2' % (intTbl,table_name);
						print(stmt)
						trans.cur.execute(stmt)
						#e()					
					#e()
					qmarks=',\n'.join(['HEX_TO_BINARY(?)' if  col[0] in ['TxMasterGUID','SwapEventGUID'] else '?' for col in file_obj.cols])
					stmt='INSERT INTO %s (%s) values(%s)' % (tmpTbl, ',\n'.join([col[0] for col in file_obj.cols]), qmarks.strip(','))
					#print stmt
					pfmt([[stmt]])
					#e()
					trans.conn.autocommit = False
					if 0:
						from include.fmt import get_formatted
						cols=[]
						for i, col in enumerate(file_obj.cols):
							cols.append(col[0]) 
						print get_formatted('',[[j,cols[j],file_obj.cols[j][1], d, type(d)] for j, d in enumerate(intdata[0]) #if file_obj.cols[j][1]  in \
						#['timestamp','integer', 'date', 'double', 'tinyint','bigint','varchar(255)','varchar(32)','varchar(64)']
						#['binary(16)']
						],['id','col', 'type','data', 'dtype'],join = True)
					#self.show_row(data, file_obj.cols)
					#e()
					#trans.cur.executemany(stmt, [data[0]]	)
					
					#pp(trans.cur.fetchall())
					if 0:
						stmt = "COPY %s FROM LOCAL '/home/s_dev_rdm/ab_gtx/iris.csv' DELIMITER '|'" % tmpTbl
					
					stmt="CREATE LOCAL TEMPORARY  TABLE tmp123 (%s)" % ',\n'.join(['%s varchar(100)' % col[0] for col in file_obj.cols])
					stmt="""
CREATE LOCAL TEMPORARY  TABLE tmp123 (TxMasterID varchar(100),
TxMasterGUID binary(16),                                    
TxDetailVersion varchar(100),                                 
TxType varchar(100),                                          
TxTypeCode varchar(100),                                      
TxSubType varchar(100),                                       
TradeDate varchar(100),                                       
SettleDate varchar(100),                                      
DelayedDeliveryDate varchar(100),                             
UserName varchar(100),                                        
Division varchar(100),                                        
TraderID varchar(100),                                        
TraderName varchar(100),                                      
Note varchar(100),                                            
FOTradeID varchar(100),                                       
ValidFromTime varchar(100),                                   
ValidToTime varchar(100),                                     
ParentTxMasterID varchar(100),                                
IsNotionalSettlement varchar(100),                            
ClearingQueueTxStatusTypeCode varchar(100),                   
PositionQueueTxStatusTypeCode varchar(100),                   
SwapEventGUID binary(16),                                   
Desk varchar(100),                                            
DeskCode varchar(100),                                        
ClearingMethod varchar(100),                                  
ClearingMethodID varchar(100),                                
ClearingMethodDescription varchar(100),                       
Price varchar(100),                                           
UnitAmount varchar(100),                                      
ExecutingAccount varchar(100),                                
ExecutingAccountID varchar(100),                              
ClearingAccount varchar(100),                                 
ClearingAccountID varchar(100),                               
SubAccount varchar(100),                                      
SubAccountCode varchar(100),                                  
CashSubAccount varchar(100),                                  
CashSubAccountCode varchar(100),                              
NetSettlement varchar(100),                                   
CPartyNetSettlement varchar(100),                             
GrossAmount varchar(100),                                     
SettlementNetID varchar(100),                                 
SettlementAdjustedDate varchar(100),                          
SettlementAmount varchar(100),                                
SettlementCurrencyID varchar(100),                            
SettlementCurrency varchar(100),                              
SettlementCounterpartyRef varchar(100),                       
SettlementOTCStatusCode varchar(100),                         
SettlementOTCStatus varchar(100),                             
SettlementStatusCode varchar(100),                            
SettlementStatus varchar(100),                                
SettlementMatchStatusCode varchar(100),                       
SettlementMatchStatus varchar(100),                           
SettlementTypeCode varchar(100),                              
SettlementType varchar(100),                                  
SettlementFlagCode varchar(100),                              
SettlementFlag varchar(100),                                  
SettlementModifiedBy varchar(100),                            
SettlementModifiedDateTime varchar(100),                      
ClientID varchar(100),                                        
GroupID varchar(100),                                         
GrossNotionalAmount varchar(100),                             
NetNotionalSecurityQty varchar(100),                          
Quantity varchar(100),                                        
CashQuantity varchar(100),                                    
TradeCurrencyID varchar(100),                                 
ValuationCurrencyID varchar(100),                             
AccruedInterest varchar(100),                                 
IsShortSale varchar(100),                                     
AccrualStatus varchar(100),                                   
AccrualStatusCode varchar(100),                               
PrimaryInstrumentID varchar(100),                             
SwapCollectionID varchar(100),                                
EditSourceCode varchar(100),                                  
EditSource varchar(100),                                      
EditReasonCode varchar(100),                                  
EditReason varchar(100),                                      
ExecutionTime varchar(100),                                   
CurrentFace varchar(100),                                     
TradingPlaceID varchar(100),                                  
ExecutingType varchar(100),                                   
ClearingType varchar(100),                                    
ActingAs varchar(100),                                        
FuturesTradeType varchar(100),                                
FuturesTradeTypeCode varchar(100),                            
TBASettlementType varchar(100),                               
TBASettlementTypeCode varchar(100),                           
CapitalMarketType varchar(100),                               
CapitalMarketTypeCode varchar(100),                           
IsDeltaAdjust varchar(100),                                   
IsCorpAct varchar(100),                                       
FxRateIsMarketConvention varchar(100),                        
OpeningOrClosing varchar(100),                                
SwapID varchar(100),                                          
DividendInterestLiabilityRate varchar(100),                   
DividendInterestWithholdingRate varchar(100),                 
DividendInterestWithholdingAmount varchar(100),               
DividendStatus varchar(100),                                  
DividendStatusCode varchar(100),                              
DeclaredDividendRate varchar(100),                            
GrossDividendRate varchar(100),                               
ReversedTxMasterID varchar(100),                              
ReversalTxMasterID varchar(100),                              
RebookedTxMasterID varchar(100),                              
HasDividendReinvestmentOption varchar(100),                   
GlobalDividendType varchar(100),                              
GlobalDividendTypeCode varchar(100),                          
CorporateActionID varchar(100),                               
HasPIKOption varchar(100),                                    
FxRate varchar(100),                                          
OtherAmount varchar(100),                                     
ExDate varchar(100),                                          
RecordDate varchar(100),                                      
FrankedPercent varchar(100),                                  
IssuingCountry varchar(100),                                  
IssuingCountryID varchar(100),                                
ConversionType varchar(100),                                  
ConversionTypeCode varchar(100),                              
LotID varchar(100),                                           
ExternalTxIdentifierTypeKey varchar(100),                     
IsOptDiv varchar(100),                                        
CAEventTypeID varchar(100))                                   """
					trans.cur.execute(stmt)
					pfmt([[stmt]])
					copyfmt=',\n'.join(["%s FORMAT 'hex'" % col[0] if col[0] in ['TxMasterGUID', 'SwapEventGUID'] else "%s" % col[0]  for col in file_obj.cols])
					stmt="COPY %s (%s) FROM LOCAL'/home/s_dev_rdm/ab_gtx/iris.csv' DELIMITER '|'"  % (tmpTbl, copyfmt)
					pfmt([[stmt]])
					#e()
					trans.cur.execute(stmt)
					
					print 555, trans.cur.rowcount
					
					print 88888888, table_name, trans.cur.execute('select count(*) from %s' % tmpTbl).fetchall()
					if 1:
						import binascii
						for row in  trans.cur.execute('select TxMasterGUID,SwapEventGUID, ExternalTxIdentifierTypeKey, IsOptDiv , CAEventTypeID from %s' % tmpTbl).fetchall():
							print row
							print binascii.hexlify(row[0])
					#trans.conn.commit()

					#pp(dir(trans.cur))
					#e()
	def show_row(self, data, file_cols):	
		if 1:
			from include.fmt import get_formatted
			cols=[]
			for i, col in enumerate(file_cols):
				cols.append(col[0]) 
			print get_formatted('',[[j,cols[j],file_cols[j][1], d, type(d)] for j, d in enumerate(data[0]) #if file_obj.cols[j][1]  in \
			#['timestamp','integer', 'date', 'double', 'tinyint','bigint','varchar(255)','varchar(32)','varchar(64)']
			#['binary(16)']
			],['id','col', 'type','data', 'dtype'],join = True)
			
			