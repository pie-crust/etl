"""
"""

import sys
from collections import OrderedDict
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


Email 		= create_actor ('Email',app_init=app_init )

Dir 	= create_reader('Dir', 		app_init=app_init ) 



dump_file		= InOut()

data_files	= InOut()
data_files.file_names=[]

insert_stats= InOut(inserted_cnt=-1)


file_size_rows=250000
email_args={'email_subject':'DB->file'}

def run():
	lite_tbl={}
	stats={}
	for _source, val in cli.cfg['source'].items():
		_dbname=val["sourceDb"]
		DB 			= create_reader(_dbname, app_init=app_init )
		FileWriter 	= create_writer('File',	app_init=app_init ) 
		data_files.file_names=[]
		if 1:
			cli.set_source(_source)
			DB.set_loader(FileWriter)
			
			total_ins= 0
			FileWriter.open_file( out = dump_file )
			dump_cfg=cli.get_dcfg()
			for iq_data in DB.fetch_many ( chunk_size=file_size_rows,  source = cli.get_scfg(), qname = 'sourceStmt', out=InOut(), skip_header=0 ):
				if not total_ins:
					
					FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg = dump_cfg)
				FileWriter.append_data ( file = dump_file,  data = iq_data, cfg = dump_cfg)
				total_ins+=len(iq_data.data)
			if not total_ins: #in case there's no data
				FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg = dump_cfg)
			FileWriter.close_file(file = dump_file)
			
		if 1: #Load to DB
			cli.set_source(_source)
			file_scfg = cli.cfg['dump'][_source]
			path = cli.get_parsed(ckey='dumpDir', cfg=file_scfg)
			Dir.get_files(path=path,  out = data_files )
			if 1:
				to_conn	= InOut()
				for _target, val in cli.cfg['target'][_source].items() or []:
					tcfg =  cli.cfg['target'][_source][_target]
					_todbname=val["targetDb"]
					toDB 	= create_writer(_todbname,	app_init=app_init )
					toDB.begin_transaction  ( out 	= to_conn )
					toDB.bulk_insert		( trans	= to_conn, file_names = data_files,  qname = 'insertStmt', cfg = (file_scfg, tcfg), out=insert_stats)
					toDB.commit_transaction ( trans	= to_conn)

		FileWriter.delete_dump(data_files)
		
		stats['%s->%s' % (_dbname, _todbname)] =st=  OrderedDict()
		st['source_cnt']		= cli.get_src_row_count(DB) if not cli.lame_duck else cli.lame_duck
		st['total_extracted'] 	= total_ins
		st['total_inserted'] 	= insert_stats.inserted_cnt
	for k, v in stats.items():
		assert v['source_cnt'] == v['total_extracted']
		assert v['source_cnt'] == v['total_inserted']
		
	if 1:
		email_args.update(dict(cli_stats=stats))
		Email.send_email( **email_args )




