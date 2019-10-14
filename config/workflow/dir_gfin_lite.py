import sys
import itertools
import threading
import subprocess
from collections import OrderedDict

from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
from include.fmt import pfmt
e=sys.exit
cli, conn_pool=app_init


Email 	= create_actor (aname = 'Email', app_init=app_init )


#ok_files	= InOut()

lite_conn	= InOut()

#ok_files.file_names=[]



dump_file		= InOut()

file_size_rows=250000
email_args={'email_subject':'GTX->Vertica'}
insert_stats= InOut(source_cnt=-1, inserted_cnt=-1) 


	
def run():
	skip 	= 2
	serviceName='gfin'
	#deleted = {}
	
	#loaded  = {}
	#not_loaded  = {}
	#masterTbl = 'gtxMasterPKData'
	#do_not_delete = ['TxFinancingRateHist', masterTbl]
	do_not_load = ['TxFinancingRate',  'TxFinancingRateHist'] #'TxFinancingRate', 
	for _source, val in cli.cfg['dump'].items():
		cli.set_source(_source)
		_src_class = list(val.keys())[0]

		DirReader 	= create_reader(aname = _src_class,	app_init=app_init )
			
		if 1: 
			cli.set_source(_source)
			dir_scfg = cli.get_dcfg(_src_class)
			path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)
			ok_files	= InOut(file_names=[])
			DirReader.glob_dir(path=path,  out = ok_files, ext='*.ok')
			

			if 1:
				for _trg_class, val in cli.cfg['target'][_source].items():

					cli.tcfg	= tcfg =  cli.get_tcfg(_trg_class)
		
					_dbname 	= tcfg["targetDb"]
					toDB 		= create_writer (aname = _trg_class,	app_init=app_init )
					masterTabTag= tcfg['masterTableTag']
					masterTbl 	= tcfg['targetTables'][masterTabTag]['table_name']
					masterTblCol 	= tcfg['targetTables'][masterTabTag]['column_name']
					do_not_delete 	= tcfg['doNotDeleteTables'] +[masterTbl]
					do_not_load 	= tcfg['doNotLoadTables']
					to_conn=InOut()
					toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
					to_conn.cur.execute('set search_path to CIGRpt');
					if ok_files.file_names: # Master first
						try:

							stmt='drop table %s' % masterTbl;
							to_conn.cur.execute(stmt)
						except Exception as ex:
							#raise
							if not 'Table "%s" does not exist' % masterTbl in str(ex):
								raise

						stmt='create local temporary table %s ( %s bigint not null, MartModifiedDate timestamp)\n ON COMMIT PRESERVE ROWS' % (masterTbl, masterTblCol);
						pfmt([[stmt]],['Create master temp PK'])
						to_conn.cur.execute(stmt)
						#e()
					stats	= {}
					deleted = {}
					processed = []
					not_processed = []
					for okfn in ok_files.file_names:
						okFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=okfn, scfg=dir_scfg)
						okdir, _ = os.path.splitext(okfn)
						okbn = os.path.basename(okdir)
						#e()
						assert os.path.isdir(okdir)
						snap_df=cli.get_dest_folder(okdir)
						if os.path.isdir(snap_df):
							log.warning('[%s]Destination folder exists: [%s]' % (okdir, snap_df))
							not_processed.append(okfn)
							continue
						OkReader 	= create_reader(aname = "Dir",	app_init=app_init )
						out_files	= InOut(file_names=[])

						DirReader.glob_dir(path=okdir,  out = out_files, ext='*.out')
							
						apx = dict(MartModifiedDate=okFile.get_value(coords=(0,0), skip = skip))
						ftlist=[]
						
						for out_fn in out_files.file_names:
							print (out_fn)
							ftlist.append(os.path.basename(out_fn).split('.')[1])
							
						pfmt([[x] for x in ftlist], ['Files->Tables'])
						#e()
						if 1:
							ctables = cli.tcfg['targetTables'].keys()
							
							extra_file_tables=list(set(ftlist)-set(ctables))
							
							pfmt([[x] for x in extra_file_tables],['Tables not in config.'])
							
							extra_config_tables=list(set(ctables) - set(ftlist))
							
							pfmt([[x] for x in extra_config_tables],['Tables in config but not in file names.'])
							
							assert not extra_file_tables, 'Tables %s are not listed in config["targetTables"].' % extra_file_tables
								
						
						if 0:
							g = raw_input("Continue?") 
						if 1: #//create PK file
							
							fromFile= create_reader(aname = 'File',	app_init=app_init, file_name=os.path.join(okdir, 'gfin.Instrument.out'), scfg=dir_scfg)
							toFile	= create_reader(aname = 'File',	app_init=app_init, file_name=os.path.join(okdir, '%s.PK.out' % serviceName), scfg=dir_scfg , parse=False)
							rowcnt = cli.createPrimaryKeyFile( ffObj = fromFile, pkfn = os.path.join(okdir, '%s.PK.out' % serviceName) )
							
							
						assert masterTabTag in ftlist, '"%s" file is missing' % masterTabTag

						if 1:
							stmt='TRUNCATE TABLE %s' % (masterTbl);
							toDB.exec_dml(stmt, trans = to_conn, commit=False)
							deleted [masterTbl] = -1
							#e()
						#e()
						loaded		={}
						not_loaded  = {}
						if 1:
							pkfn= [x for x in out_files.file_names if os.path.basename(x).split('.')[1] in [masterTabTag]][0]
							
							
							outFile 	= create_reader(aname = "File",	app_init=app_init, file_name=pkfn, scfg=dir_scfg)
							fmt_cols = tcfg['targetTables'][masterTabTag].get('formatColumns',[])
							toDB.load_file ( trans	= to_conn, file_obj = outFile, table_name=masterTbl,  qname = 'insertStmt', fmt_cols=fmt_cols, cfg = (dir_scfg, tcfg), skip=skip, apx=apx, stats=stats)
							loaded[out_fn] = masterTbl
							#e()
						if 1:
							stmt='SELECT count(*) FROM %s t' %  masterTbl;
							pkcnt = toDB.exec_query(stmt).fetchall()[0][0]
							
							assert pkcnt == (rowcnt-skip)
							
						for out_fn in [x for x in out_files.file_names if not os.path.basename(x).split('.')[1] in [masterTabTag]]:
							outFile 	= create_reader(aname = "File",	app_init=app_init, file_name=out_fn, scfg=dir_scfg)
							outCols =[col[0] for col in outFile.get_header_cols()]
							tbl= os.path.basename(out_fn).split('.')[1]
							assert tbl
							


							if tbl not in [masterTabTag] +do_not_load: 
								

								if tbl not in do_not_delete:
									stmt='DELETE FROM %s WHERE %s in (SELECT t.%s FROM %s t)' % (tbl, masterTblCol, masterTblCol,  masterTbl);
									deleted [tbl] = toDB.exec_dml(stmt, trans = to_conn, commit=False)
									pfmt([[deleted [tbl]]], ['Deleted from %s' % tbl])
								else:
									deleted [tbl] = -1
									
								tblCols =toDB.get_columns(tbl).values()
								pfmt([[x] for x in list(set(tblCols)-set(outCols)- set (['MartModifiedDate']))],['Columns in Source, but not Target'])

								missing_cols = list(set(outCols)-set(tblCols))
								pfmt([(tbl,x) for x in missing_cols],['Table', 'Missing columns'])

								if missing_cols:
									to_conn.conn.rollback()
									
									schema = tcfg["targetSchema"]
									toDB.desc_table(schema, tbl)
									
									raise Exception ('File column %s missing in table "%s".' % (missing_cols, tbl))
								
								if 1:
									fmt_cols = tcfg['targetTables'][tbl].get('formatColumns',[])
									toDB.load_file ( trans	= to_conn, file_obj = outFile, table_name=tbl,  qname = 'insertStmt', fmt_cols = fmt_cols,  cfg = (dir_scfg, tcfg), skip=skip, apx=apx, stats=stats)
									loaded[out_fn] = tbl
							else:
								not_loaded[out_fn] = tbl
							


							
						else:
							toDB.commit_transaction ( trans	= to_conn)
							pfmt([[k]+[deleted [k]]+list(v)[1:]  for k,v in stats.items() if deleted [k]>=0], ['Table','Deleted', 'Accepted', 'Rejected','Line count','Skip', 'Diff'],'Load completed (deleted)'.upper())
							pfmt([(k,v) for k, v in loaded.items()], ['Loaded Files','Loaded Tables'])
							pfmt([(k,v) for k, v in not_loaded.items()], ['Not loaded Files','Not loaded Tables'])

							assert os.path.isdir(okdir)
							if 0:
								cli.MoveSnapFolder(okdir)
							processed.append(okfn)
						#break;
					
				if not ok_files.file_names:
					counter = itertools.count(1)
					pfmt([['No OK files at working dir: [ %s ]' % cli.pa[0]]], [ 'No files'])
				if processed:

					counter = itertools.count(1)
					pfmt([[next(counter),x] for x in processed], [ '##','Processed'])					
				if not_processed:

					counter = itertools.count(1)
					pfmt([[next(counter),x] for x in not_processed], [ '##','Not processed (backup exists)'])
			
	if 0:
		email_args.update(dict(cli_stats=None))
		Email.send_email( **email_args )
		cli.done()
		





