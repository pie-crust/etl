import os
import imp
import sys
import traceback
import importlib
import time
import logging
import tempfile
import warnings, itertools
#from pubsub import pub
import errno
try:
	import __builtin__ as builtins
except:
	import builtins
import yaml
import tokenize
from pprint import pprint as pp

e=sys.exit
import yaml

from functools import wraps
import smtplib
from email.mime.text import MIMEText
import requests
try:
	from requests_kerberos import HTTPKerberosAuth
except:
	#plug
	import os as HTTPKerberosAuth
log=logging.getLogger('cli')
import inspect

from types import FunctionType

def extract_wrapped(decorated):
	closure = (c.cell_contents for c in decorated.__closure__)
	return next((c for c in closure if isinstance(c, FunctionType)), None)
	
	
class folded_unicode(str): pass
class literal_unicode(str): pass

def folded_unicode_representer(dumper, data):
	return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='>')
def literal_unicode_representer(dumper, data):
	return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(folded_unicode, folded_unicode_representer)
yaml.add_representer(literal_unicode, literal_unicode_representer)

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

text_type = unicode if PY2 else str


def get_emails(env):

	if env.upper()=='PROD':
		to_email=os.getenv('SSRSSUPPORTEMAILS')
		assert to_email
		from_email=os.getenv('GAUSER')
		assert from_email
	
	elif env.upper()=='DEV':
		if home.startswith('/home/s_dev_racct/ab_'):
			local= 'oleksandr.buzunov@home.com'
			if local:
				from_email	=  local
				to_email  	=  local
		else:		
			from_email	= os.getenv('GAUSER')
			to_email  	= os.getenv('SSRSSUPPORTEMAILS')
	else:
		raise Exception('Unsupported runtime [%s]' % env)
	log.debug('From: %s from_email. To: %s' % (from_email, to_email))
	return from_email, to_email

class CliLoggingClass:
	def __init__(self, home, app_name, workflow, table_name):
		if 0:
			self.log = logging.Logger("cli")
			self.log.stream = sys.stderr
			self.log_handler = logging.StreamHandler(self.log.stream)
			self.log.addHandler(self.log_handler)
		
		pid = os.getpid()
		

		tmp_fn = next(tempfile._get_candidate_names())
		
		tmpdir =os.getenv('G3_TEMP_DIR', '/tmp')
		log_dir =os.path.join(tmpdir,app_name, workflow, table_name)
		latest_dir = os.path.join(log_dir, 'latest')
		ts = time.strftime('%Y%m%d_%H%M%S')
		ts_dir = os.path.join(log_dir, ts)
		if not os.path.exists(ts_dir):
			try:
				os.makedirs(ts_dir)
			except OSError as e:
				if e.errno != errno.EEXIST:
					raise
				else:
					pass
			
			
		DEBUG = 1
		
		FORMAT = '%(asctime)s|%(levelname)s|%(process)d|%(module)s.py|%(funcName)s|%(lineno)d|  %(message)s'
		lfile = os.path.join(ts_dir, '%s_%d_%s.log' % (app_name, pid, tmp_fn))

		logging.basicConfig(
			filename=lfile,
			level=logging.DEBUG,
			format=FORMAT,
			datefmt="%Y-%m-%d %H:%M")
			
		log = self.log= logging.getLogger('cli')
		#self.log.stream = sys.stderr
		#self.log_handler = logging.StreamHandler(sys.stderr)
		#self.log.addHandler(self.log_handler)
		if 1:
			log.handler = handler=logging.StreamHandler(sys.stdout)
			handler.setLevel(logging.DEBUG)
			formatter = logging.Formatter(FORMAT,datefmt="%Y-%m-%d %H:%M:%S")
			handler.setFormatter(formatter)
			#pprint(dir(handler))
			log.addHandler(handler)
		log.file_name=lfile
		if 0:
			logging.getLogger('boto3').setLevel(logging.WARNING)
			logging.getLogger('boto').setLevel(logging.WARNING)
			logging.getLogger('botocore').setLevel(logging.WARNING)
			logging.getLogger('nose').setLevel(logging.WARNING)
			logging.getLogger('s3transfer').setLevel(logging.WARNING)
			logging.getLogger('urllib3').setLevel(logging.WARNING)
			logging.getLogger('kerberos').setLevel(logging.WARNING)
		
		log.info('Log:'+lfile)

	def get_loggers(self):
		'''Return a list of the logger methods: (debug, info, warn, error)'''

		return self.log.debug, self.log.info, self.log.warn, self.log.error

if 1:
	cli_logging = CliLoggingClass(home, app_name, workflow, table_name)
	debug, info, warn, error = cli_logging.get_loggers()


def log_calls(func):
	'''Decorator to log function calls.'''
	def wrapper(*args, **kargs):
		callStr = "%s(%s)" % (func.__name__, ", ".join([repr(p) for p in args] + ["%s=%s" % (k, repr(v)) for (k, v) in list(kargs.items())]))
		debug(">> %s", callStr)
		ret = func(*args, **kargs)
		debug("<< %s: %s", callStr, repr(ret))
		return ret
	return wrapper

def ctimeit(method):
	@wraps(method)
	def timed(*args, **kw):
		
		#if 'log' in __builtins__:
		log.debug('Entering: %s.%s' % ( args[0].__class__.__name__,method.__name__))
		ts = time.time()
		result = method(*args, **kw)
		te = time.time()
		#if 'log' in dir(__builtins__):
		#if 'log' in __builtins__:
		log.debug('Exiting %s.%s, time: %s sec' % (args[0].__class__.__name__, method.__name__, round((te -ts),2)))
		
		return result
	return timed
						
def timeit(method):
	def timed(*args, **kw):
		#if 'log' in __builtins__:
		log.debug('Entering: %s' % ( method.__name__))
		ts = time.time()
		result = method(*args, **kw)
		te = time.time()
		#if 'log' in dir(__builtins__):
		#if 'log' in __builtins__:
		log.debug('Exiting %s, time: %s sec' % ( method.__name__, round((te -ts),2)))
		
		return result
	return timed
	
class Security(object):
	def __init__(self):
		pass
	@ctimeit
	def create_keys(self):
		created=False
		SUCCESS=200
		if 1:
			
			response = requests.post('https://datakeep.homegroup.com/api/v2/create_access_credentials', auth=HTTPKerberosAuth())
			
			if response.status_code == SUCCESS:
				created=True
			else:
				log.warn(clierr.E_CREATE_AWS_KEYS_FAILED[0])
				created=False
			
		return created
		
	def create_aws_keys(self):
		if not self.create_keys():
			for x in range(3):
				log.warn('create_aws_keys: Try #%d ...' % (x+2))
				time.sleep(60)
				if self.create_keys(): break;
			raise Exception(clierr.E_CREATE_AWS_KEYS_FAILED[0])
		
	@ctimeit
	def get_aws_keys(self, max_tries):
		SUCCESS=200
		data = None
		tries=0
		assert max_tries
		url='https://datakeep.homegroup.com/api/v2/get_access_credentials'
		while not data:
			res = requests.get(url, auth=HTTPKerberosAuth())
			
			if res.status_code == SUCCESS:
				try:
					data = res.json()[0]
				except IndexError as ex:
					log.warn('Json data is empty: [%s]' % res.json())
					log.warn('Creating keys so we can retry.')
					
					self.create_aws_keys()
					res2 = requests.get(url, auth=HTTPKerberosAuth())
					if res2.status_code == SUCCESS:
						try:
							data = res2.json()[0]
						except IndexError as ex:
							log.error('Json data is empty after key recreate: [%s]' % res2.json())
							raise Exception(clierr.E_GET_AWS_KEYS_EMPTY_JSON[0])
				length = len(data)
				access_key_id= data.get('access_key_id')
				secret_access_key= data.get('secret_access_key')
				return access_key_id, secret_access_key
				
			tries +=1
			if tries<max_tries: 
				log.info('get_aws_keys: Try [%d]' % tries)
				time.sleep(1)
			else: 
				return None, None
			
		return None, None
		
awscreds=Security()
class InOut(object):
	def __init__(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)
class CliErr(object):
	def __init__(self):
		self.E_FAILURE			 = ['Script failed', 		1]
		self.E_UKNOWN_ERROR		 = ['Unknown error', 		2]
		self.E_UNHANDLED		 = ['Unhandled error', 		3]
		self.E_WRONG_PARAM_FORMAT= ['Wrong param format:',	4]
		self.E_WRONG_PARAM_COUNT = ['Wrong param format:',	13]
		#IQ
		self.E_SYSTEM_TEMP_NOSPACE	= ['You have run out of space in IQ_SYSTEM_TEMP DBSpace',	5]
		self.E_CONNECTION_TERMINATED= ['Connection was terminated', 6]
		self.E_EMPTY_SOURCE_PIPE 	= ['Source pipe is empty', 7]
		
		#AWS
		self.E_CREATE_AWS_KEYS_FAILED 	= ['Create AWS keys failed after 4 tries.', 8]
		self.E_GET_AWS_KEYS_FAILED 		= ['Cannot get AWS credentials. Too many tries.', 9]
		self.E_GET_AWS_KEYS_EMPTY_JSON 	= ['Json data is empty.', 10]
		
		#Snowflake
		self.E_AUTH_TOKEN_EXPIRED 		= ['Authentication token has expired.  The user must authenticate again.',	11]
		self.E_STAGE_ACCESS_FORBIDDEN 	= ['Failure using stage area. Cause: [Forbidden (Status Code: 403; Error Code: 403 Forbidden)]', 12]
		

		
		
		
	
	def  get_exit_id(self, e):
		for ename in [en for en in dir(self) if en.startswith('E_')]:
			e_err=getattr(self, ename)
			if e_err[0] in str(e):
				return e_err[1]
		else:
			return self.E_UKNOWN_ERROR[1]
clierr=CliErr()
def send_crash_email(sender,receiver,subject,message):	
	msg = MIMEText(message)
	msg['Subject'] = subject
	msg['From'] = sender
	#msg['To'] = receiver
	for rcp in receiver.split(','):
		msg.add_header('To',rcp)

	s = smtplib.SMTP('mailrelay.homegroup.com')

	s.sendmail(sender, msg.get_all('To'), msg.as_string())

def get_log_for_email(logfn, levels=['INFO']):
	if logfn and logfn:
		lll=open(log.file_name, 'rb').read().split(os.linesep)
		b = [6,]

		ll= [x.split('|')[6].strip() for x in lll if x and any('|%s|' % level in x for level in levels)]
		return [x for x in ll if not x.strip().startswith('Entering') and not x.strip().startswith('Exiting')]
def gsource(method):
	def source(*args, **kw):
		if 'src' in __builtins__:
			log.debug('SRC:Entering: %s' % ( method.__name__))
			
			src.add_call(key=method.__name__, code=inspect.getsource(method),args=(args, kw))
		result = method(*args, **kw)
		
		
		if 'src' in __builtins__:
			log.debug('SRC:Exiting %s' %  method.__name__)
		
		return result
	return source

def csource(method):
	@wraps(method)
	def source(*args, **kw):
		#print(435525, args[0].__class__.__name__)
		if 'src' in __builtins__:
			log.debug('CSRC: Entering: %s.%s' % ( args[0].__class__.__name__,method.__name__))
			src.add_c_call(cln=args[0].__class__.__name__,func=method.__name__, args=(args, kw), code=inspect.getsource(method))
				
		result = method(*args, **kw)
		
		
		if 'src' in __builtins__:
			log.debug('CSRC: Exiting %s.%s' % (args[0].__class__.__name__, method.__name__))
		
		return result
	return source
	
def api(method):
	@wraps(method)
	def timed(*args, **kw):
		print ('-'*80);print ('-'*80)
		print ('Executing %s:%s' %  ( args[0].__class__.__name__,method.__name__))
		print ('-'*80);print ('-'*80)
		result = method(*args, **kw)
		return result
	return timed




	
class slogger(object):
	def __init__(self, func):
		self.func = func
	def __get__(self, obj, type=None):
		return self.__class__(self.func.__get__(obj, type))
	def __call__(self, *args, **kw):
		if 'log' in __builtins__:
			log.debug('Entering: %s' % self.func)
		return self.func(*args, **kw)
	def __exit__(self, *args, **kw):
		if 'log' in __builtins__:
			log.debug('Exiting: %s' % self.func)
		return None
		
def formatExceptionInfo(maxTBlevel=5):
	cla, exc, trbk = sys.exc_info()
	excName = cla.__name__
	try:
		excArgs = exc.__dict__["args"]
	except KeyError:
		excArgs = "<no args>"
	excTb = traceback.format_tb(trbk, maxTBlevel)
	return (excName, excArgs, excTb)

def create_symlink(from_dir, to_dir, home):
	global log
	os.chdir(home)

	if (os.name == "posix"):

		os.symlink(from_dir, to_dir)
	elif (os.name == "nt"):
		from subprocess import Popen, PIPE, STDOUT

		wget = Popen(('mklink /J %s %s' % (to_dir, from_dir)).split(' '), stdout=PIPE, stderr=STDOUT, shell=True)
		stdout, nothing = wget.communicate()
		log.info(stdout, extra=d)

	else:
		log.error('Cannot create symlink on this OS.', extra=d)

def unlink(dirname):
	if (os.name == "posix"):
		os.unlink(dirname)
	elif (os.name == "nt"):
		try:
			os.rmdir( dirname )
		except:
			pass
	else:
		log.error('Cannot unlink. Unknown OS.', extra=d)


def load_module(fn,app_init):
	builtins.app_init=app_init
	return import_module_2(fn)

ll={}
def load_actor(**kwargs):
	aname = kwargs.get('aname')
	atype = kwargs.get('atype')
	app_init = kwargs.get('app_init')
	type_name=aname
	assert type_name
	afn=os.path.join('include',atype, '%s.py' % type_name)  
	
	actor=load_module(fn=afn,app_init=app_init)
	try:
		api = getattr(actor, type_name)
	except:
		log.error('Cannot load actor [%s] from file [%s]' % (aname, afn))
		raise
	kwargs.update(dict(env=aname,cli=app_init[0], conn_pool=app_init[1]))
	return api(**kwargs)

def create_reader(**kwargs):
	kwargs.update(dict(atype =  'extractor'))
	return load_actor(**kwargs)

def create_writer(**kwargs):
	kwargs.update(dict(atype =  'loader'))
	return load_actor(**kwargs)
	
def create_actor(**kwargs):
	kwargs.update(dict(atype =  ''))
	return load_actor(**kwargs)
	
def load_module_1(aclass, flow, name, app_init):
	val = flow["actors"][name]
	
	abspath=os.path.abspath(os.path.dirname(sys.argv[0]))
	apath=[abspath]+val.split('.')
	actor_file = os.path.join(*apath)	
	actor_mname,_ = os.path.splitext(os.path.split(actor_file)[-1])		
	builtins.app_init=app_init
	afile= '%s.py' % actor_file
	assert os.path.isfile(afile), 'File for "%s" module does not exists:\n%s' % (name, afile)
	#pp(flow)
	#e()
	amodule=import_module_2(afile)
	aclass[name]=[getattr(amodule,actor_mname),actor_mname]

def import_modul_3(module_name, file_path):

	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	if 1:
		sys.modules[module_name] = module
	return module
def import_module_2(filepath):
	class_inst = None
	#expected_class = 'MyClass'
	#print filepath , 555
	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		#print (mod_name, filepath)
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)
	return py_mod
	
def load_PY_file(dml_file):

	assert os.path.isfile(dml_file), '"%s" is not a file' % dml_file
	dml = import_module(os.path.basename(dml_file), dml_file)
	return dml


class YamlModule(object):
	def __init__(self):
		pass

def load_YAML_file(dml_file):
	assert os.path.isfile(dml_file), '"%s" is not a file' % dml_file
	dml=None
	#print(dml_file)
	with open(dml_file, 'rb') as stream:
		dml = yaml.load(stream)
		#pprint(dml); e(0)
		out=YamlModule()
		for k,v in dml.items():
			setattr(out,k,v)
		return out






def print_trace(tr):
	for l in  tr.split(os.linesep): print(l)
	
	



def unicode2utf8(arg):
	"""
	Only in Python 2. Psycopg2 expects the args as bytes not unicode.
	In Python 3 the args are expected as unicode.
	"""

	if PY2 and isinstance(arg, unicode):
		return arg.encode('utf-8')
	return arg


def utf8tounicode(arg):
	"""
	Only in Python 2. Psycopg2 returns the error message as utf-8.
	In Python 3 the errors are returned as unicode.
	"""

	if PY2 and isinstance(arg, str):
		return arg.decode('utf-8')
	return arg
def html_mail():
	if 0:
		if 1:
			from email.mime.multipart import MIMEMultipart
			from email.mime.text import MIMEText
			msg = MIMEMultipart('alternative')
			msg['Subject'] = "IQ->Snowflake[%s][%s]." % (proc_key,','.join(pa))
			msg['From'] = ecfg.from_email
			msg['To'] 	= ecfg.to_email

			# Create the body of the message (a plain-text and an HTML version).
			text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
			html = """
			<html>
			  <head>
			  <style type="text/css" media="screen">
	
	table{
		background-color: white;
		empty-cells:hide;
		font-size: 14px;
		color: #111111;
		line-height: 1.4;		
		border-bottom: 2px solid #f2f2f2;
		border:2px solid #f2f2f2;

	}

tr.border_bottom {
	border:2px solid #f2f2f2;
	
}
tr.oddrow {
	display: block;
	border-bottom: 1px solid #F00;
}
			  </style>
			  </head>
			  <body>
				<table border="0"><tr><td nowrap >%s</table
			  </body>
			</html>
			""" % '<tr><td nowrap>'.join(ll)

			# Record the MIME types of both parts - text/plain and text/html.
			part1 = MIMEText(text, 'plain')
			part2 = MIMEText(html, 'html')

			# Attach parts into message container.
			# According to RFC 2046, the last part of a multipart message, in this case
			# the HTML message, is best and preferred.
			msg.attach(part1)
			msg.attach(part2)
			p = Popen(ecfg.sendmail, stdin=PIPE)
			if 1:
				p.communicate(msg.as_string())
				stdout, stderr = p.communicate()
				if stdout: log.info('Sendmail: %s', stdout)
				if stderr: log.error('Sendmail: %s', stderr)
			log.info('Email sent.')
			