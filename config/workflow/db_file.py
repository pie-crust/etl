"""
"""

import sys
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


Email 		= create_actor ('Email',app_init=app_init )




dump_file		= InOut()



file_size_rows=250000
email_args={'email_subject':'DB->file'}

def run():
	lite_tbl={}
	for _source, val in cli.cfg['source'].items():
		_dbname=val["sourceDb"]
		DB 			= create_reader(_dbname,	app_init=app_init )
		FileWriter 	= create_writer('File',	app_init=app_init ) 
		#data_files.file_names=[]
		if 1:
			cli.set_source(_source)
			DB.set_loader(FileWriter)
			
			total_ins= 0
			FileWriter.open_file( out = dump_file )
			
			for iq_data in DB.fetch_many ( chunk_size=file_size_rows,  source = cli.get_scfg(), qname = 'sourceStmt', out=InOut(), skip_header=0 ):
				if not total_ins:
					FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg=cli.get_dcfg())
				FileWriter.append_data ( file = dump_file,  data = iq_data, cfg=cli.get_dcfg())
				total_ins+=len(iq_data.data)
			if not total_ins: #in case there's no data
				FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg=cli.get_dcfg())
			FileWriter.close_file(file = dump_file)

	if 1:
		Email.send_email( **email_args )




