#!/bin/sh

alias python=~/python27/bin/python

#DY_FinancingPosition
time python cli.py -nopp 12  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_FinancingPosition.json --proc_params \
223906 05/31/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 0 \
 2>&1| tee DY_FinancingPosition.log


#ME_FinancingPosition
time python cli.py -nopp 12 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/ME_FinancingPosition.json --proc_params \
223906 05/01/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 0 \
 2>&1| tee ME_FinancingPosition.log


#DY_Position_SD
time python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_SD.json --proc_params  \
223906 05/31/2019 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" \
 2>&1| tee DY_Position_SD.log

#ME_Position_SD
time python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/ME_Position_SD.json --proc_params \
223906 05/31/2019 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" \
 2>&1| tee ME_Position_SD.log


#ME_13F
time python cli.py -nopp 12  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/ME_13F.json --proc_params \
'03/31/2019' 223906 "EOD" '*' '0' 'ALL' 'DETAIL' '*' 0 'N' 'N' 'N' \
 2>&1| tee ME_13F.log

#DY_Position_TD
time python cli.py -nopp 27  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_TD.json --proc_params \
223906 'EOD' '05/31/2019' 'ACCT' '*' 'DEFAULT' 'REGULAR' '1' '0' 'NONE' '*' '*' 'N' '0' '0' 'NONE' 'NONE' 'ALL' '0' 'MONTH_END' 'N' 'ALL' '*' '0' '*' 'N' '*' \
 2>&1| tee DY_Position_TD.log


#ME_Position_TD
time python cli.py -nopp 27 --no-dump  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/ME_Position_TD.json --proc_params \
223906 'EOD'  '05/31/2019' 'ACCT' '*' 'DEFAULT' 'REGULAR' '1' '0' 'NONE' '*' '*' 'N' '0' '0' 'NONE' 'NONE' 'ALL' '0' 'FULL' 'N' 'ALL' '*' '0' '*' 'Y' '*' \
 2>&1| tee ME_Position_TD.log
 




