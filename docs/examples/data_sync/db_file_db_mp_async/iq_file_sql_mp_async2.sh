#!/bin/sh

alias python=~/python27/bin/python

. ~/.FARprofile
. ~/ab_ssrs_reporting_services/.envs/.odbc
. ~/ab_ssrs_reporting_services/.envs/.DEV.Snowflake


# Serial (DOP=1)
time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/db_file_db/iq_file_sql.json --proc_params   \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries
 
 
real    30m59.270s
user    1m51.389s
sys     0m6.020s


#Parallel (default DOP = 6 [multiprocessing.cpu_count()/4])
time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/db_file_db_mp_async/iq_file_sql_mp_async.json --proc_params  \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries


real    8m33.463s
user    1m51.037s
sys     0m7.812s



# DOP =12 
time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/db_file_db_mp_async/iq_file_sql_mp_async.json --proc_params  \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries -dop 12



real    6m20.389s
user    1m52.708s
sys     0m8.529s


# DOP =24 
time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/db_file_db_mp_async/iq_file_sql_mp_async.json --proc_params  \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries -dop 24

real    4m51.430s
user    1m50.613s
sys     0m9.163s


time python cli.py -nopp 3 -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db_mp_async/iq_file_sql_mp_async.json --proc_params  \
CIGActgH.HydraPNLEntries "where LastModifiedTime > '2019-07-16'"  Accounting.CIGActgH.HydraPNLEntries

where LastModifiedTime > '2019-07-16'


time python cli.py -nopp 3 -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db/iq_file_sql.json --proc_params  \
CIGActgH.HydraPNLEntries "where LastModifiedTime > '2019-07-16'"  Accounting.CIGActgH.HydraPNLEntries






