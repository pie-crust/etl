#!/bin/sh

alias python=~/python27/bin/python




python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/01/2016' '06/01/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/01/2016' '06/01/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/02/2016' '06/02/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/02/2016' '06/02/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/03/2016' '06/03/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/03/2016' '06/03/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/04/2016' '06/04/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/04/2016' '06/04/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/05/2016' '06/05/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/05/2016' '06/05/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/06/2016' '06/06/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/06/2016' '06/06/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/07/2016' '06/07/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/07/2016' '06/07/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/08/2016' '06/08/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/08/2016' '06/08/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/09/2016' '06/09/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/09/2016' '06/09/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/10/2016' '06/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/10/2016' '06/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/11/2016' '06/11/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/11/2016' '06/11/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/12/2016' '06/12/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/12/2016' '06/12/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/13/2016' '06/13/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/13/2016' '06/13/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/14/2016' '06/14/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/14/2016' '06/14/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/15/2016' '06/15/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/15/2016' '06/15/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/16/2016' '06/16/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/16/2016' '06/16/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/17/2016' '06/17/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/17/2016' '06/17/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/18/2016' '06/18/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/18/2016' '06/18/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/19/2016' '06/19/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/19/2016' '06/19/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/20/2016' '06/20/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/20/2016' '06/20/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/21/2016' '06/21/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/21/2016' '06/21/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/22/2016' '06/22/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/22/2016' '06/22/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/23/2016' '06/23/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/23/2016' '06/23/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/24/2016' '06/24/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/24/2016' '06/24/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/25/2016' '06/25/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/25/2016' '06/25/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/26/2016' '06/26/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/26/2016' '06/26/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/27/2016' '06/27/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/27/2016' '06/27/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/28/2016' '06/28/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/28/2016' '06/28/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/29/2016' '06/29/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/29/2016' '06/29/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '06/30/2016' '06/30/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '06/30/2016' '06/30/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Failed." 
fi
	
