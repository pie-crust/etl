#!/bin/sh

alias python=~/python27/bin/python

. ../ab_ssrs_reporting_services/.envs/.odbc
. ../ab_ssrs_reporting_services/.envs/.DEV.Snowflake


time python cli.py -nopp 2 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_sqlite/teardown.json --proc_params  \
./dump/10/ tablename



aws s3 ls s3://home-pmt-accounting-dev/racct/auto/dbdumps_PMT_Snow/load_test_2/|wc -load_test_2/




time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/file_load/dir_s3_snow/journalline.json --proc_params  \
/auto/dbdumps_PMT_Snow/small_test/

aws s3 ls s3://home-pmt-accounting-dev/racct/auto/dbdumps_PMT_Snow/load_test_2/|wc -load_test_2/


aws s3 ls s3://home-pmt-accounting-dev/racct/auto/dbdumps_PMT_Snow/load_test/

aws s3 rm s3://home-pmt-accounting-dev/racct/auto/dbdumps_PMT_Snow/load_test_2/ --recursive




 




