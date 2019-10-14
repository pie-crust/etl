#!/bin/sh

alias python=~/python27/bin/python

. ~/.FARprofile
. ~/ab_ssrs_reporting_services/.envs/.odbc
. ~/ab_ssrs_reporting_services/.envs/.DEV.Snowflake

time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/db_file_db_mp_async/iq_file_sql_mp_async.json --proc_params  \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" Accounting.CIGActgH.HydraPNLEntries -ld 10

wc -l /auto/dbdumps_PMT_Snow/delta_dumps/IQ.20190711_143832.csv


