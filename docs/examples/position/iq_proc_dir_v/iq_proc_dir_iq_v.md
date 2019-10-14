```
alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake
```

### DY_Position_TD
```
time ~/python3/bin/python3 cli.py -nopp 27 --dump -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir_v/DY_Position_TD.json   --proc_params \
223906 "EOD" 2019/8/1 "ACCT" "*" "DEFAULT" "REGULAR" "1" "0" "NONE" "*" "*" "N" "0" "0" "NONE" "NONE" "ALL" "0" "MONTH_END" "N" "ALL" "*" "0" "*" "N" "*" \
-ld 11
```


### DY_Position_SD
```
time ~/python3/bin/python3 cli.py -nopp 18 -dcf config/db_config.DEV.json -pcf config/proc/position/iq_proc_dir_v/DY_Position_SD.json --proc_params \
223906 2019/8/1 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" \
-ld 15
```


##  Automation
 time python tools/loader/position/iq_proc_dir_v.py -t DY_Position_SD -yr 2019 -mf 8 -mt 8 -df 22 -dt 22  -cl 223906  -cr DESK -ld 10 --dry

 