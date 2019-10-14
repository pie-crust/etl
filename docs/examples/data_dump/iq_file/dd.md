
```

time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_dump/iq_file/simple_dump.json --proc_params   \
Position.ME_FinancingPosition "WHERE AccountingDate='2019-08-31' and client=223906"  test -ld 100


select top 3 *  from  Position.ME_FinancingPosition where AccountingDate='2019-08-31' and client=223906;
```