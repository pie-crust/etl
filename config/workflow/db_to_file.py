"""
time python cli.py -nopp 3 -dcf config/db_config.DEV.json \
-pcf config/proc/sync/iq_mem_sql/delta_load.json --proc_params   \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2016-06-19'"  Accounting.CIGActgH.HydraPNLEntries \
 
 2>&1| tee delta_load.log 
"""

import sys
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init

if 0:
	SQLServer 	= create_reader('SQLServer',	app_init=app_init )
	IQ_FileWriter 	= create_writer('File',	app_init=app_init ) 
	SQL_FileWriter 	= create_writer('File',	app_init=app_init )

Email 		= create_actor ('Email',app_init=app_init )


Dir 	= create_reader('Dir', 		app_init=app_init ) 
SQLite 	= create_writer('SQLite',	app_init=app_init ) 

#sql_conn		= InOut()
dump_file		= InOut()


data_files	= InOut()
lite_conn	= InOut()

data_files.file_names=[]

file_size_rows=250000
email_args={'email_subject':'IQ_SQL_teardown'}

def run():
	lite_tbl={}
	for _source, val in cli.cfg['source'].items():
		_dbname=val["sourceDb"]
		DB 			= create_reader(_dbname,	app_init=app_init )
		FileWriter 	= create_writer('File',	app_init=app_init ) 
		data_files.file_names=[]
		if 1:
			cli.set_source(_source)
			DB.set_loader(FileWriter)
			
			total_ins= 0
			FileWriter.open_file( out = dump_file )
			
			for iq_data in DB.fetch_many ( chunk_size=file_size_rows,  source = cli.get_scfg(), qname = 'sourceStmt', out=InOut(), skip_header=0 ):
				if not total_ins:
					FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg=cli.get_tcfg())
				FileWriter.append_data ( file = dump_file,  data = iq_data, cfg=cli.get_tcfg())
				total_ins+=len(iq_data.data)
			if not total_ins: #in case there's no data
				FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg=cli.get_tcfg())
			FileWriter.close_file(file = dump_file)
		if 1:
			cli.set_source(_source)
			lite_scfg, lite_tcfg = cli.cfg['teardown']['source'][_source], cli.cfg['teardown']['target'][_source]
			#pp(lite_scfg)
			path = cli.get_parsed(ckey='sourceDir', cfg=lite_scfg)
			#pp(path)
			#e()
			Dir.get_files(path=path,  out = data_files )

			if 1:
				SQLite.begin_transaction ( out 	= lite_conn )
				
				SQLite.bulk_insert		 ( trans	= lite_conn, file_names = data_files,  qname = 'insertStmt', cfg = (lite_scfg, lite_tcfg) )
				SQLite.commit_transaction( trans	= lite_conn)
				
				lite_tbl[_source] = cli.get_parsed(ckey='targetTable', cfg=lite_tcfg)

				SQLite.show_data(lite_tbl[_source])

	if 0:
		_source="SQLServer"
		data_files.file_names=[]
		if 1:
			cli.set_source(_source)
			SQLServer.set_loader(SQL_FileWriter)
			
			total_ins= 0
			SQL_FileWriter.open_file( out = dump_file )
			
			for iq_data in SQLServer.fetch_many ( chunk_size=file_size_rows,  source = cli.get_scfg(), qname = 'sourceStmt', out=InOut(), skip_header=0 ):
				if not total_ins:
					SQL_FileWriter.create_header(file = dump_file, header = SQLServer.get_header(), cfg=cli.get_tcfg())
				SQL_FileWriter.append_data ( file = dump_file,  data = iq_data, cfg=cli.get_tcfg())
				total_ins+=len(iq_data.data)
			if not total_ins: #in case there's no data
				SQL_FileWriter.create_header(file = dump_file, header = SQLServer.get_header(), cfg=cli.get_tcfg())
			SQL_FileWriter.close_file(file = dump_file)
		if 1:
			cli.set_source(_source)
			lite_scfg, lite_tcfg = cli.cfg['teardown']['source'][_source], cli.cfg['teardown']['target'][_source]
			#pp(lite_scfg)
			path = cli.get_parsed(ckey='sourceDir', cfg=lite_scfg)
			#pp(path)
			#e()
			Dir.get_files(path=path,  out = data_files )

			if 1:
				SQLite.begin_transaction ( out 	= lite_conn )
				
				SQLite.bulk_insert		 ( trans	= lite_conn, file_names = data_files,  qname = 'insertStmt', cfg = (lite_scfg, lite_tcfg) )
				SQLite.commit_transaction( trans	= lite_conn)
				lite_tbl_2 = cli.get_parsed(ckey='targetTable', cfg=lite_tcfg)
				#pp(lite_tbl_2)
				SQLite.show_data(lite_tbl_2)
				
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
		Email.send_email( **email_args )




