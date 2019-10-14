#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/file_load/dir_iq/ME_FinancingPosition.json --proc_params  \
/auto/fina-datadev/share/PositionModel/ME_FinancingPosition/2019-8-31/ ME_FinancingPosition -ld 10 

















 




