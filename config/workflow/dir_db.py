"""

"""
import sys
import threading
import subprocess
from collections import OrderedDict

from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


Email 	= create_actor ('Email', 	app_init=app_init )


data_files	= InOut()
lite_conn	= InOut()

data_files.file_names=[]


dump_file		= InOut()

file_size_rows=250000
email_args={'email_subject':'Dir->IQ'}
insert_stats= InOut(source_cnt=-1, inserted_cnt=-1)

def run():
	lite_tbl={}
	stats={}
	for _source, val in cli.cfg['dump'].items():
		cli.set_source(_source)
		_src_class = val.keys()[0]


		DirReader 	= create_reader(_src_class,	app_init=app_init )

			
		if 1: #Get the file names
			cli.set_source(_source)
			dir_scfg = cli.get_dcfg(_src_class)
			path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)
			DirReader.get_files(path=path,  out = data_files )
			
		if 1: #Load to DB
			to_conn	= InOut()
			for _trg_class, val in cli.cfg['target'][_source].items() or []:

				cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)

				_dbname = tcfg["targetDb"]
				toDB 	= create_writer (_trg_class,	app_init=app_init )
				toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
				toDB.bulk_load			( trans	= to_conn, file_names = data_files,  qname = 'insertStmt', cfg = (dir_scfg, tcfg), out=insert_stats)
				toDB.commit_transaction ( trans	= to_conn)

		
		if 0:
			stats['Dir->%s' % (_dbname)] =st=  OrderedDict()
			st['source_cnt']		= cli.get_src_row_count(DB) if not cli.lame_duck else cli.lame_duck
			st['total_extracted'] 	= insert_stats.inserted_cnt
			st['total_inserted'] 	= insert_stats.inserted_cnt
	if 0:
		for k, v in stats.items():
			assert v['source_cnt'] == v['total_extracted']
			assert v['source_cnt'] == v['total_inserted']
		
	if 1:
		email_args.update(dict(cli_stats=None))
		Email.send_email( **email_args )
		





