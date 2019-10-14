#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


time /tmp/python3/bin/python3 cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/vertica/dir_grds_vertica/grds.json --proc_params  \
./legacy/grds  

--workingDir 
--serviceName gtx














 




