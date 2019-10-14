#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_db/dir_iq.json --proc_params  \
/auto/dbdumps_PMT_Snow/delta_dumps/20190719_141700/ DY_Position_SD -ld 10 



time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_db/dir_iq.json --proc_params  \
./dump/delta_dumps/20190722_145600/ DY_Position_SD -ld 10 

#extract
time python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir/DY_Position_SD.json --proc_params \
223906 2019/05/31 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 4000

#load
time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_db/dir_iq.json --proc_params  \
./dump/delta_dumps/20190723_163700/ DY_Position_SD 













 




