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
import pandas as pd


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


class File(object):
	def __init__(self, **kwargs):
		self.cli =cli= kwargs.get('cli', None)
		assert cli
		self.cln=cln= self.__class__.__name__

	def open_file(self,  out, id=0):
		pp(self.cli)
		#e()
		cfg=self.cli.dcfg
		#pp(self.cli.tcfg)
		dir=self.get_dir_name()
		if not os.path.isdir (dir):
			os.makedirs(dir)
		fn=self.get_file_name(id)
		fpath=os.path.join(dir, fn)
		log.info('Dump file: %s' % fpath)
		out.fpath=fpath
		out.fh=open(fpath, 'wb')

	def get_dir_name(self):

		return self.cli.get_parsed(ckey='dumpDir', cfg=self.cli.get_dcfg())
		
	def get_file_name(self, id=0):
		cli.file_id=id
		return self.cli.get_parsed(ckey='dumpFileFormat', cfg=self.cli.get_dcfg())
	def create_header(self, file, header, cfg):
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
			
			cout=[]
			if hfmt in ['column:type']:
				for h in header:
					#pp(h[:2])
					
					cname, ctype = h[:2]
					tname= str(ctype)
					
					assert tname in ttype , 'Add type translation for "%s"' %  tname
					cout.append('%s:%s' % (cname,ttype[ tname]) )
			else: #just column name (no type)
				for h in header:
					#pp(h[:2])
					
					cname=h[0]
					
					cout.append(cname)
			assert len(cout) == len(header)
			fh.write(colsep.join([c for c in cout])+eol)
		
			
	def terminate(self, file):
		#//because 'wc -l' fails to count record without EOL
		dcfg=self.cli.dcfg
		if dcfg.get('terminateFile', 0): 
			terminator = dcfg["recordDelimiter"]
			assert terminator
			file.fh.write(terminator.encode())

	def close_file(self, file):
		self.terminate(file)
		file.fh.close()
	@api
	@ctimeit
	def append_data(self, file, data, cfg):
		data=data.data
		fh=file.fh
		start_time = time.time()
		
		colsep 	= cfg.get('columnDelimiter', None)
		assert colsep
		eol 	= cfg.get('recordDelimiter', None)
		assert eol

		ifheader =  cfg.get('writeHeader', None)
		assert ifheader in [0,1]

		for row in data:
			fh.write(colsep.join([unicode(c) for c in row])+eol)


		sec=round((time.time() - start_time),2)
		
		log.debug('%s: Read:%d,  Header:%s, Elapsed: %s sec/%s min' % (self.cln, len(data), ifheader, sec, round(sec/60, 2)))
	def delete_dump(self, fn):
		
		for val in fn.file_names:
			fname= val[1]['path']
			assert os.path.isfile(fname)
			os.remove(fname)
			log.debug('File removed [%s]' % fname)
			

		