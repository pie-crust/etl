(cli, conn_pool)=app_init
import os, sys, csv, time
import pyodbc
import collections
from collections import OrderedDict
from pprint import pprint as pp
e=sys.exit
import logging
log=logging.getLogger('cli')

import requests, json
import __builtin__ as builtins

from include.extractor.common.DataStreamer import DataStreamer

from include.utils import  ctimeit, api
from include.fmt import ppe
from include.extractor.common.Extractor import Extractor

class REST(Extractor):
	def __init__(self, **kwargs):
		Extractor.__init__(self)
		global actors
		self.cli =cli= kwargs.get('cli', None)
		assert cli
		self.cpool =cpool= kwargs.get('conn_pool', None)
		self.cln=cln= self.__class__.__name__
		

	@api
	@ctimeit
	def read_stream(self, pipe, skip_header, out):
		global actors
		cli=self.cli
		pipe=pipe.pipe
		skip=str(skip_header).strip()
		if skip_header is not None:
			skip=str(skip_header).strip()
		assert str(skip).strip() in ['0','1'], 'skip_header [%s] should be "0" or "1"' % str(skip).strip()
		if str(skip) == '1':
			pipe.readline()
		filter=cli.filter
		files=[]
		timeFormat = "%Y-%m-%d %H:%M:%S"
		currentTimeStamp = time.strftime(timeFormat)
		assert pipe
		start_time = time.time()
		trans_ids=[]
		
		line=pipe.readline()
		
		while line:
			
			trans_ids.append(str(line).strip().strip('^'))
			line=pipe.readline()
		#e()
		log.info('[%s] %s: Read:%d, From-Schema:%s, From-Table:%s, Skip:%s, Elapsed: %s' % (self.objtype, self.cln, len(trans_ids),cli.scfg['sourceSchema'], cli.scfg['sourceTable'],  skip, round((time.time() - start_time),2)))
		pipe.close()
		out.trans_ids=trans_ids
		return out #Out(trans_ids=trans_ids)
		

	@api
	@ctimeit
	def open_stream(self, source, trans_ids, skip_header, out):
		global actors
		cli=self.cli

		if 1: #//Legacy code
			gaToken=self.cli.pa[2]
			config=source
			log.info('Calling "{}"'.format(config['sourceUrl'])) 
			
			payload = "{ \"transactionIDs\": [" + ','.join(trans_ids.trans_ids) + "]}"
			headers = { "accept": "application/json", 'content-type': "application/json", "gaToken": gaToken }
			response = requests.request("POST", config['sourceUrl'], data=payload, headers=headers)

			log.info('Response received from FICC: {}'.format(response.status_code)) 

			assert response.status_code != 403, 'Request to Ficc API is forbidden, please check GA Token.'
			assert len(response.text) >0, 'No transaction Ids found, please verify the parameters passed.'

			responseJ = json.loads(response.text)
			distributions = responseJ["ficcnetDistributionRecords"]
			log.info('Received Total FiccNetDistribution Records: {}'.format(len(distributions))) 
			pipe=DataStreamer(self.cli,data=distributions)
			out.pipe ,out.actor = pipe, self.cln

			return out 


	@api
	@ctimeit
	def read_json_data(self, cfg, skip_header, out, read_stats):
		global actors, log
		cli=self.cli

		if 1: #//Legacy code
			gaToken=self.cli.pa[1]
			
			
			
			headers = { "accept": "application/json", 'content-type': "application/json", "gaToken": gaToken }
			
			url = stmt = cli.get_parsed(ckey='sourceUrl', cfg=cfg)
			log.info('URL = %s' % url)
			response = requests.request("GET", url,  headers=headers)
			if 1:
				response.raise_for_status()
			log.info('Response received from FICC: {}'.format(response.status_code)) 

			assert response.status_code != 403, 'Request to Ficc API is forbidden, please check GA Token.'
			assert len(response.text) >0, 'No transaction Ids found, please verify the parameters passed.'

			responseJ = json.loads(response.text)

			log.info('Received Total Records: {}'.format(len(responseJ))) 
			pipe=DataStreamer(self.cli,data=responseJ)
			out.pipe ,out.actor = pipe, self.cln
			read_stats.total_read=len(responseJ)

