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


SQLServer 			= create_reader('SQLServer',	app_init=app_init )
FileWriter 	= create_writer('File',	app_init=app_init ) 
Email 		= create_actor ('Email',app_init=app_init )



sql_conn		= InOut()
dump_file		= InOut()

file_size_rows=250000
email_args={'email_subject':'SQL-q->File'}

def run():

	SQLServer.set_loader(FileWriter)
	
	total_ins= 0
	FileWriter.open_file( out = dump_file )
	
	for iq_data in SQLServer.fetch_many ( chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=InOut(), skip_header=0 ):
		if not total_ins:
			FileWriter.create_header(file = dump_file, header = SQLServer.get_header())
		FileWriter.append_data ( file = dump_file,  data = iq_data)
		total_ins+=len(iq_data.data)
	if not total_ins: #in case there's no data
		FileWriter.create_header(file = dump_file, header = SQLServer.get_header())
	FileWriter.close_file(file = dump_file)
	
	if 0:
		Email.send_email( **email_args )




