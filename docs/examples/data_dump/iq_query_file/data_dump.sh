#!/bin/sh

alias python=~/python27/bin/python

. ~/.FARprofile
. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake

time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/data_dump/iq_file/data_dump.json --proc_params   \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'" 

wc -l /auto/dbdumps_PMT_Snow/delta_dumps/IQ.20190711_143832.csv


time python cli.py  -nopp 2 -rte DEV -dcf config/db_config.DEV.json -pcf config/proc/data_dump/iq_file/data_dump.json --proc_params \
CIGActgH.PSJournalEntry "WHERE ValidFrom >= DATE('06-01-19')
