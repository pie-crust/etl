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

import subprocess

builtins.home=home
builtins.app_name=app_name 
from include.fmt import psql, pfmtd
	
	
	
e=sys.exit
def show():
	global cursor
	try:
		for row in cur.fetchall():
			print(row)
			
	except Exception as ex:
		print (str(ex))
		print ('nothing o show')
params={}
py2='~/python27/bin/python'
py3='~/python3/bin/python3'
rte='DEV'
wflow='iq_proc_dir_iq'
cfg = 'config/db_config.%s.json' % rte
cloc='config/proc/position/%s' % wflow

cli= 'time %s cli.py -nopp {PARAM_CNT} --dump -dcf %s -pcf %s/{TABLE}.json {LAME_DUCK} --proc_params' % (py3, cfg, cloc)

params[ 'DY_Position_SD' ]		 = [ '{CLIENT} {YEAR}/{MONTH}/{DAY} "EOD" "{CENTER}" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" ' ]


params[ 'ME_Position_SD' ]		 = [ '{CLIENT} {YEAR}/{MONTH}/{EOM} "EOD" "{CENTER}" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" ' ]

params[ 'DY_FinancingPosition' ] = [ '{CLIENT} {YEAR}/{MONTH}/{DAY} {YEAR}/{MONTH}/{DAY} EOD EOD "*" "*" "*" NONE "*" NOW 0' ]
params[ 'ME_FinancingPosition' ] = [ '{CLIENT} {YEAR}/{MONTH}/01 {YEAR}/{MONTH}/{EOM} EOD EOD "*" "*" "*" NONE "*" NOW 0' ]

params[ 'ME_13F' ]				 = [ '{YEAR}/{MONTH}/{EOM} {CLIENT} "EOD" "*" "0" "ALL" "DETAIL" "*" 0 "N" "N" "N"'] 

params[ 'DY_Position_TD' ]		 = [ '{CLIENT} "EOD" {YEAR}/{MONTH}/{DAY} "{CENTER}" "{BUNIT}" "DEFAULT" "REGULAR" "1" "0" "NONE" "*" "*" "N" "0" "0" "NONE" "NONE" "ALL" "0" "MONTH_END" "N" "ALL" "*" "0" "*" "N" "*" ' ]
params[ 'ME_Position_TD' ]		 = [ '{CLIENT} "EOD" {YEAR}/{MONTH}/{EOM} "{CENTER}" "{BUNIT}" "DEFAULT" "REGULAR" "1" "0" "NONE" "*" "*" "N" "0" "0" "NONE" "NONE" "ALL" "0" "FULL"      "N" "ALL" "*" "0" "*" "Y" "*" ' ]



mm=[31,28,31,30,31,30,31,31,30,31,30, 31]



def load_day(table, clid, year, mon, day=None, center=None, bunit='*'):
	global cli, ld
	assert bunit
	lame_duck=''
	if ld:
		lame_duck=' -ld %d' % ld
	pars = params[table][0].format( **dict( CENTER = center, CLIENT = clid, YEAR = year, MONTH = mon, DAY = day, EOM = mm[mon-1],  BUNIT= bunit ))
	pycli  = cli.format(**dict( TABLE = table, PARAM_CNT = len([p for p in pars.strip().split(' ') if p]),  LAME_DUCK=lame_duck))
	cmd= '%s %s' % (pycli, pars)
	#print (cmd)
	#e()
	
	pfmtd([dict(Command=os.linesep.join(cmd.split()))], table)
	if 1:
		#if table  in ['ME_FinancingPosition']:
		#	if	mon in [1]: 
		
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


if __name__ == "__main__":

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
		if 1:
			year	= 2019
			mon 	= 1
			day 	= mm[mon-1]
			for clid in [223906, 223907]:
				for table in ['ME_FinancingPosition']:
						load_day(table,clid, year, mon, day, center,  bunit=b_unit)
		if 0:
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


 




























