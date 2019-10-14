
Back to [README](../README.md)


# Pnl examples (IQ->StreamSlicer->S3->Snowflake)

 * Cli reads data row-by-row from IQ and hands it to S3 multipart uploader.
 * S3 uploader writes chunks of data into bucketed files in a loop.
 * Between IQ and S3 there is a StreamSlicer which cuts input stream into even 500k line parts.
 * It's done to create even ~50-100MB files for optimal Snowflake bulk load.
 * After S3 write is done Snowflake loaded issues one COPY INTO command for all uploaded files.

### Limit to 100 records from DY_DeskPLRSRange03.
```

alias python=~/python27/bin/python
python cli.py -nopp 18  -dcf config/db_config.DEV.json -pcf config/proc/pnl/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params \
223907 '09/10/2016' '09/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'

```

### Dump raw source data (with header) into csv file in ./dump/DY_DeskPLRSRange03/raw_dump.***.csv.
```

time python cli.py -nopp 18 -rte DEV --dump -dcf config/db_config.DEV.json \
-pcf config/proc/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params \
223907 05/31/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*"
```

### Load mock data from file 100_h.csv into Snowflake. (file must have header)
```

time python cli.py -nopp 18 -rte DEV -mf test/mock/DY_DeskPLRSRange03/100_h.csv\
-pcf config/proc/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params \
223907 05/31/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" 
```


### Transfer  full dataset from IQ to Snowflake for DY_DeskPLRSRange03 table.
```

time python cli.py -nopp 18 -rte DEV \
-pcf config/proc/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params \
223907 05/31/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" 
```


## PROD Example: 
```
python cli.py -nopp 18  -dcf config/db_config.PROD.json -pcf config/proc/pnl/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params \
223907 '09/10/2016' '09/10/2016'   'EOD' '*'  '*'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'

```

## Errors

* E_EMPTY_SOURCE_PIPE

```
  File "include/loader/S3StreamLoader.py", line 135, in load_stream
    raise Exception(clierr.E_EMPTY_SOURCE_PIPE[0])
Exception: Source pipe is empty
```

*Means no data returned from IQ procedure call.*






