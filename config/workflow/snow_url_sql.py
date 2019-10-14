from __future__ import print_function
assert app_init
"""
 
  time python cli2.py -nopp 4  -dcf config/db_config.json -pcf config/proc/snow_url_sql/DY_FinancingPosition.json \
 --proc_params  Repo '2018-12-31 00:00:00' "$(date +"%Y-%m-%d %H:%M:%S")" e5569eb7-e333-4e28-ad77-0f224a7d2499@1
#
# pa[0] = ReferenceType
# pa[1] = AccountingDate
# pa[2] = AsOfDateTime
# pa[3] = gatoken
#


"""

from include.PubSub import NewId, Exec
from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init


Snowflake = create_reader('Snowflake',  app_init=app_init)
REST	  = create_reader('REST', 		app_init=app_init)
SQLServer = create_writer('SQLServer',  app_init=app_init)
Email 	  = create_actor ('Email',  	app_init=app_init)

snow_cur  = InOut()
trans_ids = InOut()
rest_pipe = InOut()
sql_conn   = InOut()

email_args={'email_subject':'Snowflake->REST->SQLServer'}

def run():	
	Snowflake.open_stream		( dbcfg = cli.scfg, qname = 'RefCode_sourceStmt', out=snow_cur )
	REST.read_stream	 		( pipe  = snow_cur, skip_header = 0, 	out=trans_ids)
	SQLServer.begin_transaction ( out=sql_conn )
	REST.open_stream	 		( source= cli.rcfg, skip_header = 0, 	trans_ids=trans_ids, out = rest_pipe )
	SQLServer.purge_data		( trans	= sql_conn, source = cli.tcfg, 	stmt = 'purgeStmt' )
	SQLServer.insert_data		( trans	= sql_conn, target = cli.tcfg, 	source	= rest_pipe, stmt = 'insertStmt' )
	SQLServer.commit_transaction( trans	= sql_conn )
	Email.send_email			( **email_args )




