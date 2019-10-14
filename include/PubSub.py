import itertools
from pubsub import pub
counter=itertools.count()

def NewId():
	return counter.next()

def send(*args, **kwargs):
	pub.sendMessage(*args, **kwargs)
	
def Exec(topic, **kwargs):
	send(topic, msg=topic, extra=kwargs)
	return NewId()
	
	
class PubSub:
	def __call__(self, **kwargs):
		cln=self.__class__.__name__
		print cln
		msg= kwargs.get('msg')
		topic, subtopic = msg.split('.')
		assert topic
		assert subtopic
		if topic in [cln]:
			if hasattr(self, subtopic):
				print('Sub-Topic [%s]: ' % subtopic, kwargs)
				print 'Processing:', subtopic
				api=getattr(self, subtopic)
				api()
			else:
				print('%s: PASSING: Subtopic [%s]: ' % (cln, subtopic), kwargs)
		else:
			print('%s: PASSING: Topic [%s]: ' % (cln, topic), kwargs)	