#!/bin/sh

alias python=~/python27/bin/python




python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/01/2016' '05/01/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/01/2016' '05/01/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/02/2016' '05/02/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/02/2016' '05/02/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/03/2016' '05/03/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/03/2016' '05/03/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/04/2016' '05/04/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/04/2016' '05/04/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/05/2016' '05/05/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/05/2016' '05/05/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/06/2016' '05/06/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/06/2016' '05/06/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/07/2016' '05/07/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/07/2016' '05/07/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/08/2016' '05/08/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/08/2016' '05/08/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/09/2016' '05/09/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/09/2016' '05/09/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/10/2016' '05/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/10/2016' '05/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/11/2016' '05/11/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/11/2016' '05/11/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/12/2016' '05/12/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/12/2016' '05/12/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/13/2016' '05/13/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/13/2016' '05/13/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/14/2016' '05/14/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/14/2016' '05/14/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/15/2016' '05/15/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/15/2016' '05/15/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/16/2016' '05/16/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/16/2016' '05/16/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/17/2016' '05/17/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/17/2016' '05/17/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/18/2016' '05/18/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/18/2016' '05/18/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/19/2016' '05/19/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/19/2016' '05/19/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/20/2016' '05/20/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/20/2016' '05/20/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/21/2016' '05/21/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/21/2016' '05/21/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/22/2016' '05/22/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/22/2016' '05/22/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/23/2016' '05/23/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/23/2016' '05/23/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/24/2016' '05/24/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/24/2016' '05/24/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/25/2016' '05/25/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/25/2016' '05/25/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/26/2016' '05/26/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/26/2016' '05/26/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/27/2016' '05/27/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/27/2016' '05/27/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/28/2016' '05/28/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/28/2016' '05/28/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/29/2016' '05/29/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/29/2016' '05/29/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/30/2016' '05/30/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/30/2016' '05/30/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '05/31/2016' '05/31/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:31: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:31: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '05/31/2016' '05/31/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:31: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:31: DY_DeskPLRSRange03:223906: Failed." 
fi
	
