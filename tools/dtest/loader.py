import os
import sys
import time
import json
import util
import pyodbc
import logging
from datetime import datetime
from util import *


timeFormat = "%Y-%m-%d %H:%M:%S"
V_SCHEMA = os.environ['VERTICASCHEMA'] if os.environ['VERTICASCHEMA'] is not None else ''

def getColumnsToCopy(columnMappings, timeToStamp, params):
	selectColumns = ''
	filterForPurge = ''
	for map in columnMappings:
		if len(selectColumns) > 0:
			selectColumns += ','
		
		if map['value'] == 'Default':
			if map['valueType'] == 'TimeStamp':
				selectColumns += " {} as '{}'".format(map['columnName'], timeToStamp)
			else:
				selectColumns += " {} as '{}'".format(map['columnName'], map['valueType'])
		elif map['value'] == 'Param':
			selectColumns += " {} as '{}'".format(map['columnName'], params[map['sourceParam']])
			filterForPurge += " AND {} = '{}'".format(map['columnName'], params[map['sourceParam']])
		else:
			selectColumns += " {}".format(map['columnName'])
	return selectColumns, filterForPurge

def countAddedData(cursor, db, table, updatedBefore, filterForPurge = ''):
	logging.info('Counting data in table: "{}.{}" for records added at : {} and filter: {}'.format(
			db, table, updatedBefore, filterForPurge))
	try:
		cmd = "SELECT COUNT(1) from {}.{} WHERE AsOfDateTime = '{}' ".format(
				db, table, datetime.strptime(updatedBefore, timeFormat))
		if filterForPurge != '':
			cmd += filterForPurge
		logging.debug(cmd)
		cursor.execute(cmd)
		rows = cursor.fetchall()
		if len(rows) > 0:
			cnt = rows[0][0]
			updateRecordsAdded(cnt)
		else:
			updateRecordsAdded(0)
	except Exception as ex:
		logging.error("Exception while counting data from {}.{} for records added at: '{}' - {}".format(
						db, table, updatedBefore, ', '.join(ex)))


def purgeExistingData(cursor, db, table, updatedBefore, filterForPurge = ''):
	logging.info('Purging data in table: "{}.{}" for records updated before: {} and filter: {}'.format(
			db, table, updatedBefore, filterForPurge))
	try:
		cmd = "DELETE from {}.{} WHERE AsOfDateTime < '{}' ".format(db, table, datetime.strptime(updatedBefore, timeFormat))
		print (cmd)
		if filterForPurge != '':
			cmd += filterForPurge
		print filterForPurge
		print cmd
		sys.exit()
		logging.debug(cmd)
		cursor.execute(cmd)
		logging.info('Purged data in table: "{}.{}" for records updated before: {}'.format(
			db, table, updatedBefore))
	except Exception as ex:
		logging.error("Exception while purging data from {}.{} for records updated before: '{}' - {}".format(
						db, table, updatedBefore, ', '.join(ex)))

def uploadData(config, sourceFilePath, columnsToCopy, timeStamp, filterForPurge):
	if os.path.exists(sourceFilePath) == False:
		raise Exception('File path does not exists: {}'.format(sourceFilePath))
	logging.info('Loading data from file: "{}" to target: {}.{}'.format(sourceFilePath, config['targetDb'], config['targetTable']))

	try:

		pyodbc.pooling = False
		connString = formatVerticaConnectionString(config['targetDbConnectionString'])
		keytabfile = os.environ['KRB5_CLIENT_KTNAME']
		setKeytabCache(keytabfile)
		conn = pyodbc.connect(connString)
		cursor = conn.cursor()
		rejectionFile = sourceFilePath + '.rejections'
		exceptionFile = sourceFilePath + '.exceptions'
		targetDb = V_SCHEMA if config['targetDb'] == "verticadb" else ''
		logging.info("Starting copying data from file - '{}' to target table - {}. \n Rejection File - {} \n Exception File - {}".format(
						sourceFilePath,config['targetTable'], rejectionFile, exceptionFile))
		cmd = """COPY {}.{}({}) FROM LOCAL '{}'
					PARSER public.FCSVParser(type='traditional', escape='\\')
					DELIMITER ',' ENCLOSED BY '\"'
					REJECTED DATA '{}'
					EXCEPTIONS '{}'
					SKIP 1 ABORT ON ERROR""".format(
						targetDb, config['targetTable'], columnsToCopy, sourceFilePath, rejectionFile, exceptionFile)

		logging.debug(cmd)
		cursor.execute(cmd)
		
		purgeExistingData(cursor, targetDb, config['targetTable'], timeStamp, filterForPurge)
		conn.commit()
		
		#Keep the count of records added, used for email notification
		countAddedData(cursor, targetDb, config['targetTable'], timeStamp, filterForPurge)
		cursor.close()
		conn.close()
		raiseRejectionWarning(rejectionFile, exceptionFile)
	except pyodbc.Error as pex:
		message = 'Error occurred while uploading data - {}'.format(', '.join(pex))
		logging.error(message)
		raise Exception(message)
	logging.info("Completed copying data from file to target table.")

def raiseRejectionWarning(rejectionFile, exceptionFile):
	if os.path.exists(rejectionFile) == True:
		logging.warn("""WARNING:: Some records are rejected during data migration. 
					Please look for the following files: \n{} \n""".format(rejectionFile, exceptionFile))

def main(targetDb='', targetTable=''):
	logSetup('DbWriter', 'dbReaderWriter.log')
	logging.info('Argument List (Total- {}) : {}'.format(len(sys.argv), str(sys.argv)))
	if len(sys.argv) >= 4:
		try:
			configKey=getParamValue('-configkey')
			configFile=getParamValue('-configFile')
			timeToStamp = getParamValue('-t')
			params = getParamValue('-p')
			config = loadConfigForKey(configKey, configFile, targetDb, targetTable)
			logging.info('Config to execute: {} with TargetDbConnString: "{}"'.format(config['key'], config['targetDbConnectionString']))
						
			columnsToCopy, filterForPurge = getColumnsToCopy(config['columnMappings'], timeToStamp, params)

			sourceFilePath = getParamValue('-f')
			uploadData(config, sourceFilePath, columnsToCopy, timeToStamp, filterForPurge)
		except Exception as ex:
			logging.error('Error occurred while executing DbWriter scripts - {}'.format(ex.message))
			raise Exception(ex.message)
		logging.info("****** Completed data upload.")

	else:
		logging.warn('Please provide the input parameters.')
		logging.warn('.... -k: <<Configuration Key>>')
		logging.warn('.... -f: <<Source File path>>')
	
