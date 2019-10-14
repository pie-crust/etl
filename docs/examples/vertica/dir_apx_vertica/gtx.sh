#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/vertica/dir_apx_vertica/gtx.json --proc_params  \
./gtx/gtx.20190729-064109747411  -ld 10 

--workingDir 
--serviceName gtx














 




