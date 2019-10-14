#!/bin/sh
set -e

#DY_POSITION_SD (ACCT, 2019-06-12, 223906 & 223907)
#DY_POSITION_TD (ACCT & DESK, 6-12-19, 223906 & 223907)




alias python=~/python27/bin/python

#DY_Position_SD
time python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_SD.json --proc_params  \
223907 '2019-06-12' 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" \
 2>&1| tee DY_Position_SD_223907.log

 
 #DY_Position_SD
time python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_SD.json --proc_params  \
223906 '2019-06-12' 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" \
 2>&1| tee DY_Position_SD_223906.log
 
 

#DY_Position_TD
time python cli.py -nopp 27  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_TD.json --proc_params \
223907 'EOD' '2019-06-12' 'ACCT' '*' 'DEFAULT' 'REGULAR' '1' '0' 'NONE' '*' '*' 'N' '0' '0' 'NONE' 'NONE' 'ALL' '0' 'MONTH_END' 'N' 'ALL' '*' '0' '*' 'N' '*' \
 2>&1| tee DY_Position_TD_223906_acct.log
 
#DY_Position_TD
time python cli.py -nopp 27  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_TD.json --proc_params \
223906 'EOD' '2019-06-12' 'ACCT' '*' 'DEFAULT' 'REGULAR' '1' '0' 'NONE' '*' '*' 'N' '0' '0' 'NONE' 'NONE' 'ALL' '0' 'MONTH_END' 'N' 'ALL' '*' '0' '*' 'N' '*' \
 2>&1| tee DY_Position_TD_223906_acct.log
 

 
 
#DY_Position_TD
time python cli.py -nopp 27  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_TD.json --proc_params \
223907 'EOD' '2019-06-12' 'DESK' '*' 'DEFAULT' 'REGULAR' '1' '0' 'NONE' '*' '*' 'N' '0' '0' 'NONE' 'NONE' 'ALL' '0' 'MONTH_END' 'N' 'ALL' '*' '0' '*' 'N' '*' \
 2>&1| tee DY_Position_TD_223907_desk.log
 
#DY_Position_TD
time python cli.py -nopp 27  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_TD.json --proc_params \
223906 'EOD' '2019-06-12' 'DESK' '*' 'DEFAULT' 'REGULAR' '1' '0' 'NONE' '*' '*' 'N' '0' '0' 'NONE' 'NONE' 'ALL' '0' 'MONTH_END' 'N' 'ALL' '*' '0' '*' 'N' '*' \
 2>&1| tee DY_Position_TD_223906_desk.log
 