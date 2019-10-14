#!/bin/sh

alias python=~/python27/bin/python

#DY_FinancingPosition
time python cli.py -nopp 12  -dcf config/db_config.json -pcf config/proc/pos/sql_stream_s3_snow/DY_FinancingPosition.json --proc_params \
223906 05/31/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 0 \
 2>&1| tee DY_FinancingPosition.log


#ME_FinancingPosition
time python cli.py -nopp 12 -dcf config/db_config.json -pcf config/proc/pos/sql_stream_s3_snow/ME_FinancingPosition.json --proc_params \
223906 05/01/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 0 \
 2>&1| tee ME_FinancingPosition.log


#ME_13F
time python cli.py -nopp 12  -dcf config/db_config.json -pcf config/proc/pos/sql_stream_s3_snow/ME_13F.json --proc_params \
'03/31/2019' 223906 "EOD" '*' '0' 'ALL' 'DETAIL' '*' 0 'N' 'N' 'N' \
 2>&1| tee ME_13F.log





