import sys
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init



Email 		= create_actor (aname = 'Email', app_init=app_init )




#sql_conn		= InOut()
dump_file		= InOut()



lite_conn	= InOut()



file_size_rows=250000
email_args={'email_subject':'File->Lite'}


def run():
	lite_tbl={}
	for _source, val in cli.cfg['dump'].items():
		cli.set_source(_source)
		_src_class = list(val.keys())[0]

		DirReader 	= create_reader(aname = _src_class,	app_init=app_init )
		if 1: 
			cli.set_source(_source)
			dir_scfg = cli.get_dcfg(_src_class)
			path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)
			out_files	= InOut(file_names=[])
			print path
			DirReader.glob_dir(path=path,  out = out_files, ext='*.out')
			pp(out_files.file_names)

			for _trg_class, val in cli.cfg['target'][_source].items():
				cli.tcfg	= tcfg =  cli.get_tcfg(_trg_class)
				_dbname 	= tcfg["targetDb"]
				toDB 		= create_writer (aname = _trg_class,	app_init=app_init )
				if 1:
					toDB.begin_transaction (env =tcfg['targetDb'] , out 	= lite_conn )
					
					toDB.bulk_insert		 ( trans	= lite_conn, file_names = out_files,  qname = 'insertStmt', cfg = (dir_scfg, tcfg), create_table=True, strip_line_term=True)
					toDB.commit_transaction( trans	= lite_conn)
					
					lite_tbl[_source] = cli.get_parsed(ckey='targetTable', cfg=tcfg)
				
		pp(lite_tbl)
		
def run0():
	lite_tbl={}
	#pp(cli.cfg['source'].items())
	#e()
	for _source, val in cli.cfg['source'].items():
		_dbname=val["sourceDb"]
		DB 			= create_reader(_dbname,	app_init=app_init )
		FileWriter 	= create_writer('File',	app_init=app_init ) 
		data_files.file_names=[]
		if 1:
			cli.set_source(_source)
			lite_scfg, lite_tcfg = cli.cfg['teardown']['source'][_source], cli.cfg['teardown']['target'][_source]
			#pp(lite_scfg)
			path = cli.get_parsed(ckey='sourceDir', cfg=lite_scfg)
			#pp(path)
			#e()
			Dir.get_files(path=path,  out = data_files )
			#pp(data_files.file_names)
			#e()
			if 1:
				SQLite.begin_transaction ( out 	= lite_conn )
				
				SQLite.bulk_insert		 ( trans	= lite_conn, file_names = data_files,  qname = 'insertStmt', cfg = (lite_scfg, lite_tcfg) )
				SQLite.commit_transaction( trans	= lite_conn)
				
				lite_tbl[_source] = cli.get_parsed(ckey='targetTable', cfg=lite_tcfg)

				#SQLite.show_data(lite_tbl[_source])

	#e()
	if 1:
		tear= cli.tear
		compare = tear['compare']
		source = tear['source']
		fmt={}
		for db in source:
			fmt[db]=lite_tbl[db]
			
		for k,v in compare.items():
			
			compare[k]=v.format(**fmt)

		cli.exec_report(SQLite, compare)
	if 1:
		Email.send_email_att( **email_args )




