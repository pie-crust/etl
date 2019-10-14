
## Vertica access via cli

### vcli.sh
```
export PAGER='less -S'


. ./tools/vcli/odbc.sh
. ./tools/vcli/venv.sh


kinit s_dev_rdm -k -t ../s_dev_rdm.keytab


./tools/vcli/dist/vcli

```


## Pythonless cli
```

$ ./tools/vcli/dist/vcli
```

## Python cli
```
$ pwd
/home/s_dev_rdm/ab_gtx

$ ~/python27/bin/python2 ./tools/vcli/vcli.py

```


## Example

```

Vertica> select current_schema();
+----------------+
| current_schema |
+----------------+
| CIGRpt         |
+----------------+
1 row in set
Time: 0.017s
```

## Exit

```
Vertica> \q
Goodbye!
ld-dbn-bofin006:/home/s_dev_rdm/ab_gtx $
```