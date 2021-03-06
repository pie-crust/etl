"""
time python cli2.py -nopp 18 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_SD.json --proc_params  \
223906 05/30/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 100\
 2>&1| tee DY_Position_SD.log 
"""
from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init


IQ 				= create_reader('IQ',  app_init=app_init			)
Snowflake 		= create_writer('Snowflake',  app_init=app_init		) 
S3StreamLoader	= create_writer('S3StreamLoader', app_init=app_init )
Email 	  		= create_actor ('Email', app_init=app_init 			)


IQ_cursor		= InOut()
s3_file_names	= InOut()
snow_conn		= InOut()
iq_data			= InOut()
file_size_rows=100000
##
##
email_args={'email_subject':'IQ->Snowflake'}
##
##

def run():	
	IQ.set_loader(Snowflake)
	for data in IQ.fetch_many(chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=iq_data,skip_header=0):	
		S3StreamLoader.upload_data	(data=iq_data, target=cli.s3cfg, out=s3_file_names )
	
	if 1:
		Snowflake.begin_transaction ( out = snow_conn )	
		Snowflake.purge_data		( trans	= snow_conn, stmt = 'purgeStmt' )
		Snowflake.bulk_copy			( trans	= snow_conn, file_names = s3_file_names, target=cli.tcfg, qname = 'copyStmt')
		Snowflake.commit_transaction( trans	= snow_conn )
		
	S3StreamLoader.delete_files ( file_names=s3_file_names)
	Email.send_email			( **email_args )




