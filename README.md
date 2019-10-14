# RC

### RC_Balance_Cash
```
 time python cli.py -nopp 2  -dcf config/db_config.DEV.json -pcf config/proc/RC/rest_iq/RC_Balance_Cash.json  --proc_params  \
 '2019/07/31' e***1
```

### RC_Balance_Cash (auto detect month)
```
 time python cli.py -nopp 2  -dcf config/db_config.DEV.json -pcf config/proc/RC/rest_iq/RC_Balance_Cash.json  --proc_params  \
 'auto' e***1
```


# IQ -> Vertica

### ME_FinancingPosition
```
time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/iq_file_vert/delta_load.json --proc_params   \
Position.ME_FinancingPosition "WHERE AccountingDate='2019-08-31' and client=223906"  test -ld 100
```


# Vertica->IQ

### ME_FinancingPosition
```
time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/vert_file_iq/delta_load.json --proc_params   \
Position.ME_FinancingPosition "WHERE AccountingDate='2019-08-31' and client=223906"  test -ld 100
```




# FICC IQ->IQ

### DY_FiccDistribution
```
time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/iq_rest_iq/DY_FiccDistribution.json  --proc_params  \
Repo '2019-08-30' e5***@1
```

### ME_FiccDistribution
```
time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/iq_rest_iq/ME_FiccDistribution.json \
 --proc_params  Repo '2019-08-31' e5***@1
```



# GFIN

```
export G3_TEMP_DIR=/tmp/gfin
time ~/python3/bin/python3 cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/dir_gfin_vertica/gfin.json --proc_params  \
./legacy/gfin  
```

> Params:
>    --workingDir


# GRDS
```
 time ~/python3/bin/python3 cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/dir_grds_vertica/grds.json --proc_params  ./legacy/grds
```


> Params:
>   --workingDir 


# GTX
```
time python3 cli.py  -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/dir_gtx_vertica/gtx.json --proc_params  ./legacy/gtx
```


> Params:
>   --workingDir 
	
	
# FICC


### DY_FiccDistribution
```
 time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/iq_rest_iq/DY_FiccDistribution.json \
 --proc_params  Repo '2019-05-31' e5569eb7-e333-4e28-ad77-0f224a7d2499@1
```

### ME_FiccDistribution
```
 time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/iq_rest_iq/ME_FiccDistribution.json \
 --proc_params  Repo '2019-05-31' e5569eb7-e333-4e28-ad77-0f224a7d2499@1
```



# IQ proc -> Vertica

## Direct

### DY_Position_TD

```
time ~/python3/bin/python3 cli.py -nopp 27 -dcf config/db_config.DEV.json  -rte DEV -pcf config/proc/position/iq_proc_dir_v/DY_Position_TD.json   --proc_params \
223906 "EOD" 2019/8/1 "DESK" "CEFL" "DEFAULT" "REGULAR" "1" "0" "NONE" "*" "*" "N" "0" "0" "NONE" "NONE" "ALL" "0" "MONTH_END" "N" "ALL" "*" "0" "*" "N" "*"
```

## Using automation

223906
```
time python tools/loader/position/iq_proc_dir_v.py -t DY_Position_TD -yr 2019 -mf 8 -mt 8 -df 1 -dt eom  -cl 223906  -cr ACCT  --dry
```
 
223907 (all of aug 2019)
```
time python tools/loader/position/iq_proc_dir_v.py -t DY_Position_TD -yr 2019 -mf 8 -mt 8 -df 1 -dt eom  -cl 223907  -cr ACCT  --dry
```
223907 ( aug 22 2019)
```
time python tools/loader/position/iq_proc_dir_v.py -t DY_Position_TD -yr 2019 -mf 8 -mt 8 -df 22 -dt 22  -cl 223907  -cr ACCT  --dry
```


# IQ proc -> IQ 

## Direct

### DY_Position_TD

```
time ~/python3/bin/python3 cli.py -nopp 27 --dump -dcf config/db_config.PROD.json  -rte PROD -pcf config/proc/position/iq_proc_dir_iq/DY_Position_TD.json -ld 37  --proc_params \
223906 "EOD" 2019/1/1 "DESK" "CEFL" "DEFAULT" "REGULAR" "1" "0" "NONE" "*" "*" "N" "0" "0" "NONE" "NONE" "ALL" "0" "MONTH_END" "N" "ALL" "*" "0" "*" "N" "*"
```
### ME_Position_TD
```
time ~/python3/bin/python3 cli.py -nopp 27 --dump -dcf config/db_config.PROD.json  -rte PROD  -pcf config/proc/position/iq_proc_dir_iq/ME_Position_TD.json -ld 30  --proc_params 223906 "EOD" 2019/1/31 "DESK" "CEFL" "DEFAULT" "REGULAR" "1" "0" "NONE" "*" "*" "N" "0" "0" "NONE" "NONE" "ALL" "0" "FULL"      "N" "ALL" "*" "0" "*" "Y" "*"

```

## Using automation

### DY_Position_TD
```
time python tools/loader/position/iq_proc_dir_iq.py -t DY_Position_TD -yr 2019 -mf 1 -mt 1 -cl 223906 -df 1 -dt eom -cr DESK  -bu CEFL -ld 37
```
### ME_Position_TD
```
time python tools/loader/position/iq_proc_dir_iq.py -t ME_Position_TD -yr 2019 -mf 1 -mt 1 -cl 223906  -cr DESK -bu CEFL  -ld 30 
```



## GFIN snap ->SQLite

```
 ~/python27/bin/python2 cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/file_gfin_lite/gfin.json --proc_params  ./gfin
```


Open SQLite cli:
```
python ~/litecli/main.py dump/lite/20190829_160315/SQLite.db
```

describe table: ```PRAGMA table_info([Barrier])```
Count: ```Select count(*) from Barrier```


## IQ->IQ (position)



* [Test all](test/position/t.iq_proc_dir_iq.py)



## Report over Outlook emails
* [Max Elapsed](docs/sql_over_outlook.md)





## [Data Sync](docs/examples/data_sync.md)
 * From table name 
   * [Using file](docs/data_sync/db_file_db/iq_file_sql.sh)
   * [Using memory](docs/examples/data_sync/iq_mem_sql/example.sh)
   * [Parallel](docs/examples/data_sync/db_file_db_mp_async/iq_file_sql_mp_async.sh)
 * From query 
   * [Using file](docs/examples/data_sync/iq_query_file_sql/example.sh)

  
## [Data Dump](docs/examples/data_dump.md)
 * [From table name](docs/examples/data_dump/iq_file/data_dump.sh)
 * [From query](docs/examples/data_dump/iq_query_file/data_dump.sh)
 
 
## Docs
 * [IQ->StreamSlicer->S3->Snowflake](docs/position.md) 
 * [SQL->StreamSlicer->S3->Snowflake](docs/position.md) 
 * [Snowflake->REST->Snowflake](docs/ficc.md) 
 * [IQ->memory->SQLServer](docs/data_sync.md) 
 * [Dir->S3->Snowflake](docs/dir_load.md)
 * [IQ->File](docs/data_dump.md)
 * [SQL->File](docs/data_dump.md)
 * [Teardown](docs/teardown.md)


	
## Examples
 * Position
   * [IQ->SF](docs/examples/position/iq_stream_s3_snow) 
   * [SQL->SF](docs/examples/position/sql_stream_s3_snow)
 * PNL
    * [IQ->SF](docs/examples/pnl) 
 * Ficc
    * [SF->REST->SF](docs/examples/ficc/example.sh)
 * File load (Subledger)
    * [File->SF](docs/examples/subledger/example.sh)
 * Data Sync (HydraPNLEntries)
    * [IQ->SQL](docs/examples/subledger/example.sh)
 * Data Dump (HydraPNLEntries)
    * [IQ->File](docs/examples/data_dump/iq_file/data_dump.sh) 
    * [SQL->File](docs/examples/data_dump/sql_file/data_dump.sh)
 * Teardown
    * [IQ vs SQLServer (dmbalance)](docs/examples/teardown/db-vs-db/dmbalance.sh)



## Workflows
 * Stream
    * [IQ->StreamSlicer->S3->Snowflake](docs/position.md)
 * From File
    * [Dir->S3->Snowflake](docs/dir_load.md)
 * Memory
    * [IQ->memory->SQLServer](docs/data_sync.md)
 * REST
    * [Snowflake->REST->Snowflake](docs/ficc.md)
 * From IQ
    * [IQ->memory->SQLServer](docs/data_sync.md) 
    * [IQ->StreamSlicer->S3->Snowflake](docs/position.md)
 * From Snowflake
    * [Snowflake->REST->Snowflake](docs/ficc.md)
 * Into Snowflake
    * [Snowflake->REST->Snowflake](docs/ficc.md)
    * [IQ->StreamSlicer->S3->Snowflake](docs/position.md)
    * [Dir->S3->Snowflake](docs/dir_load.md)
 * S3
    * [IQ->StreamSlicer->S3->Snowflake](docs/position.md)
    * [Dir->S3->Snowflake](docs/dir_load.md)
 * From SQLServer
    * [SQL->StreamSlicer->S3->Snowflake](docs/position.md) 
 * Into SQLServer
    * [IQ->memory->SQLServer](docs/data_sync.md) 
 * Into File
    * [Data dump](docs/data_dump.md)
 * Compare 2 sides 
    * [DB->vs<-DB](docs/teardown.md)








