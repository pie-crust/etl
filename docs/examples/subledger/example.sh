#!/bin/sh

alias python=~/python27/bin/python


time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_s3_snow/journalline.json --proc_params  \
/auto/dbdumps_PMT_Snow/load_test_1/ |tee logs/load_test_1_2.log

echo "load_test_1" $?

time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_s3_snow/journalline.json --proc_params  \
/auto/dbdumps_PMT_Snow/load_test_3/ |tee logs/load_test_3_2.log

echo "load_test_3" $?

time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_s3_snow/journalline.json --proc_params  \
/auto/dbdumps_PMT_Snow/load_test_4/ |tee logs/load_test_4_2.log

echo "load_test_4" $?

time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_s3_snow/journalline.json --proc_params  \
/auto/dbdumps_PMT_Snow/load_test_5/ |tee logs/load_test_5_2.log

echo "load_test_5" $?


time python cli.py -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/dir_load/dir_s3_snow/journalline.json --proc_params  \
/auto/dbdumps_PMT_Snow/load_test/ |tee logs/load_test_0_2.log

echo "load_test_0" $?

