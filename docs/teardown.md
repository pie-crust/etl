
Back to [README](../README.md)


# Teardown workflow (DB->vs<-DB)

 * Cli reads data from both sources, loads it to local SQLite and emails report.

 
```
-> Extract data from Sybase IQ
	->Load data to SQLite
-> Extract data from SQLServer
	->Load data to SQLite
	
-> Extract join results from SQLite

```


### Example.

#### Multiple reports
```

time python cli.py -nopp 5 -rte PROD  -dcf config/db_config.PROD.json -pcf config/proc/teardown/db_vs_db/dmbalance.json --proc_params \
in/tear.py ./dump/33 ./dump/lite/ 
```



#### Single report (more data)
```

 time python cli.py -nopp 5 -rte PROD  -dcf config/db_config.PROD.json -pcf config/proc/teardown/db_vs_db/dmbalance.json --proc_params \
 in/teardown/iq_vs_sql.py ./dump/33 ./dump/lite/ 
```



### proc_params

 * pa[0] = SQL file 						[in/teardown/iq_vs_sql.py]
 * pa[1] = location of data dump 			[./dump/33]
 * pa[2] = location of sqlite db files 	[./dump/lite/]



