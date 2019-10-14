"""

"""
import sys, base64, hashlib
import itertools
import threading
import subprocess
from collections import OrderedDict

from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
from include.fmt import  pfmt, psql, pfmtd
e=sys.exit
cli, conn_pool=app_init


Email 	= create_actor (aname = 'Email', app_init=app_init )

lite_conn	= InOut()

dump_file		= InOut()

file_size_rows=250000
email_args={'email_subject':'GTX->Vertica'}
insert_stats= InOut(source_cnt=-1, inserted_cnt=-1) 


	
def run():
	skip 	= 2

	do_not_load = [] 
	for _source, val in cli.cfg['dump'].items():
		cli.set_source(_source)
		_src_class = list(val.keys())[0]

		DirReader 	= create_reader(aname = _src_class,	app_init=app_init )


		cli.set_source(_source)
		dir_scfg = cli.get_dcfg(_src_class)
		path = cli.get_parsed(ckey='dumpDir', cfg=dir_scfg)
		ok_files	= InOut(file_names=[])
		DirReader.glob_dir(path=path,  out = ok_files, ext='*.ok')
		
		loaded		={}

		for _trg_class, val in cli.cfg['target'][_source].items():

			cli.tcfg	= tcfg =  cli.get_tcfg(_trg_class)

			_dbname 	= tcfg["targetDb"]
			toDB 		= create_writer (aname = _trg_class,	app_init=app_init )
			
			do_not_delete 	= tcfg['doNotDeleteTables']
			do_not_load 	= tcfg['doNotLoadTables']
			to_conn=InOut()
			toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
			toSchema = tcfg['targetSchema']
			stmt = 'set search_path to %s' % toSchema
			psql(stmt)
			to_conn.cur.execute(stmt);

			

			pkstats={}
			for okfn in ok_files.file_names:
				okFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=okfn, scfg=dir_scfg)
				okdir, okname = os.path.splitext(okfn)
				okbn = os.path.basename(okdir)
			
				out_files	= InOut(file_names=[])
				
				DirReader.glob_dir(path=okdir,  out = out_files, ext='*.out')
				
				#e()
				if 1: # Check if some there are files missing in config
					ftlist=[]
					
					for out_fn in out_files.file_names:
						print (out_fn)
						ftlist.append(os.path.basename(out_fn).split('.')[1])
						
					pfmt([[x] for x in ftlist], ['Files->Tables'])
				
					ctables = cli.tcfg['targetTables'].keys()
					extra_file_tables=list(set(ftlist)-set(ctables))
					pfmt([[x] for x in extra_file_tables],['Tables not in config.'])
					extra_config_tables=list(set(ctables) - set(ftlist))
					pfmt([[x] for x in extra_config_tables],['Tables in config but not in file names.'])
					assert not extra_file_tables, 'Tables %s are not listed in config["targetTables"].' % extra_file_tables
					

				for outfn in  out_files.file_names: # Master first

					outFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=outfn, scfg=dir_scfg)

					outbn 	= os.path.basename(outfn)
					tbl=outbn.split('.')[1]
					outTbl 	= 'tmp_PK_%s' % tbl
					outCols	= outFile.get_header_cols()
					apxCols =[('MartModifiedDate', 'timestamp'), ('AsOfFrom', 'timestamp'), ('AsOfTo', 'timestamp'), ('MD5','char(22)')]
					outTblCols= toDB.get_create_col_list(outCols, apx=apxCols)
					
					toCols= toDB.get_col_types(toSchema, tbl)
					pp(toCols)
					

					toDB.desc_tmp_table(outTbl,outCols+apxCols)

					do_not_delete.append(outTbl)
					
					try:

						stmt='drop table %s' % outTbl;
						to_conn.cur.execute(stmt)
					except Exception as ex:
						#raise
						if not 'Table "%s" does not exist' % outTbl in str(ex):
							raise
					psql(outfn)
					stmt='CREATE LOCAL TEMPORARY TABLE %s ( %s )\nON COMMIT PRESERVE ROWS' % (outTbl, ', \n'.join(['%s %s' % tuple(col) for col in toCols]));
					pfmt([[stmt]],['Create master temp PK' + outTbl])
					toDB.exec_ddl(stmt)
					if 1: #//Load data into PK table


						fmt_cols = {}
						mmDt = okFile.get_value(coords=(0,0), skip=skip)
						
						md5val = (base64.b64encode(hashlib.md5(b'test').digest()))
						
						apx = OrderedDict()
						apx['MartModifiedDate'] = mmDt
						apx['AsOfFrom'] 		= mmDt
						apx['AsOfTo']			= "12/31/9999"
						apx['MD5']				= '' #//defined on row level

						pk_outfn = '%s.pk' % outfn
						colsep= dir_scfg['columnDelimiter']
						
						with open(pk_outfn, 'wb') as pkfh:
							with open(outfn, 'rb') as outfh:
								line = outfh.readline().strip()
								pkfh.write(line+ colsep.join(apx.keys()).encode()+os.linesep.encode())
								line = outfh.readline().strip()
								apxTypes= colsep.join([col[1] for col in apxCols])
								pkfh.write(line + apxTypes.encode() +os.linesep.encode())
								line = outfh.readline().strip()
								while line:
									md5 	= (base64.b64encode(hashlib.md5(line.replace(b'|',b'')).digest()))
									apx['MD5'] 	= md5.decode('ascii', 'ignore').strip('=') #// REDO

									pkfh.write(line+ colsep.join(apx.values()).encode()+os.linesep.encode())
									line = outfh.readline().strip()
						outPkFile 	= create_reader(aname = 'File',	app_init=app_init, file_name=pk_outfn, scfg=dir_scfg)
						outPkFile.set_alt_cols()
						
						schema =tcfg['targetSchema']
						toDB.load_grds_file ( trans	= to_conn, file_obj = outPkFile, schema=schema, table_name=outTbl,  qname = 'insertStmt', fmt_cols=fmt_cols, cfg = (dir_scfg, tcfg), skip=skip, stats=pkstats)
						loaded[outbn]=outTbl
						#outPkFile.delete()

				#pfmtd([pkstats])
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

				out_files	= InOut(file_names=[])
				DirReader.glob_dir(path=okdir,  out = out_files, ext='*.out')
				apx = dict(MartModifiedDate=okFile.get_value(coords=(0,0), skip = skip))


						
				#e()
				if 0:
					g = raw_input("Continue?") 

				not_loaded  = {}


					
				for table_name in ftlist:
					tmpTbl 	= 'tmp_PK_%s' % table_name
					toCols= toDB.get_tab_cols(tmpTbl)
					#pp(toCols)
					toDB.desc_table(None, tmpTbl)
					toDB.desc_table(toSchema, table_name)
					#e()
					if table_name in ['TxnLookupMap']:
						
						tmpCols= ',\n  '.join(['tmid.%s' % col[0].decode()  for col in toCols])
						ins = """ 
insert into {0} ( {1} ) 
select distinct {2} 
from {3} tmid LEFT JOIN {0} ta ON ta.{4} = tmid.{4}
AND ta.{5} = tmid.{5}
AND ta.{6} = tmid.{6}
AND ta.ValidFrom = tmid.ValidFrom and ta.AsOfTo = tmid.AsOfTo
where ta.MD5 <> tmid.MD5
OR ta.{4} is NULL
""".format(table_name, ',\n  '.join([col[0].decode() for col in toCols]), tmpCols, tmpTbl, toCols[0][0].decode(), toCols[1][0].decode(), toCols[2][0].decode())
						psql(ins)
						inserted = toDB.exec_dml(ins , trans = to_conn, commit = False)
						pfmtd([dict(Inserted = inserted)])
					elif table_name in ['G3Lookup', 'GCLookup', 'GISLookup', 'GPSLookup', 'GPXLookup', 'GPosLookup',
						'GTxLookup', 'FundToBusinessUnitMap', 'TxEditReason']:
						
						tmpCols= ',\n  '.join(['tmid.%s' % col[0].decode()  for col in toCols])
						ins = """ 
insert into {0} ( {1} )
select distinct {2}
from {3} tmid LEFT JOIN {0} ta ON ta.{4} = tmid.{4}
AND ta.{5} = tmid.{5}
AND ta.AsOfTo = tmid.AsOfTo
where ta.MD5 <> tmid.MD5
OR ta.{4} is NULL 
""".format(table_name, ',\n  '.join([col[0].decode() for col in toCols]), tmpCols, tmpTbl, toCols[0][0].decode(), toCols[1][0].decode())
						psql(ins)
						inserted = toDB.exec_dml(ins , trans = to_conn, commit = False)
						pfmtd([dict(Inserted = inserted)])
					else:
						tmpCols= ',\n  '.join(['tmid.%s' % col[0].decode()  for col in toCols])
						ins = """ 
insert into {0} ( {1} )
select distinct {2}
from {3} tmid LEFT JOIN {0} ta ON ta.{4} = tmid.{4}
AND ta.AsOfTo = tmid.AsOfTo
where ta.MD5 <> tmid.MD5
OR ta.{4} is NULL ;
""".format(table_name, ',\n  '.join([col[0].decode() for col in toCols]), tmpCols, tmpTbl, toCols[0][0].decode())
						psql(ins)
						inserted = toDB.exec_dml(ins , trans = to_conn, commit = False)
						pfmtd([dict(Inserted = inserted)])
					
				if 1:
					toDB.commit_transaction ( trans	= to_conn)

					pfmt([[k]+list(v.values())[1:]  for k,v in pkstats.items() ], ['Table', 'Accepted', 'Rejected','Line count','Skip', 'Diff'],'Load completed'.upper())
					pfmt([(k,v) for k, v in loaded.items()], ['Loaded Files','Loaded Tables'])
					pfmt([(k,v) for k, v in not_loaded.items()], ['Not loaded Files','Not loaded Tables'])
					assert os.path.isdir(okdir)
					if 0:
						cli.MoveSnapFolder(okdir)
					processed.append(dict(ProcessedFile=okfn))
				#break;
				
			if not ok_files.file_names:
				pfmtd([dict(NoFiles= 'No OK files at working dir: [ %s ]' % cli.pa[0])])
				
			pfmtd(processed)
			pfmtd(not_processed)
			
	if 0:
		email_args.update(dict(cli_stats=None))
		Email.send_email( **email_args )
		cli.done()
		





