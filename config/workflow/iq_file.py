import sys
from collections import OrderedDict
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


Email 		= create_actor (aname ='Email',app_init=app_init )

Dir 	= create_reader(aname ='Dir', 		app_init=app_init ) 



dump_file		= InOut()

data_files	= InOut()
data_files.file_names=[]

insert_stats= InOut(inserted_cnt=-1)


file_size_rows=5000
email_args={'email_subject':'IQ->file->SQL'}
from_conn	= InOut()
term_line = False
def run():
	lite_tbl={}
	stats={}
	
	for _source, val in cli.cfg['source'].items():
		cli.set_source(_source)
		_src_class = list(val.keys())[0]
		cli.scfg= scfg=cli.get_scfg(_src_class)

		_dbname=cli.scfg["sourceDb"]
		fromDB 		= create_reader(aname =_src_class, app_init=app_init )
		#FileWriter 	= create_writer(aname ='File',	app_init=app_init ) 
		data_files.file_names=[]
		if 1:
			cli.set_source(_source)
			
			
			fromDB.begin_transaction  ( env =cli.scfg['sourceDb'] , out = from_conn )
			for _dmp_class, val in cli.cfg['dump'][_source].items() or []:
				FileWriter 	= create_writer(aname =_dmp_class,	app_init=app_init )
				fromDB.set_loader(FileWriter)				

				cli.dcfg= dcfg=cli.get_dcfg(_dmp_class)
				
				#for _trg_class, val in cli.cfg['target'][_source].items() or []:
				if 1:
					#cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)
					file_ins_cnt= 0
					total_ins= 0
					FileWriter.open_file( out = dump_file )
					print(dump_file.fpath)
					id=0
					if 1:
						start_time = time.time()
						loop_time = time.time()
						#for iq_data in DB.fetch_many ( chunk_size=file_size_rows,  source = cli.get_scfg(), qname = 'sourceStmt', out=InOut(), skip_header=0 ):
						for iq_data in fromDB.fetch_many ( chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=InOut(), skip_header=0, terminate_line= term_line):
							print ('WORKFLOW: Elapsed [%d] PRE WRITE: %s' % (id, time.time() - start_time))
							start_time = time.time()
							if not file_ins_cnt:
								FileWriter.create_header(file = dump_file, header = fromDB.get_header(), cfg=cli.dcfg, terminate_line= term_line)
							FileWriter.append_data ( file = dump_file,  data = iq_data, cfg=cli.dcfg)
							file_ins_cnt+=len(iq_data.data)
							print ('WORKFLOW: Elapsed [%d] POST WRITE: %s' % (id, time.time() - start_time))
							start_time = time.time()
							print ('WORKFLOW: Elapsed [%d] LOOP: %s' % (id, time.time() - loop_time))
							loop_time = time.time()
							id +=1
						if not file_ins_cnt: #in case there's no data
							FileWriter.create_header(file = dump_file, header = fromDB.get_header(), cfg=cli.dcfg, terminate_line= term_line)
						FileWriter.close_file(file = dump_file)

						total_ins +=file_ins_cnt
						
					if 1: #//check if there's data in a file
						dataFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=dump_file.fpath, scfg=dcfg)
						dataFile.describe()
						lcnt= dataFile.line_count() - cli.header_size(dcfg)
						assert lcnt, 'Dump file is empty\n%s'  % dump_file.fpath
						
					#e()
					if 0: #Load to DB
						cli.set_source(_source)
						dir_scfg = cli.get_dcfg(_dmp_class)
						path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)
						DirReader 	= create_reader(aname = _dmp_class,	app_init=app_init )
						DirReader.glob_dir(path=path,  out = data_files, ext='*.*')
						if 1:
							to_conn	= InOut()
							_todbname=tcfg["targetDb"]
							toDB 	= create_writer(aname =  _todbname,	app_init=app_init )
							toDB.begin_transaction  ( env =cli.scfg['sourceDb'] , out = to_conn )
							#toDB.begin_transaction  ( out 	= to_conn )
							toDB.bulk_insert		( trans	= to_conn, file_names = data_files,  qname = 'insertStmt', cfg = (dir_scfg, tcfg), out=insert_stats)
							toDB.commit_transaction ( trans	= to_conn)
				if 1:
					FileWriter.delete_dump(data_files)
				if 0:
					stats['%s->%s' % (_dbname, FileWriter.tofn)] =st=  OrderedDict()
					st['source_cnt']		= cli.get_src_row_count(DB) if not cli.lame_duck else cli.lame_duck
					st['total_extracted'] 	= total_ins
					st['total_inserted'] 	= insert_stats.inserted_cnt
	if 	0:
		for k, v in stats.items():
			assert v['source_cnt'] == v['total_extracted'], " %s <> %s" % ( v['source_cnt'], v['total_extracted'])
			assert v['source_cnt'] == v['total_inserted']
		
	if 0:
		email_args.update(dict(cli_stats=stats))
		Email.send_email( **email_args)

def run_fetchone():
	lite_tbl={}
	stats={}
	
	for _source, val in cli.cfg['source'].items():
		cli.set_source(_source)
		_src_class = list(val.keys())[0]
		cli.scfg= scfg=cli.get_scfg(_src_class)

		_dbname=cli.scfg["sourceDb"]
		fromDB 		= create_reader(aname =_src_class, app_init=app_init )
		#FileWriter 	= create_writer(aname ='File',	app_init=app_init ) 
		data_files.file_names=[]
		if 1:
			cli.set_source(_source)
			
			
			fromDB.begin_transaction  ( env =cli.scfg['sourceDb'] , out = from_conn )
			for _dmp_class, val in cli.cfg['dump'][_source].items() or []:
				FileWriter 	= create_writer(aname =_dmp_class,	app_init=app_init )
				fromDB.set_loader(FileWriter)				

				cli.dcfg= dcfg=cli.get_dcfg(_dmp_class)
				
				#for _trg_class, val in cli.cfg['target'][_source].items() or []:
				if 1:
					#cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)
					file_ins_cnt= 0
					total_ins= 0
					FileWriter.open_file( out = dump_file )
					print(dump_file.fpath)
					id=0
					if 1:
						start_time = time.time()
						loop_time = time.time()
						iq_data = InOut(data=None)
						cur = fromDB.get_query_cur ( chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=InOut(), skip_header=0, terminate_line= term_line)
						#for iq_data in DB.fetch_many ( chunk_size=file_size_rows,  source = cli.get_scfg(), qname = 'sourceStmt', out=InOut(), skip_header=0 ):
						for row in fromDB.fetch_row ( cur=cur,  source = cli.scfg, qname = 'sourceStmt', out=InOut(), skip_header=0, terminate_line= term_line):
							#print ('WORKFLOW: Elapsed [%d] PRE WRITE: %s' % (id, time.time() - start_time))
							start_time = time.time()
							if not file_ins_cnt:
								FileWriter.create_header(file = dump_file, header = fromDB.get_header(), cfg=cli.dcfg, terminate_line= term_line)
							iq_data.data = [row]
							#FileWriter.append_data ( file = dump_file,  data = iq_data, cfg=cli.dcfg)
							FileWriter.append_row ( file = dump_file,  dbrow = row, cfg=cli.dcfg)
							file_ins_cnt+=len(iq_data.data)
							#print ('WORKFLOW: Elapsed [%d] POST WRITE: %s' % (id, time.time() - start_time))
							#start_time = time.time()
							#print ('WORKFLOW: Elapsed [%d] LOOP: %s' % (id, time.time() - loop_time))
							#loop_time = time.time()
							if id> file_size_rows:
								print ('WORKFLOW: Elapsed [%d] LOOP: %s' % (total_ins, time.time() - loop_time))
								loop_time = time.time()
								id=0
							id +=1
						if not file_ins_cnt: #in case there's no data
							FileWriter.create_header(file = dump_file, header = fromDB.get_header(), cfg=cli.dcfg, terminate_line= term_line)
						FileWriter.close_file(file = dump_file)

						total_ins +=file_ins_cnt
						
					if 1: #//check if there's data in a file
						dataFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=dump_file.fpath, scfg=dcfg)
						dataFile.describe()
						lcnt= dataFile.line_count() - cli.header_size(dcfg)
						assert lcnt, 'Dump file is empty\n%s'  % dump_file.fpath
						
					#e()
					if 0: #Load to DB
						cli.set_source(_source)
						dir_scfg = cli.get_dcfg(_dmp_class)
						path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)
						DirReader 	= create_reader(aname = _dmp_class,	app_init=app_init )
						DirReader.glob_dir(path=path,  out = data_files, ext='*.*')
						if 1:
							to_conn	= InOut()
							_todbname=tcfg["targetDb"]
							toDB 	= create_writer(aname =  _todbname,	app_init=app_init )
							toDB.begin_transaction  ( env =cli.scfg['sourceDb'] , out = to_conn )
							#toDB.begin_transaction  ( out 	= to_conn )
							toDB.bulk_insert		( trans	= to_conn, file_names = data_files,  qname = 'insertStmt', cfg = (dir_scfg, tcfg), out=insert_stats)
							toDB.commit_transaction ( trans	= to_conn)
				if 1:
					FileWriter.delete_dump(data_files)
				if 0:
					stats['%s->%s' % (_dbname, FileWriter.tofn)] =st=  OrderedDict()
					st['source_cnt']		= cli.get_src_row_count(DB) if not cli.lame_duck else cli.lame_duck
					st['total_extracted'] 	= total_ins
					st['total_inserted'] 	= insert_stats.inserted_cnt
	if 	0:
		for k, v in stats.items():
			assert v['source_cnt'] == v['total_extracted'], " %s <> %s" % ( v['source_cnt'], v['total_extracted'])
			assert v['source_cnt'] == v['total_inserted']
		
	if 0:
		email_args.update(dict(cli_stats=stats))
		Email.send_email( **email_args)



