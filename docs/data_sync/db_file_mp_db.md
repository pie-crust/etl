
Back to [README](../README.md)


# Workflow (Db->File->Multiprocessing->Db)

 * Cli reads data in chunks into memory using fetchmany from IQ and does conventional insert into SQLServer.

 
```
1. Connect to Sybase IQ
    -> Loop
        - fetchmany
        - save to file
    -> Multiprocessing
        - conventional load files to SQL Server in parallel
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
