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

class DbStreamer:

	def __init__(self, cli, cur, start_time):
		self.cli = cli
		self.cur = cur
		self.cln=self.__class__.__name__
		log.debug('Created %s' % self.cln)
		self.start_time = start_time
		self.first_row=True
		self.description= self.cur.description
	def readline(self, *args, **kwargs):
		colsep=kwargs.get('colsep', '|')
		dbrow = self.fetchone(*args, **kwargs)
		return colsep.join([str(c) for c in list(dbrow)]) if dbrow else None
	def fetchone(self, *args, **kwargs):
		if self.first_row: 
			sec=round((time.time() - self.start_time),2)
			log.info('First row elapsed: %s sec/%s min' % (sec, round(sec/60, 2)))
			self.first_row=False	
		return self.cur.fetchone(*args, **kwargs)
	@ctimeit
	def fetchall(self, *args, **kwargs):
		if self.first_row: 
			sec=round((time.time() - self.start_time),2)
			log.info('First row elapsed: %s sec/%s min' % (sec, round(sec/60, 2)))
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
	