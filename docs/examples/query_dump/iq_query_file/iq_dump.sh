#!/bin/sh

alias python=~/python27/bin/python

. ~/.FARprofile
. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


cat in/iq_sql.sql
select StageID, count(1) cnt from CIGActgS11.DMBalance where StageID in (184990,184991) group by StageID


time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/query_dump/iq_query_file/iq_dump.json --proc_params   \
in/iq_test.sql './dump/10' -ld 10


cat ./dump/10/IQ.iq_sql.sql.20190712_113846.csv
StageID:int|cnt:long
184990|922269
184991|6837970


time python cli.py  -nopp 2 -rte DEV -dcf config/db_config.DEV.json -pcf config/proc/data_dump/iq_file/data_dump.json --proc_params \
CIGActgH.PSJournalEntry "WHERE ValidFrom >= DATE('06-01-19')
