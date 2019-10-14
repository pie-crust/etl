from __future__ import print_function
"""
 time python cli2.py -nopp 2 --no-dump -no-mf test/mock/DY_FiccDistribution/15_h.csv -dcf config/db_config.json \
 -pcf config/proc/sql_snow/DY_FiccDistribution.json \
 --proc_params '2018-12-31 00:00:00' "$(date +"%Y-%m-%d %H:%M:%S")"
"""
assert app_init

try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init
from include.cli.sql_snow 			import sql_snow			as cli__
from include.extractor.SQLServer 	import SQLServer 		as extractor__
from include.loader.Snowflake 		import Snowflake		as loader__
from include.loader.S3StreamLoader 	import S3StreamLoader 	as s3_loader__
from include.Email 					import Email			as emailer__

from pprint import pprint as pp
from collections import OrderedDict
builtins.app_init=app_init
from include.Flow import SimpleFlow as Dag,  WaitFor, InOut, SyncMain



sql_cursor		= InOut()
s3_file_names	= InOut()

##
##
email_args={'email_subject':'SQLServer->Snowflake'}
##
##



dag=\
Dag([
	SyncMain({
		'0:SQL select'	: [extractor__.open_stream,	None, 			sql_cursor		],
		'2:upload to S3': [s3_loader__.load_stream,	sql_cursor, 	s3_file_names	],
		'3:copy into SF': [loader__.bulk_copy, 		s3_file_names, 	None			],
		'4:send email'	: [emailer__.send_email,	email_args,		None			]
		}),
	WaitFor(
		SyncMain(['4:send email'])
	)
])

#'1 test dump'	: [extractor.dump_stream,	pipe, 		None		], 

if __name__=='__main__':
	pass




