"""
C:\temp\Python37-32>python max_elapsed.py
"""
import os, sys,  re
import win32com.client
from datetime import datetime
#from sqlite3 import dbapi2 as sqlite
import sqlite3
from pprint import pprint as pp
e=sys.exit


regs=[
('center', '(?P<center>ACCT|DESK),'),
('env', '\[(?P<env>[A-Z]+)\] IQ->Snowflake'),
('table','\[PROD\] IQ->Snowflake \[(?P<table>[a-zA-Z_]+)\] \['),
('proc','[a-zA-Z]+\.(?P<proc>[0-9a-zA-Z]+_WRAPPER)'),
('client','\] \[(?P<client>[0-9]+), '),
('started_on','Started On: (?P<started_on>[0-9\-\:\ ]+)'),
('ended_on','Ended On:(?P<ended_on>[0-9\-\:\ ]+)'),
('asodt',', (?P<asodt>201[0-9\-]+), '),
('loaded_cnt','Records Added: (?P<loaded_cnt>[0-9/\,]+)')]
def connect():
	lite_dir= '/tmp/cli/lite'
	assert lite_dir
	if not os.path.isdir(lite_dir):
		os.makedirs(lite_dir)
	localdb=os.path.join(lite_dir, 'stats.db')
	if os.path.isfile(localdb): os.remove(localdb)
	return sqlite3.connect(localdb,detect_types=sqlite3.PARSE_DECLTYPES)
def parse_stats(txt, stats):
	for reg in regs:
		group, regexp = reg
		m = re.search(regexp, txt)
		try:
			stats[group]= m.group(group).strip()
		except:
			if group in stats:
				pass
			else:
				stats[group]=''
if __name__ == '__main__':
	outlook = win32com.client.Dispatch("Outlook.Application")
	namespace = outlook.GetNamespace("MAPI")
	root_folder = namespace.Folders.Item(1)
	inbox = root_folder.Folders[1]
	misc = inbox.Folders[0]

	stmt="CREATE TABLE stats( tname varchar, client varchar, center varchar, asodt varchar, started_on timestamp, ended_on timestamp, loaded_cnt varchar)"
	conn=connect()
	cur=conn.cursor()

	cur.execute(stmt)


	ins=[]
	for message in misc.Items:
		stats={}
		if message.Subject.startswith('[PROD] IQ->Snowflake'):
			subject = message.Subject
			parse_stats(subject, stats)		
			body=message.Body
			parse_stats(body, stats)
			if stats['loaded_cnt']:
				stats['loaded_cnt']= stats['loaded_cnt'].replace(',','')
			stmt="INSERT into stats (tname,client, center,asodt,  started_on,  ended_on, loaded_cnt) VALUES('{table}', '{client}', '{center}', '{asodt}','{started_on}','{ended_on}', {loaded_cnt})".format(**stats)
			conn.execute(stmt)
	conn.commit()


	if 1:
		stmt='SELECT tname, asodt, max(  Cast ((  JulianDay(ended_on) - JulianDay(started_on)) * 24 * 60  As Integer)) diff from stats group by 1, 2 order by 1 desc,2 desc'
		cur.execute(stmt)
		for row in cur.fetchall():
			print ('%s,\t %s\t %s' % row)

