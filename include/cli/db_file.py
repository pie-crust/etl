"""
 time python cli.py -nopp 4 --dump  -dcf config/db_config.json -pcf config/proc/snow_url_sql/DY_FinancingPosition.json \
 --proc_params  Repo '2018-12-31 00:00:00' "$(date +"%Y-%m-%d %H:%M:%S")" e5569eb7-e333-4e28-ad77-0f224a7d2499@1
#
# pa[0] = ReferenceType
# pa[1] = AccountingDate
# pa[2] = AsOfDateTime
# pa[3] = gatoken
#


"""
(cli, conn_pool)=app_init
import os, sys, re, time
import json, logging
from datetime import datetime
import tempfile, traceback
from pprint import pprint as pp
from include.fmt import get_formatted
from include.cli.common.db_file import db_file
e=sys.exit

from include.utils import ctimeit, clierr
try:
	import cStringIO
except ImportError:
	import io as cStringIO
	
log=logging.getLogger('cli')
		
class db_file(db_file):
	@ctimeit
	def __init__(self,*args, **kwargs):
		db_file.__init__(self, *args, **kwargs)


