#!/bin/sh

alias python=~/python27/bin/python




python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/01/2016' '10/01/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/01/2016' '10/01/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:01: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/02/2016' '10/02/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/02/2016' '10/02/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:02: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/03/2016' '10/03/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/03/2016' '10/03/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:03: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/04/2016' '10/04/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/04/2016' '10/04/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:04: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/05/2016' '10/05/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/05/2016' '10/05/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:05: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/06/2016' '10/06/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/06/2016' '10/06/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:06: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/07/2016' '10/07/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/07/2016' '10/07/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:07: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/08/2016' '10/08/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/08/2016' '10/08/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:08: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/09/2016' '10/09/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/09/2016' '10/09/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:09: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/10/2016' '10/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/10/2016' '10/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:10: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/11/2016' '10/11/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/11/2016' '10/11/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:11: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/12/2016' '10/12/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/12/2016' '10/12/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:12: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/13/2016' '10/13/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/13/2016' '10/13/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:13: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/14/2016' '10/14/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/14/2016' '10/14/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:14: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/15/2016' '10/15/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/15/2016' '10/15/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:15: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/16/2016' '10/16/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/16/2016' '10/16/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:16: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/17/2016' '10/17/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/17/2016' '10/17/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:17: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/18/2016' '10/18/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/18/2016' '10/18/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:18: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/19/2016' '10/19/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/19/2016' '10/19/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:19: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/20/2016' '10/20/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/20/2016' '10/20/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:20: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/21/2016' '10/21/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/21/2016' '10/21/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:21: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/22/2016' '10/22/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/22/2016' '10/22/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:22: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/23/2016' '10/23/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/23/2016' '10/23/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:23: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/24/2016' '10/24/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/24/2016' '10/24/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:24: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/25/2016' '10/25/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/25/2016' '10/25/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:25: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/26/2016' '10/26/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/26/2016' '10/26/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:26: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/27/2016' '10/27/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/27/2016' '10/27/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:27: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/28/2016' '10/28/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/28/2016' '10/28/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:28: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/29/2016' '10/29/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/29/2016' '10/29/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:29: DY_DeskPLRSRange03:223906: Failed." 
fi
	

python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/30/2016' '10/30/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/30/2016' '10/30/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Failed." 
fi


python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223907 '10/31/2016' '10/31/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03: Failed." 
fi

alias python=~/python27/bin/python
python cli.py -nopp 18 -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params 223906 '10/31/2016' '10/31/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'
if [ $? -eq 0 ]  
then
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Successful."
else
  echo "LOAD_STATUS:30: DY_DeskPLRSRange03:223906: Failed." 
fi

