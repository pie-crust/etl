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


ok_files	= InOut()
out_files	= InOut()
lite_conn	= InOut()

ok_files.file_names=[]
out_files.file_names=[]


dump_file		= InOut()

file_size_rows=250000
email_args={'email_subject':'GTX->Vertica'}
insert_stats= InOut(source_cnt=-1, inserted_cnt=-1)

def run():
	for _source, val in cli.cfg['dump'].items():
		cli.set_source(_source)
		_src_class = val.keys()[0]


		DirReader 	= create_reader(_src_class,	app_init=app_init )

			
		if 1: #Get the file names
			cli.set_source(_source)
			dir_scfg = cli.get_dcfg(_src_class)
			path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)
			DirReader.glob_dir(path=path,  out = ok_files, ext='*.ok')
			
			
			for okfn in ok_files.file_names:
				okdir, _ = os.path.splitext(okfn)
				assert os.path.isdir(okdir)
				OkReader 	= create_reader("Dir",	app_init=app_init )
				DirReader.glob_dir(path=okdir,  out = out_files, ext='*.out')
				pp(out_files.file_names)

				if 1:
					for _trg_class, val in cli.cfg['target'][_source].items():

						cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)

						_dbname = tcfg["targetDb"]
						toDB 	= create_writer (_trg_class,	app_init=app_init )
						to_conn=InOut()
						for out_fn in out_files.file_names:
							tbl= os.path.basename(out_fn).split('.')[1]
							print tbl
							toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
							toDB.load_file			( trans	= to_conn, file_name = out_fn, table_name=tbl,  qname = 'insertStmt', cfg = (dir_scfg, tcfg), create_table = True)
							toDB.commit_transaction ( trans	= to_conn)
				

	if 1:
		email_args.update(dict(cli_stats=None))
		
		Email.send_email( **email_args )
		etl.done()
		





