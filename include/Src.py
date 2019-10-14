from collections import OrderedDict
class Src(object):
	def __init__(self):
		opt=None
		self.src=OrderedDict()
		self.actors=None
		self.sources={}
		self.csources={}
		self.flow=[]
		self.aclass=None
		self.init={}
	def add_c_call(self, cln, func, args, code):
		if cln not in self.csources:
			self.csources[cln]= []
		self.csources[cln].append([func, args, code])
			
		#self.init[cln]=args
	def add_call(self, key, code, args):
		if key not in self.sources:
			self.sources[key]= code
		self.flow.append([key,args])
	def show(self):
		assert self.actors
		print ('#'*40);	print('#actors');print ('#'*40);
		for k,v in self.actors.items():
			print '%s as %s' % (v,k)
		print ('#'*40);	print('#flow');print ('#'*40);
		for i in self.flow:
			k, v= i
			print '%s()' % (k)
		assert self.aclass
		print ('#'*40);	print('#methods');print ('#'*40);
		for k,v in self.aclass.items():
			#print(v)
			print '%s.%s' % (k,str(v[0].__name__))
		print ('#'*40);	print('#class calls');print ('#'*40);
		for k in self.csources:
			for kk in self.csources[k]:
				print '%s.%s()' % (k, kk[0])