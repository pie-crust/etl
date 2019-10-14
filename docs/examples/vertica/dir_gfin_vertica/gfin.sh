#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


time ./cli -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/vertica/dir_gfin_vertica/gfin.json --proc_params  \
./gfin  

--workingDir 
--serviceName gtx














 




