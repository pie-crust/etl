Richard:

```
Use 9-18-19 for DY tables 
Use 8-31-19 for ME tables

### DY_FinancingPosition 9-24-19

select Client, count(*) from Position.DY_FinancingPosition where AccountingDate='2019/9/24' group by Client ;

time python tools/loader/position/iq_proc_dir_iq.py -t DY_FinancingPosition -yr 2019 -mf 9 -mt 9  -df 24 -dt 24  -cl 223906 --dry


### ME_FinancingPosition 8-31-19

time python tools/loader/position/iq_proc_dir_iq.py -t ME_FinancingPosition -yr 2019 -mf 8 -mt 8  -cl 223906 --dry




### DY_Position_SD (ACCT only) 9-18-19

time python tools/loader/position/iq_proc_dir_iq.py -t DY_Position_SD -yr 2019 -mf 9 -mt 9 -cl 223906 -df 18 -dt 18 -cr ACCT   -ld 37 --dry

ME_Position_SD (ACCT and DESK)



ME_Position_TD (ACCT and DESK)
DY_Position_TD (ACCT and DESK)

# ME_FiccDistribution 8-31-19

time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/iq_rest_iq/ME_FiccDistribution.json  --proc_params  \
Repo '2019/08/31' e5569eb7-e333-4e28-ad77-0f224a7d2499@1



# DY_FiccDistribution 9-18-19

time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/iq_rest_iq/DY_FiccDistribution.json  --proc_params  \
Repo '2019/09/18' e5569eb7-e333-4e28-ad77-0f224a7d2499@1
time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/iq_rest_iq/DY_FiccDistribution.json  --proc_params  \
Repo '2019/09/24' e5569eb7-e333-4e28-ad77-0f224a7d2499@1







ME_13F
```


