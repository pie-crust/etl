#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_db/dir_snow.json --proc_params  \
/auto/dbdumps_PMT_Snow/delta_dumps/20190719_141700/ DY_Position_SD -ld 10 








 




