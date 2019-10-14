#!/bin/sh

alias python=~/python27/bin/python

. ~/ab_ssrs_reporting_services/.envs/.odbc
. ~/ab_ssrs_reporting_services/.envs/.DEV.SQLServer


time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/iq_file_sql/delta_load.json --proc_params   \
CIGActgH.HydraPNLEntries "WHERE LastModifiedTime>'2019-06-19'"  Accounting.CIGActgH.HydraPNLEntries -ld 100


select * from CIGActgS11.BondAmDetail  lhs where lhs.StageID =189472

select * from CIGActgS11.BondAmDetail  rhs where rhs.StageID =189473


time python cli.py -nopp 3 -dcf config/db_config.DEV.json -pcf config/proc/data_sync/iq_file_sql/delta_load.json --proc_params   \
CIGActgS11.BondAmDetail "WHERE  StageID =189473" Accounting2018.CIGActgH.BondAmDetail -ld 100