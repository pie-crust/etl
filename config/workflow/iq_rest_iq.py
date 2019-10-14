cli, conn_pool=app_init
import sys
from collections import OrderedDict
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit


	


Email 		= create_actor (aname ='Email',app_init=app_init )


insert_stats= InOut(inserted_cnt=-1)


email_args={'email_subject':'IQ->REST->IQ'}




from_conn  = InOut()
trans_ids = InOut()
rest_pipe = InOut()


to_conn	= InOut()


def run():
	lite_tbl={}
	stats={}
	
	for _source, val in cli.cfg['source'].items():
		cli.set_source(_source)
		_src_class = list(val.keys())[0]
		cli.scfg= scfg=cli.get_scfg(_src_class)

		_dbname=cli.scfg["sourceDb"]
		fromDB 		= create_reader(aname =_src_class, app_init=app_init )
		fromDB.begin_transaction  ( env =cli.scfg['sourceDb'] , out = from_conn )
		print fromDB.conn
		fromDB.open_query_cur	( dbcfg = cli.scfg, qname = 'RefCode_sourceStmt', out=from_conn )
		if 1: #REST
			for _rest, val in cli.cfg['rest'].items():
				cli.set_rest(_rest)
				_rest_class = list(val.keys())[0]
				
				cli.rcfg= rcfg=cli.get_rcfg(_rest_class)
			pp(cli.rcfg)
			REST = create_reader(aname =_rest_class, app_init=app_init )
			REST.read_stream	 		( pipe  = from_conn, skip_header = 0, 	out=trans_ids)
			
			
		if 1: #//Load data
			for _trg_class, val in cli.cfg['target'][_source].items() or []:
			
				cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)
				
				_dbname = tcfg["targetDb"]
				toDB 	= create_writer (aname =_trg_class,	app_init=app_init )
				
				toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
				
				table='%s.%s' % (tcfg['targetSchema'], tcfg['targetTable'])
				toDB.desc_table(schema=tcfg['targetSchema'], tbl=tcfg['targetTable'], col_ord=False)
				
				REST.open_stream ( source= cli.rcfg, skip_header = 0, trans_ids=trans_ids, out = rest_pipe )
				toDB.insert_trans_data ( trans	= to_conn, target = cli.tcfg, source = rest_pipe, stmt = 'insertStmt' )
				toDB.commit_transaction( trans	= to_conn )
						
						
				
		if 0:
			cli.set_source(_source)

			fromDB.begin_transaction  ( env =cli.scfg['sourceDb'] , out = from_conn )
			for _dmp_class, val in cli.cfg['dump'][_source].items() or []:
				FileWriter 	= create_writer(aname =_dmp_class,	app_init=app_init )
				fromDB.set_loader(FileWriter)
				cli.dcfg= dcfg=cli.get_dcfg(_dmp_class)				
				for _trg_class, val in cli.cfg['target'][_source].items() or []:
					cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)
					file_ins_cnt= 0
					total_ins= 0
					
				
				stats['%s->%s' % (_dbname, _todbname)] =st=  OrderedDict()
				st['source_cnt']		= cli.get_src_row_count(DB) if not cli.lame_duck else cli.lame_duck
				st['total_extracted'] 	= total_ins
				st['total_inserted'] 	= insert_stats.inserted_cnt
	if 0:
		for k, v in stats.items():
			assert v['source_cnt'] == v['total_extracted'], " %s <> %s" % ( v['source_cnt'], v['total_extracted'])
			assert v['source_cnt'] == v['total_inserted']
		
	if 0:
		email_args.update(dict(cli_stats=stats))
		Email.send_email( **email_args)




		
		

def run0():	
	Snowflake_rdr.open_stream	( dbcfg = cli.scfg, qname = 'RefCode_sourceStmt', out=snow_cur )
	REST.read_stream	 		( pipe  = snow_cur, skip_header = 0, 	out=trans_ids)
	Snowflake.begin_transaction ( out	= snow_conn )
	REST.open_stream	 		( source= cli.rcfg, skip_header = 0, 	trans_ids=trans_ids, out = rest_pipe )
	Snowflake.purge_data		( trans	= snow_conn, source = cli.tcfg, stmt = 'purgeStmt' )
	Snowflake.insert_data		( trans	= snow_conn, target = cli.tcfg, source	= rest_pipe, stmt = 'insertStmt' )
	Snowflake.commit_transaction( trans	= snow_conn )
	Email.send_email			( **email_args )




