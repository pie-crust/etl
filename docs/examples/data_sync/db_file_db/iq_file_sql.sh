#!/bin/sh

alias python=~/python27/bin/python

. ~/.FARprofile
. ~/ab_ssrs_reporting_services/.envs/.odbc
. ~/ab_ssrs_reporting_services/.envs/.DEV.Snowflake

time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/data_dump/db_file_db/iq_file_sql.json --proc_params  \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'"  -ld 11

wc -l /auto/dbdumps_PMT_Snow/delta_dumps/IQ.20190711_143832.csv


time python cli.py -nopp 3 -rte PROD -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db/iq_file_sql.json --proc_params \
CIGActgH.AdjustmentPostStatus "where AdjPSBatchID = 'ADJ0369017'"  Accounting.CIGActgH.AdjustmentPostStatus


time python cli.py -nopp 3 -rte PROD -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db/iq_file_sql.json --proc_params \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries -ld 10




time python cli.py -nopp 3 -rte PROD -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db_mp/iq_file_sql_mp.json --proc_params \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries -ld 5000


time python cli.py -nopp 3 -rte PROD -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db_mp/db_file_db_mp.json --proc_params \
CIGActgH.AdjustmentPostStatus "where 1=1"  Accounting.CIGActgH.AdjustmentPostStatus -ld 10


 time python cli.py -nopp 3 -rte PROD -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db/iq_file_sql.json --proc_params \
 CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries -ld 30000





time python cli.py -nopp 3 -rte PROD -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db/iq_file_sql.json --proc_params \
CIGActgH.AdjustmentPostStatus "where AdjPSBatchID = 'ADJ0369017'"  Accounting.CIGActgH.AdjustmentPostStatus

#PAsync
time python cli.py -nopp 3 -rte PROD -dcf config/db_config.PROD.json -pcf config/proc/data_sync/db_file_db_mp/iq_file_sql_mp.json --proc_params \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries -ld 5000


time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/db_file_db/iq_file_sql.json --proc_params  \
CIGActgH.AdjustmentPostStatus "where AdjPSBatchID = 'ADJ0369017'"  Accounting.CIGActgH.AdjustmentPostStatus 

