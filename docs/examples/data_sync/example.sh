#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake

time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/sync/iq_mem_sql/delta_load.json --proc_params   \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'"  Accounting.CIGActgH.HydraPNLEntries




time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/sync/iq_mem_sql/delta_load.json --proc_params   \
CIGActgH.PSJournalEntry "WHERE AccountingDate = '2019-06-30' and PSBusinessUnitCode = '22400' and NaturalAccountCode = '115202' and BatchID in ('PS00328047','PS00328048')"  Accounting.CIGActgH.PSJournalEntry

time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/sync/iq_mem_sql/delta_load.json --proc_params   \
CIGActgH.PSJournalEntry "WHERE AccountingDate = '2019-06-30'"  Accounting.CIGActgH.PSJournalEntry

