
def timeit(method):
	def timed(*args, **kw):
		log.info('Entering: %s' % ( method.__name__))
		ts = time.time()
		result = method(*args, **kw)
		te = time.time()
		log.info('Exiting %s, time: %s sec' % ( method.__name__, round((te -ts),2)))
		
		return result
	return timed