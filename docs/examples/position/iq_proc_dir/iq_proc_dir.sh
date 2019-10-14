#!/bin/sh

alias python=~/python27/bin/python


. ~/.FARprofile
. ~/ab_ssrs_reporting_services/.envs/.odbc
. ~/ab_ssrs_reporting_services/.envs/.DEV.Snowflake

#DY_Position_SD
time python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir/DY_Position_SD.json --proc_params  \
223906 05/31/2019 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 4


