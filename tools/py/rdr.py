
import os
import re
import ast
import json
import sys
import csv
import time
import logging
import platform
import pyodbc
import getpass
import traceback
import _util as util
#from util import util.updateEmailContent, logSetup
from argparse import ArgumentParser, SUPPRESS
import _loader

e=sys.exit

timeFormat = "%Y-%m-%d %H:%M:%S"
csv.register_dialect('IqVerticaDialect', doublequote=False, escapechar='\\')
reload(sys)
sys.setdefaultencoding('utf8')

STARTED_ON = "Started On"
SOURCE = "Source"
TARGET = "Target"
ADDITIONAL_ARGUMENTS = "Additional arguments"
ENDED_ON = "Ended On"
JOB_FAILED = 'Job Failed'
LOGS_PATH = "Logs Path"
PARAMETERS_PROVIDED = "Parameters provided"
RECORDS_ADDED = "Records Added"
REQUEST_FROM = "Request From"


EMAIL_SORTING = [ REQUEST_FROM, PARAMETERS_PROVIDED, ADDITIONAL_ARGUMENTS, SOURCE, TARGET, STARTED_ON, ENDED_ON, RECORDS_ADDED, LOGS_PATH, JOB_FAILED ]
SENDER = os.environ['GAUSER']  if os.environ['GAUSER'] is not None else ''
RECEIVER=os.environ['SSRSSUPPORTEMAILS'] if os.environ['SSRSSUPPORTEMAILS'] is not None else ''


DB_READER_DATA_DIR = '{}racct/DataMigration/DbReaderData'.format(os.environ['LOGLOC'])

LOG_DIR = '{}racct/DataMigration/DbReader'.format(os.environ['LOGLOC'])
LOG_FILE = 'dbReaderWriter_{}.log'.format(platform.uname()[1])
DB_READ_SERVER =  os.environ['IQREADERSERVER'] if os.environ['IQREADERSERVER'] is not None else ''
DB_READ_USER = os.environ['IQDBUSER'] if os.environ['IQDBUSER'] is not None else ''
DB_READ_PWD = os.environ['IQDBPASSWORD'] if os.environ['IQDBPASSWORD'] is not None else ''
VERTICA_SUCCESS_STATUS_DIR = os.environ['VERTICA_SUCCESS_LINUX_DIR']
TD_POSITION_DIR='TDPosition'
FIN_POSITION_DIR='FinancingPosition'
SD_POSITION_DIR='SDPosition'

def writeRowsToFiles(directory, field_names, procConfig, rows):
	rowCount = 0
	fileNames = []
	fileCount = 0
	file = None
	csv_out = None
	maxRecords = int(procConfig['maxRecordsInFile'])
	if maxRecords <= 0:
		maxRecords = 1000000

	for ind in range(len(rows)):
		if rowCount % maxRecords == 0:
			fileCount += 1
			file = util.getTempFile(procConfig['key'], fileCount, 'csv', directory)
			csv_out = csv.writer(file, 'IqVerticaDialect')
			logging.info("Writing data to file: {}".format(file.name))
			fileNames.append(file.name)
			csv_out.writerow(field_names)
		try:
			csv_out.writerow(rows[ind])
		except Exception as ex:
		
			logging.error("Exception occurred in row index: {}".format(ind))
			logging.error(rows[ind])
			raise
		rowCount += 1

	return fileNames

def downloadDataToFile(procConfig, params):
	if os.path.exists(DB_READER_DATA_DIR) == False :
		os.mkdir(DB_READER_DATA_DIR)

	try:
		pyodbc.pooling = False
		
		connString = procConfig['sourceDbConnectionString']
		pp(connString)
		if DB_READ_SERVER and DB_READ_USER and DB_READ_PWD:
			connString = connString.format(DB_READ_SERVER,DB_READ_USER,DB_READ_PWD)
		else:
			message="DB_READ_SERVER {} or DB_READ_USER {} or DB_READ_PWD {} not defined".format(DB_READ_SERVER,DB_READ_USER,DB_READ_PWD)
			logging.error(message)
			raise Exception(message)
		logging.debug('Making connection using : {}'.format(connString))
		pp(connString)
		
		conn = pyodbc.connect(connString)
		logging.debug('Successfule connection!!!')
		print 333
		e()
		cur = conn.cursor()
		proc =  procConfig['procName']

		paramlist = str(params).strip('[]')
		print(paramlist)
		stmt = 'SET TEMPORARY OPTION DATE_ORDER=MDY exec {} {}'.format(proc, paramlist) if DB_READ_SERVER.find('IQ') != -1 else 'exec {} {}'.format(proc, paramlist)
		#e()
		if 0:
			stmt = """SET TEMPORARY OPTION DATE_ORDER=MDY  exec CIGActgH.spFIRPTAReport_WRAPPER	
 @pClientID=223906 
, @pStartDate='01/01/2018'
, @pEndDate='01/01/2018'
, @pEndStage='EOD'
, @pFund='*'
, @pAccount='*'
, @pPosType='ACCT'
, @pDesk='*'
, @pPosBlock='*'
, @pInstrument='*'"""
		
		logging.info("Executing Statement: {}".format(stmt))
		print('-'*80)
		pp(stmt)
		#e()
		cur.execute(stmt)
		logging.info("Execution completed for statement, fetching rows..")
 
		field_names = [val[0] for val in cur.description]
		rows = cur.fetchall()
		logging.info('{} rows returned by executing proc: {}'.format(len(rows), proc))
		
		cur.close()
		conn.close()
		pp(dir(rows))
		print(len(rows))
		#e()
		fileNames = writeRowsToFiles(DB_READER_DATA_DIR, field_names, procConfig, rows)
		logging.info("Finished writing data to following files: {}".format('\n '.join(fileNames)))
		return fileNames 
	except pyodbc.Error as pex:
		raise
		#message = 'Error occurred while downloading data - {}'.format(', '.join(pex))
		#raise Exception(message)
	except Exception as err:
		#logging.error("Unexpected error: {}".format(sys.exc_info()[0]))
		raise

def getParamsToBeUsedInInsert(colMappings, params):
	selParams = {}
	try:
		for map in colMappings:
			#pp(map)
			#e(0)
			if map['value'] == 'Param':
				paramValue = params[map['sourceParamIndex']]
				selParams[map['sourceParam']] = re.sub('[\'" ]', '', paramValue)
	except Exception as ex:
		raise
		#raise Exception('Exception occured by mapping params with Insert statement: ' + ex.message)
	return selParams

def executeJobForConfig(config_file,config_key,procparams,sourceDb, targetDb, targetTable):
	procConfig = util.loadConfigForKey(config_key,config_file, sourceDb, targetDb, targetTable)
	#pp(procConfig['columnMappings'])
	#print(123)
	#e(0)
	util.updateEmailContent(SOURCE, '{} - {}'.format(procConfig['sourceDb'], procConfig['procName']))
	util.updateEmailContent(TARGET, '{} - {}'.format(procConfig['targetDb'], procConfig['targetTable']))
	logging.info('Config to execute: {} with SourceDbConnString: "{}", TargetDbConnString: "{}"'.format(
		procConfig['key'], procConfig['sourceDbConnectionString'], procConfig['targetDbConnectionString']))
	#pp(procparams)
	#e()
	paramsForInsertStmt = getParamsToBeUsedInInsert(procConfig['columnMappings'],procparams)
	pp(paramsForInsertStmt)
	#e(0)
	logging.info('paramsForInsertStmt:: {}'.format(paramsForInsertStmt))
	logging.info('config_file:: {} config_key:: {} procparams:: {}'.format(config_file,config_key,procparams))
	if 1:
		fileNames = downloadDataToFile(procConfig, procparams)
		pprint(fileNames)
		e()
	else:
		fileNames=['/logdev/racct/DataMigration/DbReaderData/Daily_FinancingPosition_2019-05-16_08-54-29-1.csv']
	currentTimeStamp = time.strftime(timeFormat)
	for fileName in fileNames:
		pp(fileName)
		#e()
		_loader.sys.argv = ['-configkey', config_key,'-configFile',config_file,'-f', fileName, '-t', currentTimeStamp, '-p', paramsForInsertStmt]
		if 1:
			_loader.main(targetDb, targetTable)
		else:
			logging.info('bypass loader.main:: targetDb={} targetDb={} '.format(targetDb,targetTable))
			
	#writeFileUploadStatus(procparams,config_key,True)
	#deleteFiles(fileNames)


def executeJob(config_file,config_key,procparams,sourceDb='', targetDb='', targetTable=''):
	logging.info('****** Additional arguments: sourceDb: {}, targetDb: {}, targetTable: {}'.format(sourceDb, targetDb, targetTable))
	logging.info('config_file:: {} config_key:: {} procparams:: {}'.format(config_file,config_key,procparams))
	if (len(sourceDb) > 0 or len(targetDb) > 0 or len(targetTable) > 0):
		util.updateEmailContent(ADDITIONAL_ARGUMENTS, 'sourceDb: {}, targetDb: {}, targetTable: {}'.format(sourceDb, targetDb, targetTable))
	if len(sys.argv) >= 2:
		try:
			executeJobForConfig(config_file,config_key,procparams,sourceDb, targetDb, targetTable)
			if 0:
				util.updateEmailContent(ENDED_ON, time.strftime(timeFormat))
				util.sendEmail(RECEIVER,SENDER,'Finished job execution', EMAIL_SORTING)
		except Exception as ex:
			raise
			if 0:
				logging.error('****** Error occurred while executing DbReader scripts - {}'.format(ex.message))
				exc_traceback = sys.exc_info()
				traceback.print_tb(ex)
				util.updateEmailContent(JOB_FAILED, 'Exception occurred while processing job, please check the logs for more details.')
				sendEmail(RECEIVER,SENDER,JOB_FAILED, EMAIL_SORTING)

	else:
		logging.warn('Please provide the input parameters.')
		logging.warn('.... -k: <<Config Key to execute>>')
 
def processParamFile(paramFile):
	(sourceDb, targetDb, targetTable, requestFrom) = getDbInfo(paramFile)
	#pp((sourceDb, targetDb, targetTable, requestFrom))
	#e(0);
	util.updateEmailContent(REQUEST_FROM, requestFrom)
	logging.info('Read parameters from file: {}'.format(paramFile))
	with open(paramFile) as params:
		for i, param in enumerate(params):
			param = param.rstrip()
			logging.debug(param)
			if len(param) > 6 and str(param).startswith("'-k'") == True:
				param = ast.literal_eval(param)
				logging.info('Executing params - {}'.format(param))
				sys.argv = param
				executeJob(sourceDb, targetDb, targetTable)
				logging.info('Finished executing params - {}'.format(param))


def writeFileUploadStatus(mainParamList,config_key,successStatus=False,checkForPurge=False):
	if successStatus:
		statusDir=''
		fileName=''
		startFileName=''
		if config_key == 'ME_Position_TD':
			statusDir = '{}/{}'.format(VERTICA_SUCCESS_STATUS_DIR , TD_POSITION_DIR)
			startFileName='PositionTD'
			fileName='{}/{}_{}_{}_{}.{}'.format(statusDir,startFileName,mainParamList[0],mainParamList[2],mainParamList[3],'success')
		elif config_key == 'ME_FinancingPosition':
			statusDir = '{}/{}'.format(VERTICA_SUCCESS_STATUS_DIR , FIN_POSITION_DIR)
			startFileName='FinancingPosition'
			fileName='{}/{}_{}_{}.{}'.format(statusDir,startFileName,mainParamList[0],mainParamList[1],'success')
		elif config_key == 'ME_Position_SD':
			statusDir = '{}/{}'.format(VERTICA_SUCCESS_STATUS_DIR , SD_POSITION_DIR)
			startFileName='PositionSD'
			fileName='{}/{}_{}_{}_{}.{}'.format(statusDir,startFileName,mainParamList[0],mainParamList[1], mainParamList[3],'success')
		else:
			logging.info('Not a valid configKey for writing Status!!!')
			return
		fileName=fileName.replace('-','')
		logging('Status File: {}'.format(fileName))
		with open(fileName, 'w') as sFile:
			sFile.write('Success')
		sFile.clos	


from pprint import pprint as pp
def main():
	parser = ArgumentParser()
	parser.add_argument("--config", dest="config", help="JSON configuration file", type=str, required=True)
	parser.add_argument("--configKey", dest="configKey", help="Config Key", type=str, required=True)
	parser.add_argument("--paramsToProc", nargs="*", help="ParmasConfig Key", type=str, required=True)
	args = parser.parse_args()
	args = vars(args)
	#pp(args)
	#e()
	config_file = None
	logsPath = util.logSetup(LOG_DIR,LOG_FILE)
	util.updateEmailContent(STARTED_ON, time.strftime(timeFormat))
	util.updateEmailContent(LOGS_PATH, logsPath)
	logging.info('****** Starting Db Reader/Writer. Total number of arguments: {}'.format(sys.argv))
	
	util.updateEmailContent(PARAMETERS_PROVIDED, sys.argv)
	print('-'*80)
	try:
		config_file = os.path.basename(args['config'])
		if len(sys.argv) == 2:
			logging.info('****** DbReader script called- {}'.format(sys.argv))
			filePath = sys.argv[1]
			if os.path.exists(filePath) == False:
				raise Exception("File path does not exists - {}".format(filePath))
			
			processParamFile(filePath)
		elif len(sys.argv) > 2:
			if 1:
				
				
				executeJob(args['config'],args['configKey'],args['paramsToProc'])
				print 123
				e()
		else:
			raise
			logging.error('Either provide the input file path, or input parameters for job execution.')
			util.updateEmailContent(JOB_FAILED, 'Exception occurred while processing job, please check the logs for more details.')
			sendEmail(JOB_FAILED, EMAIL_SORTING)
			
	except Exception as ex:
		raise
		if 0:
			logging.error('****** Error occurred while executing DbReader scripts - {}'.format(ex.message))
			logging.error('****** Error - {}'.format(ex))
			exc_traceback = sys.exc_info()
			#traceback.print_tb(ex)
			print(exc_traceback)
			util.updateEmailContent(JOB_FAILED, 'Exception occurred while processing job, please check the logs for more details.')
			#util.sendEmail(JOB_FAILED, EMAIL_SORTING)
	
if __name__ == '__main__':
	#main()
	try:
		pyodbc.pooling = False
		

		conn = pyodbc.connect('DSN=IQDEV9;uid=CIGActgDownload;pwd=m0n3ybuck3t;db=CIGActgH')
		logging.debug('Successfule connection!!!')
		print 333
		e()
		cur = conn.cursor()

	except pyodbc.Error as pex:
		raise
		#message = 'Error occurred while downloading data - {}'.format(', '.join(pex))
		#raise Exception(message)
	except Exception as err:
		#logging.error("Unexpected error: {}".format(sys.exc_info()[0]))
		raise
		
