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

if sys.version_info[0] >= 3:
	unicode=bytes

from include.utils import  ctimeit, api,  clierr

try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
builtins.log=log

from include.loader.common.Loader import Loader

class Dir(Loader):
	def __init__(self, **kwargs):
		self.cli =cli= kwargs.get('cli', None)
		assert cli
		self.cln=cln= self.__class__.__name__
		

	def open_file(self,  out, id=0):
		dir=self.get_dir_name()

		if not os.path.isdir (dir):
			os.makedirs(dir)
		self.tofn=tofn=self.get_file_name(id)
		fpath=os.path.join(dir, tofn)
		log.info('Dump file: %s' % fpath)
		out.fpath=fpath
		out.fh=open(fpath, 'wb')

	def get_dir_name(self):
		return self.cli.get_parsed(ckey='dumpDir', cfg=self.cli.dcfg)
		
	def get_file_name(self, id=0):
		cli.file_id=id
		return self.cli.get_parsed(ckey='dumpFileFormat', cfg=self.cli.dcfg)
	def create_header(self, file, header, cfg, terminate_line = False):	

		fh=file.fh
		assert fh
		assert header
		colsep 	= cfg.get('columnDelimiter', None)
		assert colsep		

		eol 	= cfg.get('recordDelimiter', None)
		assert eol		
		ifheader =  cfg.get('writeHeader', None)
		assert ifheader in [0,1]
		

		hfmt 	= cfg.get('headerFormat', None)
		assert hfmt in ['column', 'column:type']
		ttype 	= cfg.get('translateType', None)
		if hfmt in ['column:type']:
			assert ttype
		

		if ifheader:

			apx_cmap,apx_cols, apx=self.cli.get_appendix2()

			cout=[]
			if hfmt in ['column:type']:
				for h in header:
					#pp(h[:2])
					
					cname, ctype = h[:2]
					tname= str(ctype)
					
					assert tname in ttype , 'Add type translation for "%s"' %  tname
					cout.append('%s:%s' % (cname,ttype[ tname]) )
				if apx_cmap:
					apxtypes = self.cli.dcfg["apxColumnTypes"]					
					for k in apx_cols:
						assert k in apxtypes, 'Column "%s" type is not set in dump->apxColumnTypes: %s' % (k, apxtypes)
						ktype= apxtypes[k]
						cout.append('%s:%s' % (k,ktype) )
			else: #just column name (no type)
				for h in header:
					cname=h[0]
					cout.append(cname)
				if apx_cmap:
					for k in apx_cols:
						cout.append(k )
						
			assert len(cout) == len(header)+len(apx_cols)
			#print 77777, len(header),len(apx_cmap.keys()), len(cout), apx, apx_cols

			fh.write(colsep.encode().join([c.encode() for c in cout])+(colsep if terminate_line else '').encode() + eol.encode())
		
	def terminate(self, file):
		#//because 'wc -l' fails to count record without EOL
		dcfg=self.cli.dcfg
		if dcfg.get('terminateFile', 0): 
			terminator = dcfg["recordDelimiter"]
			assert terminator
			file.fh.write(terminator.encode())

	def close_file(self, file):
		
		file.fh.close()
	@api
	@ctimeit
	def append_data(self, file, data, cfg):
		dbdata=data.data
		#pp( dir(data))
		#e()
		fh=file.fh
		start_time = time.time()
		
		colsep 	= cfg.get('columnDelimiter', None)
		assert colsep
		eol 	= cfg.get('recordDelimiter', None)
		assert eol

		ifheader =  cfg.get('writeHeader', None)
		assert ifheader in [0,1]
		
		
		fh.write(eol.encode().join([colsep.encode().join([c if isinstance(c, unicode) else str(c).encode() for c in row]) for row in dbdata]))
		
		if 0:
			for row in dbdata:
				fh.write(colsep.encode().join([c if isinstance(c, unicode) else c.encode() for c in row])+eol.encode())


		sec=round((time.time() - start_time),2)
		
		log.debug('%s: Read:%d,  Header:%s, Elapsed: %s sec/%s min' % (self.cln, len(dbdata), ifheader, sec, round(sec/60, 2)))
	def append_row(self, file, dbrow, cfg):
		#dbdata=data.data
		#pp( dir(data))
		#e()
		fh=file.fh
		
		
		colsep 	= cfg.get('columnDelimiter', None)
		assert colsep
		eol 	= cfg.get('recordDelimiter', None)
		assert eol

		ifheader =  cfg.get('writeHeader', None)
		assert ifheader in [0,1]
		
		
		fh.write(eol.encode().join([colsep.encode().join([c if isinstance(c, unicode) else str(c).encode() for c in row]) for row in [dbrow]]))
		
		if 0:
			for row in dbdata:
				fh.write(colsep.encode().join([c if isinstance(c, unicode) else c.encode() for c in row])+eol.encode())


		
		
		
		
	def delete_dump(self, fn):
		
		for fname in fn.file_names:
			#fname= val[1]['path']
			assert os.path.isfile(fname)
			os.remove(fname)
			log.debug('File removed [%s]' % fname)
			

		