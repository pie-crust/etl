"""
Usage:
#DY
time python tools/loader/position/iq_proc_dir_iq.py -t DY_Position_TD -yr 2019 -mf 8 -mt 8 -cl 223906 -df 30 -dt 30 -cr DESK  -bu CEFL -ld 33

#ME
time python tools/loader/position/iq_proc_dir_iq.py -t ME_Position_TD -yr 2019 -mf 1 -mt 1 -cl 223906  -cr DESK   -ld 30

time python tools/loader/position/iq_proc_dir_iq.py -t ME_Position_TD -yr 2019 -mf 1 -mt 1 -cl 223906  -cr ACCT


time python tools/loader/position/iq_proc_dir_iq.py -t DY_Position_SD -yr 2019 -mf 8 -mt 8 -cl 223906 -df 30 -dt 30 -cr DESK  -rte PROD  -ld 37

time python tools/loader/position/iq_proc_dir_iq.py -t ME_Position_SD -yr 2019 -mf 8 -mt 8 -cl 223906  -cr ACCT

"""

from __future__ import print_function


import os, sys, time
sys.path.append("../../../")
sys.path.append("../../../../")
sys.path.append("../../../../../")
sys.path.append("../../")
sys.path.append("../")

try:
	import __builtin__ as builtins
except:
	import builtins
home = os.path.dirname(sys.argv[0])
if not home or not home.strip('.'):
	home = os.path.dirname(os.path.abspath(__file__))

app_name = os.path.basename(os.path.splitext(__file__)[0])
	
from pprint import pprint as pp

import subprocess, logging

import click
click.disable_unicode_literals_warning = True

builtins.home=home
builtins.app_name=app_name 
from common.fmt import psql, pfmtd
import traceback
try:
	import cStringIO
except ImportError:
	import io as cStringIO
	
e=sys.exit
def show():
	global cursor
	try:
		for row in cur.fetchall():
			print(row)
			
	except Exception as ex:
		print (str(ex))
		print ('nothing o show')

SUCCESS=0

PY2	= '~/python27/bin/python'
PY3	= '~/python3/bin/python3'
PY  = PY3
params={}



params[ 'RC_Balance_Cash' ]		 = [ " '{YEAR}/{MONTH}/{DAY}' {TOCKEN} " ]


class SimpleNamespace (object):
	def __init__ (self, **kwargs):
		self.__dict__.update(kwargs)
	def __repr__ (self):
		keys = sorted(self.__dict__)
		items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
		return "{}({})".format(type(self).__name__, ", ".join(items))
	def __eq__ (self, other):
		return self.__dict__ == other.__dict__

mm=[31,28,31,30,31,30,31,31,30,31,30, 31]

center = ['DESK', 'ACCT']

def get_cli(a):

	wflow =os.path.splitext(os.path.basename(__file__))[0]
	cfg 	= 'config/db_config.%s.json' % a.runtime_env
	cloc	= 'config/proc/position/%s' % wflow

	return 'time %s cli.py -nopp {PARAM_CNT} -dcf %s -pcf %s/{TABLE}.json  -rte {RUNTIME} --proc_params' % (PY, cfg, cloc)
	
@click.command()
@click.option('-t',  '--table',			default = None, type=str, help = 'Table name.', 								required=True )
@click.option('-yr', '--year',			default = None, type=int, help = 'Load year.', 									required=True )
@click.option('-mf', '--month_from',	default = None, type=int, help = 'Month from.', 								required=True )
@click.option('-mt', '--month_to',  	default = None, type=int, help = 'Month to.', 									required=True )
@click.option('-df', '--day_from', 		default = '', 	type=str, help = 'Day from.', 									required=True )
@click.option('-dt', '--day_to',   		default = '', 	type=str, help = 'Day to.', 									required=True )
@click.option('-tk', '--tocken',   		default = '', 	type=str, help = 'Tocken.', 									required=True )
@click.option('-rte', 	'--runtime_env',default = 'DEV',help='Runtime.' ) # DEV/UAT/PROD
@click.option('--dry',	 				default = False, is_flag=True, help="Dry run.", 								required=False)

def main(**kwargs):

	pp(kwargs)

	a = SimpleNamespace(**kwargs)
	print (a.dry)
	cgroup = ['RC_Balance_Cash']
	
	if a.table in cgroup:
		assert a.month_from in list(range(1,13))
		assert a.month_to 	in list(range(1,13))
		mon = a.month_from
		if a.day_to in ['eom']:
			a.day_to=mm[mon-1]
		if a.table in cgroup_dy:
			assert a.month_from == a.month_to
			

			for day in range(int(a.day_from),  int(a.day_to)+1):
				load_day(a, mon, day)
	else:
		raise Exception ('Unsupported table [%s]' % a.table)


def load_day(a, mon, day=None):
	cli= get_cli(a)
	pars = params[a.table][0].format( **dict(  YEAR = a.year, MONTH = mon, DAY = day, TOCKEN = a.tocken,  EOM = a.day_to))

	pycli  = cli.format(**dict( TABLE = a.table, PARAM_CNT = len([p for p in pars.strip().split(' ') if p]),  RUNTIME=a.runtime_env))
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
			
		print("retcode =", pipe.returncode)
	else:
		print (cmd)

log=logging.getLogger('loader')

if __name__ == "__main__":
	try:
		main()
		sys.exit(SUCCESS)
	except Exception as ex:
		err_log = cStringIO.StringIO()
		traceback.print_exc(file=err_log)
		error = err_log.getvalue()
		if 1:
			print ('#' * 80)
			print ('ERROR while running cli')
			print ('#' * 80)
			if hasattr(log,'handler') and log.handler:
				log.error(error)
			else:
				print (error)
			print ('#' * 80)
			print ('#' * 80)

 




























