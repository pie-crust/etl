# GTX

## Vertica
. ./tools/vcli/odbc.sh
. ./tools/vcli/venv.sh
kinit s_dev_rdm -k -t ../s_dev_rdm.keytab




```
export G3_TEMP_DIR=/tmp/gfin
time python3 cli.py  -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/dir_gtx_vertica/gtx.json --proc_params  ./legacy/gtx
```


> Params:
>    --workingDir 














 




