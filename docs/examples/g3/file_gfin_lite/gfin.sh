#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


time ./cli -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/file_gfin_lite/gfin.json --proc_params  \


 ~/python27/bin/python2 cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/file_gfin_lite/gfin.json --proc_params  ./gfin




python ~/litecli/main.py dump/lite/20190829_160315/SQLite.db

PRAGMA table_info([Barrier])










 




