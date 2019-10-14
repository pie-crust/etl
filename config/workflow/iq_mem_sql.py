"""
time python cli.py -nopp 3 -dcf config/db_config.DEV.json \
-pcf config/proc/sync/iq_mem_sql/delta_load.json --proc_params   \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2016-06-19'"  Accounting.CIGActgH.HydraPNLEntries \
 
 2>&1| tee delta_load.log 
"""

import sys
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


IQ 				= create_reader('IQ',			app_init=app_init )
SQLServer 		= create_writer('SQLServer',	app_init=app_init ) 
Email 	  		= create_actor ('Email',		app_init=app_init )



sql_conn		= InOut()
#iq_data			= InOut()

file_size_rows=10000
email_args={'email_subject':'IQ->SQL'}


SQLServer.begin_transaction ( out 	= sql_conn )
cli.set_target_cols(SQLServer)


def run():	
	IQ.set_loader(SQLServer)
	
	total_ins= 0
	for iq_data in IQ.fetch_many(chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=InOut(),skip_header=0):


		SQLServer.insert_array		( trans	= sql_conn, target = cli.tcfg, data = iq_data, stmt = 'insertStmt' )
		
		SQLServer.commit_transaction( trans	= sql_conn )
		total_ins+=len(iq_data.data)
		
		
	
	log.info('SQLServer: Inserted:%d' % total_ins)
	SQLServer.commit_transaction( trans	= sql_conn, close_conn=True)
	if 1:
		Email.send_email			( **email_args )




