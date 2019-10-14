
class MockStreamer:

	def __init__(self, cli, data):
		self.cli = cli
		self.data = data
		assert isinstance(data, list)
		self.cln=self.__class__.__name__
		log.debug('Created %s' % self.cln)
		self.start_time = time.time()
		self.first_row=True

	def fetchone(self, *args, **kwargs):
		if not self.data:
			return None
		else:
			return self.data.pop()


	def readline(self):
		if self.first_row: 
			sec=round((time.time() - self.start_time),2)
			log.info('[%s] First row elapsed: %s sec/%s min' % (self.cln,sec, round(sec/60, 2)))
			self.first_row=False
		return str(self.cli.csep.decode()).join(self.data.pop())


	def _read(self, *args, **kwargs):
		return os.linesep.join([self.cli.csep.join (row) for row in self.cur.fetchall()])
	def write(self, data, *args, **kwargs):
		pass
	def reset(self):
		self.cnt=0
	def __enter__(self):
		return self
	def close(self):
		del self.data
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass