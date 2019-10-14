#!/bin/sh

alias python=~/python27/bin/python

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '03/01/2016' '03/01/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:01: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:01: DY_DeskPLRSRange03: Failed." 
fi


