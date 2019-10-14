"""
 time python cli.py -nopp 1 -dcf config/db_config.json -pcf config/proc/file_s3_snow/DY_Position_SD.json --proc_params  \
 test.csv.gz -ld 100\
 2>&1| tee DY_Position_SD.log
"""
import threading
import subprocess
from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init



Snowflake 	= create_writer('Snowflake',  app_init=app_init	) 
S3			= create_writer('S3', app_init=app_init			)
Email 	  	= create_actor ('Email', app_init=app_init 		)



s3_file_names	= InOut()
snow_conn		= InOut()

##
##
email_args={'email_subject':'File->Snowflake'}
##
##
threads={}
s3_file_names.file_names=[]


	
	
def run():	
	
	Snowflake.begin_transaction ( out = snow_conn )	
	assert isinstance(cli.pa,(str, unicode)), 'Provide only file name you want to upload in [--proc_params]'

	fname=cli.pa
	s3_file_names.file_names
	assert os.path.isfile(fname), 'Upload file "%s" does not exists.' % fname
	if 1:
		to_fn='%s.gz' % fname
		S3.compress_file(fname, to_fn)
		S3.upload_file(to_fn)
		s3_file_names.file_names.append(to_fn)
	if 1:
		
		
		Snowflake.begin_transaction ( out = snow_conn )	
		#Snowflake.purge_data		( trans	= snow_conn, stmt = 'purgeStmt' )
		Snowflake.bulk_copy			( trans	= snow_conn, file_names = s3_file_names, target=cli.tcfg, qname = 'copyStmt')
		Snowflake.commit_transaction( trans	= snow_conn )
	if 0:
		S3StreamLoader.delete_files ( file_names=s3_file_names)
		Email.send_email			( **email_args )


