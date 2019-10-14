#!/bin/sh
set -e
alias python=~/python27/bin/python


#DY_FinancingPosition
time python cli.py -nopp 12  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_FinancingPosition.json --proc_params \
223907 05/31/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 1 \
 2>&1| tee DY_FinancingPosition.log


#ME_FinancingPosition
time python cli.py -nopp 12 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/ME_FinancingPosition.json --proc_params \
223907 05/01/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 1 \
 2>&1| tee ME_FinancingPosition.log
 
 
 
#DY_FinancingPosition
time python cli.py -nopp 12  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_FinancingPosition.json --proc_params \
223906 05/31/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 1 \
 2>&1| tee DY_FinancingPosition.log


#ME_FinancingPosition
time python cli.py -nopp 12 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/ME_FinancingPosition.json --proc_params \
223906 05/01/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 1 \
 2>&1| tee ME_FinancingPosition.log
 
 