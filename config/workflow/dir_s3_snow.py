"""
 time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/file_load/dir_s3_snow/journalline.json --proc_params \
 /auto/dbdumps_PMT_Snow/load_test/ \
 2>&1| tee DY_Position_SD.log
 
  time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/file_load/dir_s3_snow/journalline.json --proc_params  \
  /auto/dbdumps_PMT_Snow/load_test_2/ 2>&1| tee logs/load_test_2.log

  
  
"""
import sys
import threading
import subprocess
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


Dir 		= create_reader('Dir', 			app_init=app_init ) 
S3			= create_writer('ParallelS3', 	app_init=app_init )
Snowflake 	= create_writer('Snowflake',  	app_init=app_init ) 
Email 	  	= create_actor ('Email', 		app_init=app_init )


data_files		= InOut()
chunked_data_files	= InOut()
sql_files		= InOut()
s3_data_keys	= InOut()
snow_conn		= InOut()

##
##
email_args={'email_subject':'File->Snowflake'}
##
##

data_files.file_names=[]
s3_data_keys.file_names=[]


	
	
def run():	
	#S3.delete_file('racct/auto/dbdumps_PMT_Snow/tiny_test/100.csv.0.gz')
	#e()
	Dir.get_files			( out = data_files )
	skip_header = cli.scfg.get('skip_header', 0)
	rec_delim = cli.scfg.get('record_delimiter', os.linesep)

	
	S3.upload_files			( file_names = data_files, out = s3_data_keys, skip_header=skip_header, rec_delim=rec_delim)
	print Dir.uploaded
	#pp(s3_data_keys.file_names)
	#print s3_data_keys.file_location
	#e()
	#cli.file_location=os.sep.join(file_names.file_location.split(os.sep)[1:])
	#assert cli.file_location
	if 1:
		Snowflake.begin_transaction ( out 	= snow_conn )
		Snowflake.bulk_copy			( trans	= snow_conn, file_names = s3_data_keys, target=cli.tcfg, qname = 'copyStmt')
		Snowflake.commit_transaction( trans	= snow_conn )
	if 1:
		S3.delete_files ( file_names=s3_data_keys )
		#Email.send_email( **email_args )


