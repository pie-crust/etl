#!/bin/sh

alias python=~/python27/bin/python
. ~/.FARprofile
. ~/ab_ssrs_reporting_services/.envs/.odbc
. ~/ab_ssrs_reporting_services/.envs/.DEV.Snowflake
. ~/ab_ssrs_reporting_services/.envs/.DEV.IQ

#DY_FinancingPosition
time python cli.py -nopp 12  -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir_iq/DY_FinancingPosition.json --proc_params \
223907 2019/05/31 2019/05/31 EOD EOD 'HORZ' '*' '*' NONE '*' NOW 0 



#ME_FinancingPosition
time python cli.py -nopp 12 -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir_iq/ME_FinancingPosition.json --proc_params \
223907 2019/05/01 2019/05/31 EOD EOD '*' '*' '*' NONE '*' NOW 0  




#ME_13F
time python cli.py -nopp 12  -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir_iq/ME_13F.json --proc_params \
'2019/03/31' 223907 "EOD" '*' '0' 'ALL' 'DETAIL' '*' 0 'N' 'N' 'N' 






