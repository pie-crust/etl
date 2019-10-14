import time, logging
from include.utils import ctimeit
log=logging.getLogger('cli')

class DataStreamer:
	@ctimeit
	def __init__(self, cli, data):
		self.cli = cli
		self.data = data
		assert isinstance(data, list)
		self.cln=self.__class__.__name__
		log.debug('Created %s' % self.cln)
		self.start_time = time.time()
		self.first_row=True
		self.cln=self.__class__.__name__
		self.rid=-1
		
	def _fetchone(self, *args, **kwargs):
		if self.fh.closed:
			return None
		else:
			row=self.readline()
			if row:
				return row.strip().split(self.cli.csep)
			else:
				return None


	def readline(self):
		if self.first_row: 
			log.info('[%s] First row elapsed: %s sec' % (self.cln, round((time.time() - self.start_time),2)))
			self.first_row=False
		self.rid +=1
		#print self.cln, 'line: ', self.rid
		if self.rid>len(self.data)-1:
			return None
		else:
			return self.data[self.rid]
	def _read(self, *args, **kwargs):
		return os.linesep.join([self.cli.csep.join (row) for row in self.data])
	def write(self, data, *args, **kwargs):
		pass
	def reset(self):
		self.cnt=0
	def __enter__(self):
		return self
	def close(self):
		pass
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass