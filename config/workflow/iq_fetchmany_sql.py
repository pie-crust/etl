"""
time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/test/iq_fetchmany_sql/delta_load.json --proc_params  \
 CIGActgH.HydraPNLEntries “WHERE LastModifiedTime>’2016-06-19’”  Accounting.CIGActgH.HydraPNLEntries \
 
 2>&1| tee DY_Position_SD.log 
"""
"""
select * from CIGActgH.HydraClients

SELECT syscolumns.name, systypes.name FROM sysobjects 
JOIN syscolumns ON sysobjects.id = syscolumns.id
JOIN systypes ON systypes.type = syscolumns.type AND systypes.usertype = syscolumns.usertype
WHERE sysobjects.name LIKE 'HydraPNLEntries' 

Select * from systabcol
key join systab
 where table_name = 'HydraPNLEntries'
 order by column_id
 
 
 
 
Select user_name(creator) as 'owner_name' , column_id, column_name from systabcol
key join systab
 where table_name = 'HydraPNLEntries'
 order by column_id
 
 
Select user_name(systabcol.object_id)  as 'owner_name' from systabcol
key join systab
 where table_name = 'HydraPNLEntries'
 order by column_id
 
 
 
 SELECT
DB_NAME() TABLE_CATALOG,
NULL TABLE_SCHEMA,
sc.column_id ORDINAL_POSITION,
NULL COLUMN_DEFAULT,
NULL CHARACTER_SET_CATALOG,
NULL CHARACTER_SET_SCHEMA,
NULL COLLATION_CATALOG,
NULL COLLATION_SCHEMA,
NULL DOMAIN_CATALOG,
NULL DOMAIN_SCHEMA,
NULL DOMAIN_NAME
FROM 
sysobjects so
INNER JOIN 
systabcol sc
ON sc.column_id = so.id
WHERE so.name = 'HydraPNLEntries'

SELECT SCHEMA_NAME();


select u.name as 'owner_name', 
       o.name as 'table_name'
from   sysobjects o,
       sysusers u
where  o.uid  = u.uid
and    o.name = 'HydraPNLEntries'
and    o.type = 'U'


select user_name(o.uid), o.uid as 'owner_name', 
       o.name as 'table_name'
from   sysobjects o
where  o.name = 'HydraPNLEntries'
and    o.type = 'U'
"""

from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init


IQ 				= create_reader('IQ',			app_init=app_init )
SQLServer 		= create_writer('SQLServer',	app_init=app_init ) 
Email 	  		= create_actor ('Email',		app_init=app_init )



sql_conn		= InOut()
#iq_data			= InOut()

file_size_rows=100000
##
##
email_args={'email_subject':'IQ->SQL'}
##
##

def run():	
	IQ.set_loader(SQLServer)
	for iq_data in IQ.fetch_many(chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=InOut(),skip_header=0):

		SQLServer.begin_transaction ( out 	= sql_conn )
		SQLServer.insert_array		( trans	= sql_conn, target = cli.tcfg, data = iq_data, stmt = 'insertStmt' )
		SQLServer.commit_transaction( trans	= sql_conn )

	
	if 0:
		Email.send_email			( **email_args )




