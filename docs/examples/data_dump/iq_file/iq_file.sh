#!/bin/sh

alias python=~/python27/bin/python

. ~/.FARprofile
. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake

time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/sync/iq_mem_sql/delta_load.json --proc_params   \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'"  Accounting.CIGActgH.HydraPNLEntries