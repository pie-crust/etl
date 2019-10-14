#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake





python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/file_load/file_lite/ME_FinancingPosition.json --proc_params  \
/auto/fina-datadev/share/PositionModel/ME_FinancingPosition/2019-8-31/




python ~/litecli/main.py dump/lite/20190829_160315/SQLite.db

PRAGMA table_info([Barrier])










 




