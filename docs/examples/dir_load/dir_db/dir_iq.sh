#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake



#extract
time python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir/DY_Position_SD.json --proc_params \
223906 2019/05/31 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 3

#load
time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_iq/DY_Position_SD.json --proc_params  \
/auto/fina-datadev/share/PositionModel/20190724_084042/ DY_Position_SD 













 




