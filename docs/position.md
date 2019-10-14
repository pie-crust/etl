
Back to [README](../README.md)


# Position examples (IQ->StreamSlicer->S3->Snowflake)

 * Cli reads data row-by-row from IQ and hands it to S3 multipart uploader.
 * S3 uploader writes chunks of data into bucketed files in a loop.
 * Between IQ and S3 there is a StreamSlicer which cuts input stream into even 500k line parts.
 * It's done to create even ~50-100MB files for optimal Snowflake bulk load.
 * After S3 write is done Snowflake loaded issues one COPY INTO command for all uploaded files.

### Limit to 100 records from ME_Position_SD.
```

time python cli.py -nopp 18 -rte DEV  -dcf config/db_config.DEV.json \
-pcf config/proc/iq_stream_s3_snow/ME_Position_SD.json --proc_params \
223907 05/31/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 100
```

### Dump raw source data (with header) into csv file in ./dump/ME_Position_SD/raw_dump.***.csv.
```

time python cli.py -nopp 18 -rte DEV --dump -dcf config/db_config.DEV.json \
-pcf config/proc/iq_stream_s3_snow/ME_Position_SD.json --proc_params \
223907 05/31/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*"
```

### Load mock data from file 100_h.csv into Snowflake. (file must have header)
```

time python cli.py -nopp 18 -rte DEV -mf test/mock/ME_Position_SD/100_h.csv\
-pcf config/proc/iq_stream_s3_snow/ME_Position_SD.json --proc_params \
223907 05/31/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" 
```


### Transfer  full dataset from IQ to Snowflake for ME_Position_SD table.
```

time python cli.py -nopp 18 -rte DEV \
-pcf config/proc/iq_stream_s3_snow/ME_Position_SD.json --proc_params \
223907 05/31/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" 
```


## PROD Example: 
```
time python cli.py -nopp 18 -rte PROD -dcf config/db_config.PROD.json \
-pcf config/proc/iq_stream_s3_snow/ME_Position_SD.json --proc_params \
223907 05/31/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" 
```

## Errors

* E_EMPTY_SOURCE_PIPE

```
  File "include/loader/S3StreamLoader.py", line 135, in load_stream
    raise Exception(clierr.E_EMPTY_SOURCE_PIPE[0])
Exception: Source pipe is empty
```

*Means no data returned from IQ procedure call.*






