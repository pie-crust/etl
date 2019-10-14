from __future__ import print_function
assert app_init
"""
 time python cli2.py -nopp 2 --no-dump  -dcf config/db_config.json \
 -pcf config/proc/snow_url_sql/DY_Position_SD.json \
 --proc_params '2018-12-31 00:00:00' "$(date +"%Y-%m-%d %H:%M:%S")"
 
 
  time python cli2.py -nopp 4  -dcf config/db_config.json -pcf config/proc/snow_url_sql/DY_FinancingPosition.json \
 --proc_params  Repo '2018-12-31 00:00:00' "$(date +"%Y-%m-%d %H:%M:%S")" e5569eb7-e333-4e28-ad77-0f224a7d2499@1
#
# pa[0] = ReferenceType
# pa[1] = AccountingDate
# pa[2] = AsOfDateTime
# pa[3] = gatoken
#



"""
try:
	import __builtin__ as builtins
except:
	import builtins
builtins.app_init=app_init

from include.cli.snow_url_sql 		import snow_url_sql		as cli__
from include.extractor.Snowflake	import Snowflake 		as extractor__
from include.loader.SQLServer 		import SQLServer		as sql_loader__
from include.extractor.Url 			import Url 				as url_extractor__
from include.Email 					import Email			as emailer__

from pprint import pprint as pp
from collections import OrderedDict
builtins.app_init=app_init
from include.Flow import ListFlow as Dag,  WaitFor, InOut, SyncMain as Main, Async


Snow_cursor	= InOut()
url_pipe	= InOut()
trans_ids	= InOut()

##
##
email_args={'email_subject':'RefCode->SQLServer'}
##
##

#import include.clisten
import include.csend as senders


def run():
    print('Using "kwargs" messaging protocol of pubsub v3')

    senders.doSomething1()
    senders.doSomething2()
	
if 0:
	Dag([
		Main([
			[[extractor__		.open_stream,		None, 			Snow_cursor	], 'IDs fetch'		],
			[[url_extractor__	.read_stream,		Snow_cursor, 	trans_ids	], 'Read IDs'		],
			[[sql_loader__		.begin_transaction,	None, 			None		], 'Target trans'	],
			[[url_extractor__	.open_stream, 		trans_ids, 		url_pipe	], 'Read data'		],
			[[sql_loader__		.purge_data, 		None, 			None		], 'purge old '		],
			[[sql_loader__		.insert_data, 		url_pipe, 		None		], 'Insert new '	],
			[[sql_loader__		.end_transaction, 	None, 			None		], 'Commit target'	],
			Async([[emailer__	.send_email,		email_args,		None		], 'send email'		])
			]),
		WaitFor(
			Main(['send email'])
		)
	])



if __name__=='__main__':
	pass




