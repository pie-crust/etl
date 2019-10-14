#!/usr/bin/env python

import csv
from datetime import datetime,timedelta
import json
import io
import os
import pyodbc
import socket
import stat
import sys
import time
import urllib
import smtplib
import shutil
import logging
import platform
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
import os.path
import getpass
import requests
from requests_kerberos import HTTPKerberosAuth


def GetAWSAccessCredentials(SF_DATA_FILE_DIRECTORY, SENDER, RECEIVER,SERVICE_NAME, logger):
    try:
        logger.info('GetAWSAccessCredentials: Getting active AWS access credential')
        aws_access_key_id = ''
        aws_secret_access_key = ''
        count = 0
        for i in range (0, 4):
            if count != 0:
                break
            res = requests.get('https://datakeep.homegroup.com/api/v2/get_access_credentials', auth=HTTPKerberosAuth())
            logger.info('response code for get aws access key is : {0} '.format(res.status_code))
            if res.status_code != 200:
                time.sleep(60)
                if i == 3:
                    aws_access_key_id, aws_secret_access_key = NewAWSAccessCredentials(SF_DATA_FILE_DIRECTORY, SENDER, RECEIVER,SERVICE_NAME,logger)
                    break
                else:
                    continue
            else:
                data = res.json()
                #count = 0
                length = len(data)
                if length > 0:
                    for l in data:
                        if count < 1:
                            json_str_obj = json.dumps(l)
                            json_dict = json.loads(json_str_obj)
                            aws_access_key_id = json_dict['access_key_id']
                            aws_secret_access_key = json_dict['secret_access_key']
                            owner = json_dict['owner']
                            start_time = json_dict['create_time']
                            end_time = json_dict['expire_time']
                            dt_obj_start = datetime.fromtimestamp(start_time)
                            dt_obj_end = datetime.fromtimestamp(end_time)
                            count = count + 1
                            logger.info('AWS credentials details are : aws_access_key_id : {0} : aws_secret_access_key : {1} : owner : {2} : create_time: {3} : expire_time : {4} '.format(aws_access_key_id, aws_secret_access_key, owner, dt_obj_start, dt_obj_end))
                            #break
                            #myErr = 'hello'
                            #EmailSend(SENDER,RECEIVER,'SnowFlake loader failed for {3} in {1} on host {0} for processing snap {2}  '.format(os.environ['HOSTNAME'],os.environ['home_ENV'],SF_DATA_FILE_DIRECTORY,SERVICE_NAME),myErr,logger)

                else:
                    aws_access_key_id, aws_secret_access_key = NewAWSAccessCredentials(SF_DATA_FILE_DIRECTORY, SENDER, RECEIVER,SERVICE_NAME,logger)
                    break

        return aws_access_key_id, aws_secret_access_key
            
    except Exception as ex:
        logger.exception('Exception processing data file {0} :: [{1}] '.format(SF_DATA_FILE_DIRECTORY,str(ex)))
        logger.critical('Exception processing data file {0} :: [{1}] '.format(SF_DATA_FILE_DIRECTORY,str(ex)))
        myErr = '''
        Data file: [{0}]

        Error:
        {1}
        '''.format(SF_DATA_FILE_DIRECTORY,str(ex))
        EmailSend(SENDER,RECEIVER,'SnowFlake loader failed for {3} in {1} on host {0} for processing snap {2}  '.format(os.environ['HOSTNAME'],os.environ['home_ENV'],SF_DATA_FILE_DIRECTORY,SERVICE_NAME),myErr,logger)
        sys.exit(1)
        
def NewAWSAccessCredentials(SF_DATA_FILE_DIRECTORY, SENDER, RECEIVER,SERVICE_NAME,logger):
    logger.info('NewAWSAccessCredentials: Unable to find the valid credentials through rest interface of datakeep so generating a new AWS credentials using POST request')
    try:
        lcount = 0
        aws_access_key_id = ''
        aws_secret_access_key = ''
        for x in range(0, 4):
            if lcount < 1:
                response = requests.post('https://datakeep.homegroup.com/api/v2/create_access_credentials', auth=HTTPKerberosAuth())
                if response.status_code == 200:
                    res = requests.get('https://datakeep.homegroup.com/api/v2/get_access_credentials', auth=HTTPKerberosAuth())
                    logger.info('response code for get aws access key is : {0} '.format(res.status_code))
                    if res.status_code == 200:
                        data = res.json()
                        length = len(data)
                        count = 0
                        if length > 0:
                            for l in data:
                                if count < 1:
                                    json_str_obj = json.dumps(l)
                                    json_dict = json.loads(json_str_obj)
                                    aws_access_key_id = json_dict['access_key_id']
                                    aws_secret_access_key = json_dict['secret_access_key']
                                    owner = json_dict['owner']
                                    start_time = json_dict['create_time']
                                    end_time = json_dict['expire_time']
                                    dt_obj_start = datetime.fromtimestamp(start_time)
                                    dt_obj_end = datetime.fromtimestamp(end_time)
                                    count = count + 1
                                    lcount = count
                                    logger.info('AWS credentials from else case are : aws_access_key_id : {0} : aws_secret_access_key : {1} : owner : {2} : create_time: {3} : expire_time : {4} '.format(aws_access_key_id, aws_secret_access_key, owner, dt_obj_start, dt_obj_end))

                    else:
                        time.sleep(60)
                        logger.info('get_access_credentials rest call response code is : {0} Unable to get AWS credentials from  so waiting for 60 and will try again'.format(res.status_code))
                else:
                    time.sleep(60)
                    logger.info('create_access_credentials rest call response code is : {0} Unable to get AWS credentials from  so waiting for 60 and will try again'.format(response.status_code))

        time.sleep(60)
        return aws_access_key_id, aws_secret_access_key

    except Exception as ex:
        logger.exception('Exception processing data file {0} :: [{1}] '.format(SF_DATA_FILE_DIRECTORY,str(ex)))
        logger.critical('Exception processing data file {0} :: [{1}] '.format(SF_DATA_FILE_DIRECTORY,str(ex)))
        myErr = '''
        Data file: [{0}]

        Error:
        {1}
        '''.format(SF_DATA_FILE_DIRECTORY,str(ex))
        EmailSend(SENDER,RECEIVER,'SnowFlake loader failed for {3} in {1} on host {0} for processing snap {2}  '.format(os.environ['HOSTNAME'],os.environ['home_ENV'],SF_DATA_FILE_DIRECTORY,SERVICE_NAME),myErr,logger)
        sys.exit(1)

def EmailSend(sender,receiver,subject,message,logger):
    logger.info("Sending output email to [{0}]".format(receiver))
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    #msg['To'] = receiver
    for rcp in receiver.split(','):
        msg.add_header('To',rcp)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('mailrelay.homegroup.com')
    # and message to send - here it is sent as one string.
    s.sendmail(sender, msg.get_all('To'), msg.as_string())
