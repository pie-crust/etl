from include.utils import timeit, ctimeit, csource
import os,  time
try:
	import cStringIO
except ImportError:
	import io as cStringIO	
import logging
import traceback
from include.utils import timeit, ctimeit, csource
log= logging.getLogger('cli')

class FileStreamer:

	def __init__(self, cli, fh):
		self.cli = cli
		self.fh = fh
		self.cln=self.__class__.__name__
		log.debug('Created %s' % self.cln)
		self.start_time = time.time()
		self.first_row=True
		
	def fetchone(self, *args, **kwargs):
		if self.fh.closed:
			return None
		else:
			row=self.readline()
			if row:
				return row.strip().split(str(self.cli.csep.decode()))
			else:
				return None

	def readline(self):
		if self.first_row: 
			sec=round((time.time() - self.start_time),2)
			log.info('[%s] First row elapsed: %s sec/%s min' % (self.cln, sec, round(sec/60, 2)))
			self.first_row=False
		return self.fh.readline()
	def _read(self, *args, **kwargs):
		sec=round((time.time() - self.start_time),2)
		log.info('[%s] First row elapsed: %s sec/%s min' % (self.cln,sec, round(sec/60, 2)))
	def write(self, data, *args, **kwargs):
		pass
	def reset(self):
		self.cnt=0
	def __enter__(self):
		return self
	def close(self):
		self.fh.close()
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass
