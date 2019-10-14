#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake

./cli -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/vertica/dir_gtx_vertica/gtx.json --proc_params  \
./gtx  

--workingDir 
--serviceName gtx














 




