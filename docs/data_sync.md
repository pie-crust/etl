
Back to [README](../README.md)


# Workflow (IQ->memory->SQLServer)

 * Cli reads data in chunks into memory using fetchmany from IQ and does conventional insert into SQLServer.

 
```
1. Connect to Sybase IQ
    -> loop
        - fetchmany
        - Conventional insert into SQL Server
    -> commit 
```


### Example.
```

 time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/sync/iq_mem_sql/delta_load.json --proc_params   \
 CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'"  Accounting.CIGActgH.HydraPNLEntries  -ld 100
```


### proc_params

 * pa[0] = from table 	[CIGActgH.HydraPNLEntries]
 * pa[1] = from filter 	[WHERE LastModifiedTime>'2019-06-19']
 * pa[2] = to table 	[ Accounting.CIGActgH.HydraPNLEntries]


 


### Lame duck load.

Use option `-ld 100` to load only first 100 rows from the source table


## Examples

 * From table name 
   * [Using file] (docs/examples/data_sync/iq_file_sql/example.sh)
   * [Using memory] (docs/examples/data_sync/iq_mem_sql/example.sh)
 * From query 
   * [Using file] (docs/examples/data_sync/iq_query_file_sql/example.sh)
   
   