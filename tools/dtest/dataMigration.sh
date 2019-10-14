#!/bin/sh
# Copyright (c) 2000, 2002 - 2012 home LLC, Confidential
# Information of home LLC, or its affiliates.  All rights reserved
. ~/.FARprofile
unset LD_PRELOAD;
export LD_LIBRARY_PATH=/opt/unixodbc/lib64:/opt/vertica/lib64:/opt/sybase/IQ/Client/15.4/ESD7/IQ-15_4/lib64/:$LD_LIBRARY_PATH
export ODBCINI=/opt/home/etc/db/unixodbc/odbc.ini
export ODBCSYSINI=/opt/home/etc/db/unixodbc
export PYTHONPATH=$RUNTIME64/racct/PyAcct/1.0/:$PYTHONPATH
export KRB5_CLIENT_KTNAME=$SSRSREPORTINGKEYTABFILE

DIR=`dirname $0`

echo "Argument provided to shell script: $@"
/opt/home/bin/python ${DIR}/reader.py "$@"
