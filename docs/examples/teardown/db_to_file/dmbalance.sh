#!/bin/sh

alias python=~/python27/bin/python

. ~/.FARprofile
. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


in/tear.IQ.dev_vs_prod.py ./dump/33 ./dump/lite/  email-y show-y


time python cli.py -nopp 5 -dcf config/db_config.DEV.json -pcf config/proc/teardown/db_to_file/dmbalance.json --proc_params \
in/tear.db_to_file.py ./dump/33 ./dump/lite/  email-y show-y







cat ./dump/10/IQ.iq_sql.sql.20190712_113846.csv
StageID:int|cnt:long
184990|922269
184991|6837970


time python cli.py  -nopp 2 -rte DEV -dcf config/db_config.DEV.json -pcf config/proc/data_dump/iq_file/data_dump.json --proc_params \
CIGActgH.PSJournalEntry "WHERE ValidFrom >= DATE('06-01-19')
