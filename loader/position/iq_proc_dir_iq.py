"""
Usage:
#DY
time python tools/loader/position/iq_proc_dir_iq.py -t DY_Position_TD -yr 2019 -mf 8 -mt 8 -cl 223906 -df 1 -dt eom -cr DESK  -bu CEFL -ld 37

#ME
time python tools/loader/position/iq_proc_dir_iq.py -t ME_Position_TD -yr 2019 -mf 1 -mt 1 -cl 223906  -cr DESK   -ld 30

time python tools/loader/position/iq_proc_dir_iq.py -t ME_Position_TD -yr 2019 -mf 1 -mt 1 -cl 223906  -cr ACCT


"""

from __future__ import print_function


import os, sys, time
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
from include.fmt import psql, pfmtd
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



params[ 'DY_Position_SD' ]		 = [ '{CLIENT} {YEAR}/{MONTH}/{DAY} "EOD" "{CENTER}" "{BUNIT}" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" ' ]


params[ 'ME_Position_SD' ]		 = [ '{CLIENT} {YEAR}/{MONTH}/{EOM} "EOD" "{CENTER}" "{BUNIT}" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" ' ]

params[ 'DY_FinancingPosition' ] = [ '{CLIENT} {YEAR}/{MONTH}/{DAY} {YEAR}/{MONTH}/{DAY} EOD EOD "*" "*" "*" NONE "*" NOW 0' ]
params[ 'ME_FinancingPosition' ] = [ '{CLIENT} {YEAR}/{MONTH}/01 {YEAR}/{MONTH}/{EOM} EOD EOD "*" "*" "*" NONE "*" NOW 0' ]

params[ 'ME_13F' ]				 = [ '{YEAR}/{MONTH}/{EOM} {CLIENT} "EOD" "*" "0" "ALL" "DETAIL" "*" 0 "N" "N" "N"'] 

params[ 'DY_Position_TD' ]		 = [ '{CLIENT} "EOD" {YEAR}/{MONTH}/{DAY} "{CENTER}" "{BUNIT}" "DEFAULT" "REGULAR" "1" "0" "NONE" "*" "*" "N" "0" "0" "NONE" "NONE" "ALL" "0" "MONTH_END" "N" "ALL" "*" "0" "*" "N" "*" ' ]
params[ 'ME_Position_TD' ]		 = [ '{CLIENT} "EOD" {YEAR}/{MONTH}/{EOM} "{CENTER}" "{BUNIT}" "DEFAULT" "REGULAR" "1" "0" "NONE" "*" "*" "N" "0" "0" "NONE" "NONE" "ALL" "0" "FULL"      "N" "ALL" "*" "0" "*" "Y" "*" ' ]

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

	return 'time %s cli.py -nopp {PARAM_CNT} {DUMP} -dcf %s -pcf %s/{TABLE}.json {LAME_DUCK} --proc_params' % (PY, cfg, cloc)
@click.command()
@click.option('-t',  '--table',			default = None, type=str, help = 'Table name.', 								required=True )
@click.option('-yr', '--year',			default = None, type=int, help = 'Load year.', 									required=True )
@click.option('-mf', '--month_from',	default = None, type=int, help = 'Month from.', 								required=True )
@click.option('-mt', '--month_to',  	default = None, type=int, help = 'Month to.', 									required=True )
@click.option('-df', '--day_from', 		default = '', 	type=str, help = 'Day from.', 									required=True )
@click.option('-dt', '--day_to',   		default = '', 	type=str, help = 'Day to.', 									required=True )
@click.option('-cl', '--client',   		default = None, type=int, help = 'Client id.', 									required=True )
@click.option('-cr', '--center',   		default = '', 	type=str, help = 'Center.', 									required=True )
@click.option('-bu', '--bunit', 		default = '*', 	type=str, help = 'Business unit.', 								required=True )
@click.option('-rte', 	'--runtime_env',default = 'DEV',help='Runtime.' ) # DEV/UAT/PROD
@click.option('--dump', 				default = False, is_flag=True, help="Dump input stream to file.", 				required=False)
@click.option('--dry',	 				default = False, is_flag=True, help="Dry run.", 								required=False)
@click.option('-ld', '--lame_duck', 	default = 0,	type=int, help="Limit IQ streamer output to this row count.", 	required=False)
def main(**kwargs):

	pp(kwargs)

	a = SimpleNamespace(**kwargs)
	print (a.dry)
	cgroup_dy = ['DY_Position_SD', 'DY_Position_TD']
	cgroup_me = ['ME_Position_SD', 'ME_Position_TD']
	if a.table in cgroup_dy + cgroup_me:
		assert a.center,	'Center must be in %s' % center
		assert a.center in center,	'Center must be in %s' % center
		#= 'DESK'
		assert a.month_from in list(range(1,13))
		assert a.month_to 	in list(range(1,13))
		mon = a.month_from
		if a.day_to in ['eom']:
			a.day_to=mm[mon-1]
		if a.table in cgroup_dy:
			assert a.month_from == a.month_to
			

			for day in range(int(a.day_from),  int(a.day_to)+1):
				load_day(a, mon, day)
		if a.table in cgroup_me:
			assert not a.day_from,  'Remove "-df"'
			assert not a.day_to, 	'Remove "-dt"'
			for mon in range(a.month_from, a.month_to+1):
				a.day_to=mm[mon-1]
				load_day(a, mon)
	


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
	if 0:
		#clid	= 223907
		#day		= 31
		#mon		= 5
		year	= 2019
		center	= 'ACCT'
		ld		= 0

		b_unit = 'CEFL'
		#load_day('ME_FinancingPosition',223906, 2019, 2, day, center)
		if 0:
			for mon in range(1,8):					
				day =mm[mon-1]
				for clid in [223906, 223907]:
					for table in params:
						#	print ('#',table)
						if  table in ['DY_FinancingPosition', 'ME_FinancingPosition','ME_13F']:
							load_day(table,clid, year, mon, day, center,  bunit=b_unit)
		if 1:
			if 0:
				year	= 2019
				mon 	= 1
				day 	= mm[mon-1]
				for clid in [223906, 223907]:
					for table in ['ME_FinancingPosition']:
							load_day(table,clid, year, mon, day, center,  bunit=b_unit)
			if 1:
				mon =1 
				eom =mm[mon-1]
				for clid in [223906, 223907]:
					for table in ['DY_FinancingPosition']:
						for day in range(1, eom+1):
							load_day(table,clid, year, mon, day, center,  bunit=b_unit)
							#e()

		if 0:
			if 0:
				center	= 'ACCT'
				year	= 2019
				mon 	= 1
				day 	= mm[mon-1]
				b_unit 	= 'CEFL'
				for clid in [223906, 223907]:
					for  table in [ 'ME_Position_TD']: #['DY_FinancingPosition', 'ME_FinancingPosition','ME_13F']:
						load_day(table,clid, year, mon, day, center,  bunit=b_unit)
			if 1:
				center	= 'ACCT'
				year	= 2019
				mon 	= 1
				eom 	= mm[mon-1]
				b_unit 	= 'CEFL'
				for clid in [223906, 223907]:
					for day in range(1, eom+1):
						for  table in [ 'DY_Position_TD']: #['DY_FinancingPosition', 'ME_FinancingPosition','ME_13F']:
							load_day(table,clid, year, mon, day, center,  bunit=b_unit)
					
		if 0:
			center	= 'DESK'
			for mon in range(1,8):
				day =mm[mon-1]
				for clid in [223906, 223907]:
					for table in params:
						#	print ('#',table)
						if  table in ['DY_Position_SD' , 'ME_Position_SD', 'DY_Position_TD', 'ME_Position_TD']: #['DY_FinancingPosition', 'ME_FinancingPosition','ME_13F']:
							load_day(table,clid, year, mon, day, center,  bunit=b_unit)
							#ld +=11
							
							#ld +=11
		if 0:
			if 0:
				center	= 'ACCT'
				for mon in range(1,8):
					day =mm[mon-1]
					for clid in [223906, 223907]:
						for table in params:
							#	print ('#',table)
							if  table in ['DY_Position_SD' , 'ME_Position_SD', 'DY_Position_TD', 'ME_Position_TD']: #['DY_FinancingPosition', 'ME_FinancingPosition','ME_13F']:
								load_day(table,clid, year, mon, day, center,  bunit=b_unit)
			if 0:
				center	= 'DESK'
				for mon in range(1,8):
					day =mm[mon-1]
					for clid in [223906, 223907]:
						for table in params:
							#	print ('#',table)
							if  table in ['DY_Position_SD' , 'ME_Position_SD', 'DY_Position_TD', 'ME_Position_TD']: #['DY_FinancingPosition', 'ME_FinancingPosition','ME_13F']:
								load_day(table,clid, year, mon, day, center,  bunit=b_unit)
								#ld +=11


 




























