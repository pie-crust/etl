ll=['Host: [ld-dbn-bofin006], User: [s_dev_racct]',
 'Home: [/home/s_dev_racct/ab_ssrs_reporting_services]',
 'Db conf: config/db_config.json',
 'Proc conf: config/proc/iq_stream_s3_snow/ME_Position_SD.json',
 "Procedure: CIGActgH.spSettleDatePosition_WRAPPER '223907','05/31/2019','EOD','DESK','*','*','*','*','*','*','*','*','*','*','*','*','*','*'",
 'Env: [DEV]',
 'IQ: Using mock file: test/mock/ME_Position_SD/100_h.csv',
 'First row elapsed: 0.2 sec/0.0 min',
 's3://home-pmt-accounting-dev/racct/ME_Position_SD/file_0.IQ.Xs8Kdx.20190625_143635.csv.gz',
 'S3: Loaded:100, Read:100, Files:1, Elapsed: 0 sec/0 min',
 'S3: Total:24.42 KB, Compressed (gz):3.1 KB',
 'Records deleted: 100, Elapsed: 0.79 sec/0.01 min',
 'Snowflake: Inserted:100, Schema:ACCOUNTINGBI.POSITION, Table:ME_Position_SD Elapsed:1.35 sec/0.02 min',
 'Log: /tmp/tmp_AezzG/cli/20190625_143632/cli_46140.log',
 'Total elapsed: 8.57 sec/0.14 min']

import os, re
stats={}
group='first_row'
m = re.search('First row elapsed: (?P<first_row>[0-9., ]+sec/[0-9., ]+min)', os.sep.join(ll))
stats[group]= m.group(group)

group='s3_loaded'
m = re.search('S3: Loaded:(?P<s3_loaded>[0-9]+)', os.sep.join(ll))
stats[group]= m.group(group)

group='s3_read'
m = re.search('S3: Loaded:[0-9]+, Read:(?P<s3_read>[0-9]+)', os.sep.join(ll))
stats[group]= m.group(group)

group='s3_raw'
m = re.search('S3: Total:(?P<s3_raw>[0-9., A-Z]+),', os.sep.join(ll))
stats[group]= m.group(group)

group='snow_del'
m = re.search('Records deleted: (?P<snow_del>[0-9]+)', os.sep.join(ll))
stats[group]= m.group(group)

group='snow_ins'
m = re.search('Snowflake: Inserted:(?P<snow_ins>[0-9]+)', os.sep.join(ll))
stats[group]= m.group(group)

group='s3_files'
m = re.search(', Files:(?P<s3_files>[0-9]+)', os.sep.join(ll))
stats[group]= m.group(group)

group='s3_compressed'
m = re.search('Compressed \(gz\)\:(?P<s3_compressed>[0-9., A-Z]+)', os.sep.join(ll))
stats[group]= m.group(group)

group='total_elapsed'
m = re.search('Total elapsed: (?P<total_elapsed>[0-9., ]+sec/[0-9., ]+min)', os.sep.join(ll))
stats[group]= m.group(group)


group='env'
m = re.search('Env: \[(?P<env>[A-Z]+)\]', os.sep.join(ll))
stats[group]= m.group(group)

group='table'
m = re.search(', Table:(?P<table>[a-zA-Z_]+)', os.sep.join(ll))
stats[group]= m.group(group)
group='schema'
m = re.search(', Schema:(?P<schema>[a-zA-Z_\.]+)', os.sep.join(ll))
stats[group]= m.group(group)



