import re
import sys
import time
import json
import logging
from logging.handlers import RotatingFileHandler
import smtplib
import os
from email.mime.text import MIMEText

TEXT_FORMAT = '%(asctime)-12s [%(levelname)s] %(message)s'
LOG_LEVEL = logging.DEBUG
contents = {}
V_SERVER =os.environ['VERTICASERVER'] if os.environ['VERTICASERVER'] is not None else ''
V_USER = os.environ['VERTICAUSER'] if os.environ['VERTICAUSER']  is not None else''
V_SCHEMA = os.environ['VERTICASCHEMA'] if os.environ['VERTICASCHEMA']  is not None else''
DATA_STAGING_SERVER = os.environ['DATASTAGINGSQLSERVER'] if os.environ['DATASTAGINGSQLSERVER'] is not None else ''
DATA_STAGING_DB = os.environ['DATASTAGINGDB'] if os.environ['DATASTAGINGDB'] is not None else ''
DEFAULT_DOMAIN = 'homeGROUP.COM'

def getParamValueFromArray(param, params):
	value = ''
	for idx, pname in enumerate(params):
		if pname.split('=')[0]==param:
			value = pname.split('=')[1]
	return value


def getParamValue(param):
	value = ''
	for idx, pname in enumerate(sys.argv):
		if pname==param and len(sys.argv) > idx:
			value = sys.argv[idx+1]
	return value

def getParamValueWithIndex(param):
	value = ''
	index = 0
	for idx, pname in enumerate(sys.argv):
		if pname==param and len(sys.argv) > idx:
			value = sys.argv[idx+1]
			index = idx+1
			break
	return (value, index)

def getParamsAsDict(start):
	params = {}
	idx = start
	for ind, pname in enumerate(sys.argv):
		if ind == idx and len(sys.argv) > idx:
			params[pname] = sys.argv[idx+1]
			idx += 2
	return params

def getParamsAsStringAfterIndex(start):
	params = ''
	idx = start
	for ind, pname in enumerate(sys.argv):
		if ind >= start:
			value = sys.argv[ind]
			if len(params) >= 1:
				params += ', '
			if type(value) is int or type(value) is bool or type(value) is long or type(value) is float:
				params += str(value)
			else:
				params += "'{}'".format(value)
			
	return params

def createTempFile(directory, fileName):
	if os.path.exists(directory) == False:
		os.makedirs(directory)
	fileName = os.path.join(directory, fileName)
	file = open(fileName, "wb")
	return file

def getTempFile(fileSuffix, fileExt, directory):
	fileName = '{}_{}.{}'.format(fileSuffix, time.strftime("%Y-%m-%d_%H-%M-%S"), fileExt)
	return createTempFile(directory, fileName)

def getTempFile(fileSuffix, count, fileExt, directory):
	fileName = '{}_{}-{}.{}'.format(fileSuffix, time.strftime("%Y-%m-%d_%H-%M-%S"), count, fileExt)
	return createTempFile(directory, fileName)

def loadConfigForKey(key, configFileName,sourceDb='', targetDb='', targetTable=''):
	#configFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), configFileName)
	with open(configFileName, 'r') as f:
		datastore = json.loads(f.read())

		targetDbs = datastore["targetDb"]
		dataConfigs = datastore["dataConfig"]

		configs = filter(lambda x: x['key'] == key, dataConfigs)
		if len(configs) > 0:
			config = configs[0]

			overrideConfiguration(sourceDb, None, targetDb, targetTable, config)
			setDbInfo(config, targetDbs)
			return config
		else:
			raise Exception("Configuration Key: '{}' not found. Please verify the provided parameters and config file".
				format(key))

def overrideConfiguration(sourceDb, sourceTable, targetDb, targetTable, targetUrl):
	if sourceDb != None and sourceDb != '' and len(sourceDb) > 0:
		targetUrl['sourceDb'] = sourceDb
		logging.info('Overriding Source DB as: {}'.format(sourceDb))
	if sourceTable != None and sourceTable != '' and len(sourceTable) > 0:
		targetUrl['sourceTable'] = sourceTable
		logging.info('Overriding Source Table as: {}'.format(sourceTable))
	if targetDb != None and targetDb != '' and len(targetDb) > 0:
		targetUrl['targetDb'] = targetDb
		logging.info('Overriding Target DB as: {}'.format(targetDb))
	if targetTable != None and targetTable != '' and len(targetTable) > 0:
		targetUrl['targetTable'] = targetTable
		logging.info('Overriding Target Table as: {}'.format(targetTable))

def getRestUrl(key, configFileName, sourceDb = None, sourceTable = None, targetDb= None, targetTable= None):
	configFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), configFileName)
	with open(configFilePath, 'r') as f:
		datastore = json.loads(f.read())
		targetUrls = datastore["restUrls"]
		targetDbs = datastore["targetDb"]
		if len(targetUrls) > 0:
			targetUrl = filter(lambda x: x['key'] == key, targetUrls)[0]
			overrideConfiguration(sourceDb, sourceTable, targetDb, targetTable, targetUrl)
			setDbInfo(targetUrl, targetDbs)
			return targetUrl
		else:
			raise Exception("Configuration Key: '{}' not found. Please verify the provided parameters and config file".
				format(key))


def setDbInfo(config, targetDbs):
	sourceDb = filter(lambda x: x['key'] == config['sourceDb'], targetDbs)[0]
	config['sourceDbConnectionString'] = sourceDb['connectionString']
	config['sourceDbKeyTabFile'] = sourceDb['keyTabFile'] if 'keyTabFile' in sourceDb else ''
	config['sourceDbKeyTabPrincipal'] = sourceDb['keyTabPrincipal'] if 'keyTabPrincipal' in sourceDb else ''

	targetDb = filter(lambda x: x['key'] == config['targetDb'], targetDbs)[0]
	config['targetDbConnectionString'] = targetDb['connectionString']
	config['targetDbKeyTabFile'] = targetDb['keyTabFile'] if 'keyTabFile' in targetDb else ''
	config['targetDbKeyTabPrincipal'] = targetDb['keyTabPrincipal'] if 'keyTabPrincipal' in targetDb else ''


def applyParamsOnProcConfig(params, procConfig):
	for key, val in params.items():
		paramExists = list(filter(lambda p: p['paramName'] == key, procConfig['parameters']))

		if len(paramExists) > 0:
			paramExists[0]['defaultValue'] = val
		else:
			raise Exception("Parameter: '{}' doesn't exists in configuration of {}".format(key, procConfig['key']))

def getSafeString(obj):
	try: return str(obj)
	except UnicodeEncodeError:
		return obj.encode('ascii', 'ignore').decode('ascii')
	return ""

def logSetup(logdir,fileName):
	if len(logging.getLogger().handlers) < 1:
		#directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir)
		#directory = os.path.join('/logdev/racct/DataMigration', dir) if os.path.exists('/logdev/racct/DataMigration') else os.path.dirname(os.path.realpath(__file__))
		if os.path.exists(logdir) == False:
			os.mkdir(logdir)
		filePath = os.path.join(logdir, fileName)
		
		logging.basicConfig(level=LOG_LEVEL, format=TEXT_FORMAT)
		rhandler = RotatingFileHandler(filePath, maxBytes=100000, backupCount=50)
		formatter = logging.Formatter(TEXT_FORMAT)  
		rhandler.setFormatter(formatter)
		rhandler.setLevel(LOG_LEVEL)
		logging.getLogger().addHandler(rhandler)
		print('Creating logs at - "{}"'.format(filePath))
		return filePath
	
def deleteFiles(fileNames):
	for fileName in fileNames:
		if os.path.exists(fileName):
			logging.info('Deleting file: {}'.format(fileName))
			os.remove(fileName)


def setEnvironment(keyTabFile, keyTabPrincipal):
	os.environ['LD_LIBRARY_PATH'] = "/opt/unixodbc/lib64:/opt/microsoft/msodbcsql/lib64:$LD_LIBRARY_PATH"
	os.environ['ODBCINI'] = "/opt/unixodbc/etc/odbc.ini"
	os.environ['ODBCSYSINI'] = "/opt/unixodbc/etc"
	os.environ['unset'] = "ODBCINST"
	os.environ['PYTHONPATH'] = "/opt/home/alt/lib64/python:$PYTHONPATH"
	# KeyTab file should already be set for the user under whose account this service is running -
	# https://wiki/display/OT/Setup+Kerberos+for+Database+Authentication+from+Linux
	# https://wiki/display/DEV/Microsoft+Linux+ODBC+Driver+for+SQL+Server#MicrosoftLinuxODBCDriverforSQLServer-Exampleusingkerberosforpasswordlessconnection
	if keyTabFile != '' and keyTabPrincipal != '':
		os.system("kinit -k -t {}/{} {}".format(os.environ['HOME'], keyTabFile, keyTabPrincipal))

def getDbInfo(paramFile):
	sourceDb = '';
	targetDb = '';
	targetTable = '';
	requestFrom = '';

	with open(paramFile) as params:
		logging.info('Read Db Info from file: {}'.format(paramFile))
		for i, param in enumerate(params):
			param = param.replace('\n', '')
			if str(param).startswith('sourceDb:') :
				param1 = str(param)[10:]
				sourceDb = json.loads(param1)['Server']
			elif str(param).startswith('targetDb:'):
				param1 = str(param)[10:]
				targetDb = json.loads(param1)['Server']
			elif str(param).startswith('targetTable:'):
				targetTable = re.sub("'", '', re.sub('"', '', str(param)[12:]))
			elif str(param).startswith('requestFrom:'):
				requestFrom = re.sub("'", '', re.sub('"', '', str(param)[12:]))

	return (sourceDb, targetDb, targetTable, requestFrom)

def readDbInfoFromFile(paramFile, retParams):
	with open(paramFile) as params:
		logging.info('Read Db Info from file: {}'.format(paramFile))
		for i, param in enumerate(params):
			param = param.replace('\n', '')
			for key in retParams:
				matchKey = "{}:".format(key)
				if str(param).startswith(matchKey):
					retParams[key] = str(param)[len(matchKey):]

	return retParams


def getEmailContents(sortBy):
	global contents
	content = ''
	try:
		for k in sortBy:
			if k in contents.keys():
				content += '{}:\t{}\n'.format(k, contents[k])
	except Exception as ex:
		content = ''
		for key in contents:
			content += '{}:\t{}\n'.format(key, contents[key])
	return content

from pprint import pprint as pp

def sendEmail(receiver,sender,subject, sortBy):
	global contents
	content = ''
	pp(getEmailContents(sortBy))

	if 0:
		try:
			content = getEmailContents(sortBy)
			if sender and receiver:
				msg = MIMEText(content)
				msg['Subject'] = subject
				msg['From'] = sender
				msg['To'] = 'oleksandr.buzunov@home.com'
				s = smtplib.SMTP('localhost')
				s.sendmail(sender, [receiver], msg.as_string())
				s.quit()
			else:
				logging.warn('SENDER or RECEIVER not defined'.format(sender,receiver))
		except Exception as ex:
			logging.error('****** Error occurred while sending email - {} \n Email contents: {}'.format(ex.message, content))
		contents = {}

def updateEmailContent(key, text):
	global contents
	if key in contents:
		contents[key] += str(' {}'.format(text))
	else:
		contents[key] = str(text)

def updateRecordsAdded(count):
	global contents
	contents["Records Added"] = int(count)

def formatVerticaConnectionString(connString):
	formattedconString=''
	if V_SERVER and V_USER:
		formattedconString=connString.format(V_SERVER,V_SERVER,V_USER)
	else:
			message="V_SERVER {} or V_USER {} not defined".format(V_SERVER,V_USER)
			logging.error(message)
			raise Exception(message)
	return  formattedconString

def formatSqlServerConnectionString(connString):
	formattedconString=''
	if DATA_STAGING_SERVER and DATA_STAGING_DB:
		formattedconString=connString.format(DATA_STAGING_SERVER,DATA_STAGING_DB)
	else:
			message="DATA_STAGING_SERVER {} or DATA_STAGING_DB {} not defined".format(DATA_STAGING_SERVER,DATA_STAGING_DB)
			logging.error(message)
			raise Exception(message)
	return  formattedconString

def setKeytabCache(keyTabFile, keyTabPrincipal='',isVertica=True):
	if isVertica:
		if keyTabFile != '':
			verticakeyTabPrincipal = V_USER + '@' + DEFAULT_DOMAIN
			os.system("kinit -k -t {} {}".format(keyTabFile, verticakeyTabPrincipal))
		else:
			message="keyTabFile {} not defined. Check environ variable KRB5_CLIENT_KTNAME".format(keyTabFile)
			logging.error(message)
			raise Exception(message)
	else:
		 if keyTabFile != '' and keyTabPrincipal != '':
			os.system("kinit -k -t {} {}".format(keyTabFile, keyTabPrincipal))
		 else:
			message="keyTabFile {} or keyTabPrincipal not defined. Check environ variable KRB5_CLIENT_KTNAME".format(keyTabFile,keyTabPrincipal)
			logging.error(message)
			raise Exception(message)


