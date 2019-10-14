
Back to [README](../README.md)


# Workflow (IQ->file)

 * Cli dumps data from IQ into file.

 
```
1. Connect to Sybase IQ
    -> loop
        - fetchmany
        - append to dump file
```


### Example.
```
 time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/data_dump/iq_file/data_dump.json --proc_params   \
 CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'"  -ld 11
 ```


### proc_params

 * pa[0] = from table 	[CIGActgH.HydraPNLEntries]
 * pa[1] = from filter 	[WHERE LastModifiedTime>'2019-06-19']
 

### Dump file location defined in JSON config

```
"dump":{
	"dumpDir"		: ["/auto/dbdumps_PMT_Snow/delta_dumps", 0],
	"dumpFileFormat": ["{source*sourceDb}_{cli*tss}.csv", 2],
	
	"recordDelimiter"	: "\n",
	"columnDelimiter"	: ",",
	
	"writeHeader"		: 0,
		"headerFormat"		: "column",
```

### Lame duck load.

Use option `-ld 100` to load only first 100 rows from the source table











