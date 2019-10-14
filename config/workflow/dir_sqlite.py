"""

"""
import sys
import threading
import subprocess
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


Dir 	= create_reader('Dir', 		app_init=app_init ) 
SQLite 	= create_writer('SQLite',	app_init=app_init ) 
Email 	= create_actor ('Email', 	app_init=app_init )


data_files	= InOut()
lite_conn	= InOut()

##
##
email_args={'email_subject':'File->SQLite'}
##
##

data_files.file_names=[]



	
	
def run():	

	Dir.get_files			( out = data_files )

	if 1:
		SQLite.begin_transaction ( out 	= lite_conn )
		SQLite.bulk_insert		 ( trans	= lite_conn, file_names = data_files,  qname = 'insertStmt' )
		SQLite.commit_transaction( trans	= lite_conn)
	if 0:
		
		Email.send_email			( **email_args )



