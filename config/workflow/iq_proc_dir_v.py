from include.utils import create_reader, create_writer, create_actor, InOut
from include.fmt import pfmtd, pfmt


cli, conn_pool=app_init



Email 	  		= create_actor (aname = 'Email', app_init=app_init )


IQ_cursor		= InOut()
s3_file_names	= InOut()



dump_file		= InOut()

file_size_rows=250000

email_args={'email_subject':'IQ.proc->file->Vertica'}

data_files	= InOut(); data_files.file_names=[]

insert_stats	= {} 
file_stats		= {}
from_conn		= InOut()

stats			= {}
deleted 		= {}
processed 		= []
not_processed 	= []
					
					
loaded			= {}
not_loaded  	= {}
do_not_delete 	= []
do_not_load 	= []
to_conn	= InOut()
def run():
	skip 		= 1
	total_ins 	= 0
	term_line 	= True
	#//validate cols
	for _source, val in cli.cfg['source'].items():
		cli.set_source(_source)
		_src_class = list(val.keys())[0]
		cli.scfg= scfg=cli.get_scfg(_src_class)
		for _trg_class, val in cli.cfg['target'][_source].items() or []:
			cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)

			_dbname = tcfg["targetDb"]
			toDB 	= create_writer (aname =_trg_class,	app_init=app_init )
			
			toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
			table='%s.%s' % (tcfg['targetSchema'], tcfg['targetTable'])
			toDB.desc_table(schema=tcfg['targetSchema'], tbl=tcfg['targetTable'], col_ord=False)
			#// validate cols
			cfg_cols=[x[u'columnName'] for x in cli.scfg[u'columnMappings']]
			tcols=toDB.get_cols()
			t_vs_c  = set(tcols) -set(cfg_cols)
			c_vs_t  = set(cfg_cols) -set(tcols)
			if t_vs_c: 
				pfmtd([dict(c_vs_t = c_vs_t)], 'Config has columns missing in target table.')
				
				raise Exception('Target table has columns missing in config: %s' % t_vs_c)
			
			if c_vs_t: 
				pfmtd([dict(t_vs_c = t_vs_c)], 'Target table has columns missing in config.')
				raise Exception('Config has columns missing in target table: %s' % c_vs_t)
			toDB.commit_transaction ( trans	= to_conn)
	#// transfer
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
		_src_class = list(val.keys())[0]

		DirReader 	= create_reader(aname = _src_class,	app_init=app_init )

		if 1: #//Get the file names
			cli.set_source(_source)
			dir_scfg = cli.get_dcfg(_src_class)
			path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)

			DirReader.glob_dir(path=path,  out = data_files, ext='*.*')
			
		if 1: #//Load to DB
			
			for _trg_class, val in cli.cfg['target'][_source].items() or []:

				cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)

				_dbname = tcfg["targetDb"]
				toDB 	= create_writer (aname =_trg_class,	app_init=app_init )
				
				toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
				
				table='%s.%s' % (tcfg['targetSchema'], tcfg['targetTable'])
				toDB.desc_table(schema=tcfg['targetSchema'], tbl=tcfg['targetTable'], col_ord=None)
				
				#// validate cols
				cfg_cols=[x[u'columnName'] for x in cli.scfg[u'columnMappings']]
				
				acols= cli.get_alt_cols(scfg)
				tcols=toDB.get_cols()
				fcols_alt=[]
				for data_file in data_files.file_names:
					dataFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=data_file, scfg=dir_scfg)
					dataFile.describe()
					file_stats[data_file] =  dataFile.line_count() - cli.header_size(dir_scfg)
					fcols_alt=[acols.get(x.decode(),x.decode()) for x in  dataFile.get_header(data_file, dir_scfg)]
					f_vs_c  = set(fcols_alt) -set(cfg_cols)
					c_vs_f  = set(cfg_cols) -set(fcols_alt)
					f_vs_t = set(fcols_alt) -set(tcols)
					t_vs_f = set(tcols) -set(fcols_alt)
					if f_vs_c: 
						pfmtd([dict(c_vs_f = c_vs_f)], 'Config has columns missing in dump file.')
						pfmtd([dict(f_vs_t = f_vs_t)], 'Dump file has columns missing in target table.')
						pfmtd([dict(t_vs_f = t_vs_f)], 'Target table has columns missing in dump file.')
						raise Exception('Target table has columns missing in config: %s' % f_vs_c)
					
					if c_vs_f: 
						pfmtd([dict(f_vs_c = f_vs_c)], 'Dump file has columns missing in config.')
						pfmtd([dict(f_vs_t = f_vs_t)], 'Dump file has columns missing in target table.')
						pfmtd([dict(t_vs_f = t_vs_f)], 'Target table has columns missing in dump file.')
						raise Exception('Config has columns missing in target table: %s' % c_vs_f)

					if f_vs_t: 
						pfmtd([dict(f_vs_c = f_vs_c)], 'Dump file has columns missing in config.')
						pfmtd([dict(c_vs_f = c_vs_f)], 'Config has columns missing in dump file.')
						pfmtd([dict(t_vs_f = t_vs_f)], 'Target table has columns missing in dump file.')
						raise Exception('Dump file has columns missing in target table: %s' % f_vs_t)
					if t_vs_f: 
						pfmtd([dict(f_vs_c = f_vs_c)], 'Dump file has columns missing in config.')
						pfmtd([dict(c_vs_f = c_vs_f)], 'Config has columns missing in dump file.')
						pfmtd([dict(f_vs_t = f_vs_t)], 'Dump file has columns missing in target table.')
						raise Exception('Target table has columns missing in dump file: %s' % t_vs_f)

				if 1:
					for data_fn in [x for x in data_files.file_names]:
						dataFile 	= create_reader(aname = "File",	app_init=app_init, file_name=data_fn, scfg=dir_scfg)
						dataFile.describe()

						fileCols =[col.decode() for col in dataFile.get_header_cols()]
						tbl= tcfg["targetTable"] #tcfg. os.path.basename(data_fn).split('.')[-2]
						assert tbl
						if 1:

							if 0 and tbl not in do_not_delete:
								stmt='DELETE FROM %s WHERE %s in (SELECT t.%s FROM %s t)' % (tbl, masterTblCol, masterTblCol,  masterTbl);
								deleted [tbl] = toDB.exec_dml(stmt, trans = to_conn, commit=False)
								pfmt([[deleted [tbl]]], ['Deleted from %s' % tbl])
							else:
								deleted [tbl] = -1
							if 0:
								acols= cli.get_alt_cols(scfg)
								dataFile.cols_alt=[acols.get(x.decode(),x.decode()) for x in  dataFile.cols]
							else:
								dataFile.set_alt_cols()

							missing_cols = list(set(dataFile.cols_alt)-set(tcols))
							pfmt([(tbl,x) for x in missing_cols],['Table', 'Missing columns'])
							schema = tcfg["targetSchema"]
							if missing_cols:
								pfmt([[x] for x in missing_cols],['Columns in Source, but not Target'])
								to_conn.conn.rollback()
								toDB.desc_table(schema, tbl)
								raise Exception ('File column %s missing in table "%s".' % (missing_cols, tbl))
							
							if 1:
								apx={}
								fmt_cols = []

								toDB.load_file ( trans	= to_conn, file_obj = dataFile, schema=schema,  table_name=tbl,  qname = 'insertStmt', fmt_cols = fmt_cols,  cfg = (dir_scfg, tcfg), skip=skip, apx=apx, stats=stats)
								loaded[data_fn] = tbl
						else:
							not_loaded[data_fn] = tbl

					else:
						if 1:
							toDB.commit_transaction ( trans	= to_conn)
							pfmt([[k]+[deleted [k]]+list(v)[1:]  for k,v in stats.items() if deleted [k]>=0], ['Table','Deleted', 'Accepted', 'Rejected','Line count','Skip', 'Diff'],'Load completed (deleted)'.upper())
							pfmt([(k,v) for k, v in loaded.items()], ['Loaded Files','Loaded Tables'])
							pfmt([(k,v) for k, v in not_loaded.items()], ['Not loaded Files','Not loaded Tables'])

				e()
				if 0:
					#toDB.truncate_table		( table = table )
					toDB.bulk_load			( trans	= to_conn, file_names = data_files,  qname = 'insertStmt', cfg = (dir_scfg, tcfg), out=insert_stats)

				for k in file_stats.keys():
					assert insert_stats[k] == file_stats[k], 'Insert vs file count diff: %s<>%s for file \n%s' % (insert_stats[k] , file_stats[k], k)
				toDB.commit_transaction ( trans	= to_conn)

				
				
	if 0:
		Email.send_email( **email_args )










