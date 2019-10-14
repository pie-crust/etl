from __future__ import print_function
import os, sys
from include.fmt import psql, pfmtd
import subprocess, logging

e=sys.exit
log=logging.getLogger('loader')

class SimpleNamespace (object):
	def __init__ (self, **kwargs):
		self.__dict__.update(kwargs)
	def __repr__ (self):
		keys = sorted(self.__dict__)
		items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
		return "{}({})".format(type(self).__name__, ", ".join(items))
	def __eq__ (self, other):
		return self.__dict__ == other.__dict__
		
def get_cli(a, ):
	cfg 	= 'config/db_config.%s.json' % a.runtime_env
	cloc	= 'config/proc/position/%s' % wflow
	assert os.path.isfile (cfg), 'Db config file does not exists.'
	assert os.path.isdir (cloc), 'Pileline dir does not exists.'
	return 'time %s cli.py -nopp {PARAM_CNT} {DUMP} -dcf %s -pcf %s/{TABLE}.json {LAME_DUCK} --proc_params' % (PY, cfg, cloc)
def load_day(a, mon, day=None):
	cli= get_cli(a)
	pars = params[a.table][0].format( **dict( CENTER = a.center, CLIENT = a.client, YEAR = a.year, MONTH = mon, DAY = day, EOM = a.day_to,  BUNIT= a.bunit ))

	pycli  = cli.format(**dict( TABLE = a.table, PARAM_CNT = len([p for p in pars.strip().split(' ') if p]), DUMP = '--dump' if a.dump else '--no-dump', LAME_DUCK='-ld %d ' % a.lame_duck))
	cmd= '%s %s' % (pycli, pars)
	
	if not a.dry:
		pfmtd([dict(Command=os.linesep.join(cmd.split()))], a.table)
		pipe=subprocess.Popen([cmd], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
		
		line= pipe.stdout.readline()
		
		while line: 
			print ('OUTPUT:', line.strip())
			line= pipe.stdout.readline()
		
		line= pipe.stderr.readline()
		
		while line:
			print ('ERROR:', line)
			line= pipe.stderr.readline()

		while pipe.poll() is None:
			print ('Waiting...')
			time.sleep(1)
			
		if pipe.returncode != 0:
			print('returncode = %d' % pipe.returncode)
			e(pipe.returncode)
	else:
		print (cmd)