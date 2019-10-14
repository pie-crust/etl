#!/bin/sh

alias python=~/python27/bin/python

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/01/2016' '01/01/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:01: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:01: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/01/2016' '01/01/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:01: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:01: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/02/2016' '01/02/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:02: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:02: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/02/2016' '01/02/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:02: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:02: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/03/2016' '01/03/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:03: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:03: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/03/2016' '01/03/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:03: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:03: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/04/2016' '01/04/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:04: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:04: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/04/2016' '01/04/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:04: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:04: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/05/2016' '01/05/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:05: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:05: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/05/2016' '01/05/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:05: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:05: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/06/2016' '01/06/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:06: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:06: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/06/2016' '01/06/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:06: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:06: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/07/2016' '01/07/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:07: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:07: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/07/2016' '01/07/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:07: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:07: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/08/2016' '01/08/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:08: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:08: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/08/2016' '01/08/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:08: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:08: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/09/2016' '01/09/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:09: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:09: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/09/2016' '01/09/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:09: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:09: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/10/2016' '01/10/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:10: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:10: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/10/2016' '01/10/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:10: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:10: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/11/2016' '01/11/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:11: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:11: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/11/2016' '01/11/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:11: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:11: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/12/2016' '01/12/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:12: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:12: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/12/2016' '01/12/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:12: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:12: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/13/2016' '01/13/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:13: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:13: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/13/2016' '01/13/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:13: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:13: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/14/2016' '01/14/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:14: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:14: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/14/2016' '01/14/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:14: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:14: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/15/2016' '01/15/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:15: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:15: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/15/2016' '01/15/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:15: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:15: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/16/2016' '01/16/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:16: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:16: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/16/2016' '01/16/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:16: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:16: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/17/2016' '01/17/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:17: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:17: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/17/2016' '01/17/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:17: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:17: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/18/2016' '01/18/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:18: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:18: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/18/2016' '01/18/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:18: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:18: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/19/2016' '01/19/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:19: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:19: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/19/2016' '01/19/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:19: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:19: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/20/2016' '01/20/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:20: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:20: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/20/2016' '01/20/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:20: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:20: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/21/2016' '01/21/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:21: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:21: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/21/2016' '01/21/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:21: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:21: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/22/2016' '01/22/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:22: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:22: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/22/2016' '01/22/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:22: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:22: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/23/2016' '01/23/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:23: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:23: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/23/2016' '01/23/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:23: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:23: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/24/2016' '01/24/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:24: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:24: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/24/2016' '01/24/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:24: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:24: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/25/2016' '01/25/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:25: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:25: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/25/2016' '01/25/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:25: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:25: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/26/2016' '01/26/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:26: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:26: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/26/2016' '01/26/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:26: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:26: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/27/2016' '01/27/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:27: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:27: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/27/2016' '01/27/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:27: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:27: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/28/2016' '01/28/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:28: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:28: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/28/2016' '01/28/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:28: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:28: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/29/2016' '01/29/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:29: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:29: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/29/2016' '01/29/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:29: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:29: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/30/2016' '01/30/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:30: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:30: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/30/2016' '01/30/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:30: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:30: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '01/31/2016' '01/31/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:31: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:Jan:31: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '01/31/2016' '01/31/2016'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:Jan:31: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:Jan:31: DY_DeskPLRSRange03:223906: Failed." 
fi
	


