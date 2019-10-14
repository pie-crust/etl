from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init


#IQ 				= create_reader('IQ',  	app_init=app_init )
#FileWriter 	= create_writer('File',	app_init=app_init ) 
Email 	  		= create_actor ('Email',app_init=app_init )


IQ_cursor		= InOut()
s3_file_names	= InOut()



dump_file		= InOut()

file_size_rows=250000

email_args={'email_subject':'IQ.procedure->IQ'}



def run():
	total_ins = 0
	for _source, val in cli.cfg['source'].items():
		cli.set_source(_source)
		_src_class = val.keys()[0]
		cli.scfg= cli.get_scfg(_src_class)

		_dbname=cli.scfg["sourceDb"]
		DB 			= create_reader(_dbname,	app_init=app_init )
		FileWriter 	= create_writer('Dir',	app_init=app_init ) 
		DB.set_loader(FileWriter)

		if 1: #Extract to Dir
			
			for _dmp_class, val in cli.cfg['dump'][_source].items() or []:

				cli.dcfg= cli.get_dcfg(_dmp_class)
				pp(cli.dcfg)

				file_ins_cnt= 0
				FileWriter.open_file( out = dump_file )
				if 0:
					IQ.open_stream				( dbcfg = cli.scfg, qname = 'sourceStmt', out=IQ_cursor )
					S3StreamLoader.load_stream	( source=IQ_cursor,skip_header=0,  out=s3_file_names )
	
				for iq_data in DB.fetch_many( chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=InOut(), skip_header=0 ):
					if not file_ins_cnt:
						FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg=cli.dcfg)
					FileWriter.append_data ( file = dump_file,  data = iq_data, cfg=cli.dcfg)
					file_ins_cnt+=len(iq_data.data)
				if not file_ins_cnt: #in case there's no data
					FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg=cli.dcfg)
				FileWriter.close_file(file = dump_file)
				total_ins +=file_ins_cnt

	log.info('Total records saved: %d' % total_ins)
	if 1:
		Email.send_email( **email_args )
		




