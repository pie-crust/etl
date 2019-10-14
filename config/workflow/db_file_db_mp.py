"""
"""

import sys
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


Email 		= create_actor ('Email',app_init=app_init )

Dir 	= create_reader('Dir', 		app_init=app_init ) 

uploaded_files= InOut()



data_files	= InOut()
data_files.file_names=[]
uploaded_files.file_names=[]

email_args={'email_subject':'DB->file'}

def run():
	ext_files=[]
	
	for _source, val in cli.cfg['source'].items():
		_dbname=val["sourceDb"]
		DB 			= create_reader(_dbname,	app_init=app_init )
		FileWriter 	= create_writer('File',	app_init=app_init ) 
		data_files.file_names=[]
		uploaded_files.file_names=[]
		if 1:
			cli.set_source(_source)
			DB.set_loader(FileWriter)
			
			total_ins= 0
			
			scfg= cli.get_scfg()
			source_chunk_size= scfg['sourceChunkSize']
			#maxRowsPerFile
			for cid, iq_data in enumerate(DB.fetch_many ( chunk_size=source_chunk_size,  source = scfg, qname = 'sourceStmt', out=InOut(), skip_header=0 )):
				dump_file		= InOut()
				FileWriter.open_file(id=cid, out = dump_file )
				if 1: #not total_ins:
					dump_cfg=cli.get_dcfg()
					FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg = dump_cfg)
				FileWriter.append_data ( file = dump_file,  data = iq_data, cfg = dump_cfg)
				total_ins+=len(iq_data.data)
				FileWriter.close_file(file = dump_file)
				ext_files.append(dump_file.fpath)
			#if not total_ins: #in case there's no data
			#	FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg = dump_cfg)
			
		pp(ext_files)
		if 1: #Load to DB
			cli.set_source(_source)
			file_scfg = cli.cfg['dump'][_source]

			path = cli.get_parsed(ckey='dumpDir', cfg=file_scfg)

			Dir.get_files(path=path,  out = data_files )
			pp(data_files.file_names)
			
			if 1:
				to_conn	= InOut()
				for _target, val in cli.cfg['target'][_source].items() or []:
					tcfg =  cli.cfg['target'][_source][_target]
					_todbname=val["targetDb"]
					
					toDB 	= create_writer(_target,	app_init=app_init )
					#print toDB
					#e()
					#toDB.begin_transaction  ( out 	= to_conn )
					rec_delim='\n'
					skip_header=0
					#S3.upload_files			( file_names = data_files, out = uploaded_files, skip_header=skip_header, rec_delim=rec_delim)
					toDB.insert_files		( file_names = data_files, out = uploaded_files, skip_header=skip_header, rec_delim=rec_delim, cfg= (file_scfg, tcfg) )
					#trans	= to_conn, file_names = data_files,  qname = 'insertStmt', cfg = (file_scfg, tcfg) )
					#toDB.commit_transaction ( trans	= to_conn)


	if 0:
		Email.send_email( **email_args )




