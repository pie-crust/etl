"""
time python cli2.py -nopp 18 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_SD.json --proc_params  \
223906 05/30/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 100\
 2>&1| tee DY_Position_SD.log 
"""
from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init


#IQ 				= create_reader('IQ',  app_init=app_init			)
#Snowflake 		= create_writer('Snowflake',  app_init=app_init		) 
#S3StreamLoader	= create_writer('S3StreamLoader', app_init=app_init )
Email 	  		= create_actor ('Email', app_init=app_init 			)


IQ_cursor		= InOut()
s3_file_names	= InOut()
snow_conn		= InOut()

##
##
email_args={'email_subject':'IQ->Snowflake'}
##
##
from_conn	= InOut()
def run():	
	for _source, val in cli.cfg['source'].items():
		cli.set_source(_source)
		_src_class = val.keys()[0]
		cli.scfg= cli.get_scfg(_src_class)
		_dbname=cli.scfg["sourceDb"]
		fromDB 			= create_reader(_src_class,	app_init=app_init )
		fromDB.begin_transaction  ( env =cli.scfg['sourceDb'] , out = from_conn )
		for _s3_class, val in cli.cfg['s3'][_source].items() or []:
			cli.s3cfg= cli.get_s3cfg(_s3_class)
			S3StreamLoader 	= create_writer(_s3_class,	app_init=app_init ) 
			for _trg_class, val in cli.cfg['target'][_source].items() or []:
				cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)
				TOdb = create_writer(_trg_class,  app_init=app_init) 
				fromDB.set_loader(TOdb)
				cli.proc_config()
				fromDB.open_stream				( dbcfg = cli.scfg, qname = 'sourceStmt', out=IQ_cursor )
				S3StreamLoader.load_stream	( source=IQ_cursor,skip_header=0,  out=s3_file_names )
				if 1:
					TOdb.begin_transaction  ( env =cli.tcfg['targetDb'], out = snow_conn )
					TOdb.purge_data			( trans	= snow_conn, stmt = 'purgeStmt' )
					TOdb.bulk_copy			( trans	= snow_conn, file_names = s3_file_names, target=cli.tcfg, qname = 'copyStmt', )
					TOdb.commit_transaction ( trans	= snow_conn )
					
				S3StreamLoader.delete_files ( file_names=s3_file_names)

		
	if 0:
		IQ.set_loader(Snowflake)
		
		IQ.open_stream				( dbcfg = cli.scfg, qname = 'sourceStmt', out=IQ_cursor )
		S3StreamLoader.load_stream	( source=IQ_cursor,skip_header=0,  out=s3_file_names )
		#fromDB.commit_transaction ( trans	= from_conn)
		pp(cli.tcfg)
		Snowflake.begin_transaction ( env =cli.tcfg['targetDb'], out = snow_conn )
		Snowflake.purge_data		( trans	= snow_conn, stmt = 'purgeStmt' )
		Snowflake.bulk_copy			( trans	= snow_conn, file_names = s3_file_names, target=cli.tcfg, qname = 'copyStmt', )
		Snowflake.commit_transaction( trans	= snow_conn )
		S3StreamLoader.delete_files ( file_names=s3_file_names)
	if 0:
		Email.send_email			( **email_args )
		cli.done					()




