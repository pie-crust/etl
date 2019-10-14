
#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake



#extract
time python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir/DY_Position_SD.json --proc_params \
223906 2019/05/31 'EOD' 'ACCT' "HORZ" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 3

#load
time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_iq/DY_Position_SD.json --proc_params  \
/auto/fina-datadev/share/PositionModel/20190724_084042/ DY_Position_SD 





#DY_Position_SD
time python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir_lite/DY_Position_SD.json --proc_params \
223906 2019/05/31 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 5


#ME_13F
time python cli.py -nopp 12  -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir_lite/ME_13F.json --proc_params \
'2019/03/31' 223907 "EOD" '*' '0' 'ALL' 'DETAIL' '*' 0 'N' 'N' 'N'  -ld 33





python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params \
223907 '2016/12/07' '2016/12/07'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'


~/python27/bin/python cli.py -nopp 18  --no-dump  -dcf config/db_config.DEV.json -pcf config/proc/pnl/iq_proc_dir_lite/DY_DeskPLRSRange03.json --proc_params \
223906 '2016/12/07' '2016/12/07'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'

