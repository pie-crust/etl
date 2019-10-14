from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init



Email 	  		= create_actor (aname = 'Email', app_init=app_init )


IQ_cursor		= InOut()
s3_file_names	= InOut()



dump_file		= InOut()

file_size_rows=250000

email_args={'email_subject':'IQ.procedure->IQ'}

data_files	= InOut()

data_files.file_names=[]
insert_stats= {} 
file_stats= {}
from_conn	= InOut()
def run():
	total_ins = 0
	term_line = True
	for _source, val in cli.cfg['source'].items():
		cli.set_source(_source)
		_src_class = list(val.keys())[0]
		cli.scfg= scfg=cli.get_scfg(_src_class)

		_dbname=cli.scfg["sourceDb"]
		fromDB 			= create_reader(aname = _src_class,	app_init=app_init )


		fromDB.begin_transaction  ( env =cli.scfg['sourceDb'] , out = from_conn )
		if 1: #//Extract to Dir
			
			for _dmp_class, val in cli.cfg['dump'][_source].items() or []:
				FileWriter 	= create_writer(aname =_dmp_class,	app_init=app_init ) 
				fromDB.set_loader(FileWriter)
				cli.dcfg= cli.get_dcfg(_dmp_class)
				for _trg_class, val in cli.cfg['target'][_source].items() or []:

					cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)
					file_ins_cnt= 0
					FileWriter.open_file( out = dump_file )
					
					for iq_data in fromDB.fetch_many ( chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=InOut(), skip_header=0, terminate_line= term_line):

						if not file_ins_cnt:
							FileWriter.create_header(file = dump_file, header = fromDB.get_header(), cfg=cli.dcfg, terminate_line= term_line)
						FileWriter.append_data ( file = dump_file,  data = iq_data, cfg=cli.dcfg)
						file_ins_cnt+=len(iq_data.data)
					if not file_ins_cnt: #in case there's no data
						FileWriter.create_header(file = dump_file, header = fromDB.get_header(), cfg=cli.dcfg, terminate_line= term_line)
					FileWriter.close_file(file = dump_file)
					total_ins +=file_ins_cnt
		fromDB.desc_cur(cur = from_conn.cur, colord=False)
		
		fromDB.commit_transaction ( trans	= from_conn)
	log.info('Total records saved: %d' % total_ins)
	#// Load to IQ
	for _source, val in cli.cfg['dump'].items():
		cli.set_source(_source)
		_src_class = val.keys()[0]


		DirReader 	= create_reader(aname = _src_class,	app_init=app_init )

			
		if 1: #//Get the file names
			cli.set_source(_source)
			dir_scfg = cli.get_dcfg(_src_class)
			path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)

			DirReader.glob_dir(path=path,  out = data_files, ext='*.*')
			
		if 1: #//Load to DB
			to_conn	= InOut()
			for _trg_class, val in cli.cfg['target'][_source].items() or []:

				cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)

				_dbname = tcfg["targetDb"]
				toDB 	= create_writer (aname =_trg_class,	app_init=app_init )
				
				toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
				
				table='%s.%s' % (tcfg['targetSchema'], tcfg['targetTable'])
				toDB.desc_table(schema=tcfg['targetSchema'], tbl=tcfg['targetTable'], colord=False)

				
				#// validate cols
				acols= cli.get_alt_cols(scfg)
				tcols=toDB.get_cols()
				fcols_alt=[]
				for data_file in data_files.file_names:
					dataFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=data_file, scfg=dir_scfg)
					dataFile.describe()
					file_stats[data_file] =  dataFile.line_count() - cli.header_size(dir_scfg)
					fcols_alt=[acols.get(x,x) for x in  dataFile.get_header(data_file, dir_scfg)]
					assert not set(fcols_alt) -set(tcols), 'File has columns missing in table.'
					assert not set(tcols) -set(fcols_alt), 'Table has columns missing in file.'


				#toDB.truncate_table		( table = table )
				toDB.bulk_load			( trans	= to_conn, file_names = data_files,  qname = 'insertStmt', cfg = (dir_scfg, tcfg), out=insert_stats, header=fcols_alt)

				for k in file_stats.keys():
					assert insert_stats[k] == file_stats[k], 'Insert vs file count diff: %s<>%s for file \n%s' % (insert_stats[k] , file_stats[k], k)
				toDB.commit_transaction ( trans	= to_conn)

				
				
	if 0:
		Email.send_email( **email_args )










