

```
time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/iq_file_vert/delta_load.json --proc_params   \
Position.ME_FinancingPosition "WHERE AccountingDate='2019-08-31' and client=223906"  test -ld 100
```

