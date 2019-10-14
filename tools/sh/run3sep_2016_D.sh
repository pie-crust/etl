#!/bin/sh

alias python=~/python27/bin/python




python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/01/2016' '09/01/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/01/2016' '09/01/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/02/2016' '09/02/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/02/2016' '09/02/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/03/2016' '09/03/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/03/2016' '09/03/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/04/2016' '09/04/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/04/2016' '09/04/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/05/2016' '09/05/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/05/2016' '09/05/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/06/2016' '09/06/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/06/2016' '09/06/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/07/2016' '09/07/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/07/2016' '09/07/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/08/2016' '09/08/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/08/2016' '09/08/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/09/2016' '09/09/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/09/2016' '09/09/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/10/2016' '09/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/10/2016' '09/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/11/2016' '09/11/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/11/2016' '09/11/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/12/2016' '09/12/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/12/2016' '09/12/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/13/2016' '09/13/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/13/2016' '09/13/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/14/2016' '09/14/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/14/2016' '09/14/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/15/2016' '09/15/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/15/2016' '09/15/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/16/2016' '09/16/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/16/2016' '09/16/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/17/2016' '09/17/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/17/2016' '09/17/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/18/2016' '09/18/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/18/2016' '09/18/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/19/2016' '09/19/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/19/2016' '09/19/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/20/2016' '09/20/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/20/2016' '09/20/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/21/2016' '09/21/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/21/2016' '09/21/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/22/2016' '09/22/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/22/2016' '09/22/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/23/2016' '09/23/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/23/2016' '09/23/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/24/2016' '09/24/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/24/2016' '09/24/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/25/2016' '09/25/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/25/2016' '09/25/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/26/2016' '09/26/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/26/2016' '09/26/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/27/2016' '09/27/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/27/2016' '09/27/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/28/2016' '09/28/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/28/2016' '09/28/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/29/2016' '09/29/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/29/2016' '09/29/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '09/30/2016' '09/30/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '09/30/2016' '09/30/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Failed." 
fi
	
