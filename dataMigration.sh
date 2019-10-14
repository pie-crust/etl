#!/bin/sh

. ~/.FARprofile
unset LD_PRELOAD;
export LD_LIBRARY_PATH=/opt/unixodbc/lib64:/opt/vertica/lib64:/opt/sybase/IQ/Client/15.4/ESD7/IQ-15_4/lib64/:$LD_LIBRARY_PATH
export ODBCINI=/opt/home/etc/db/unixodbc/odbc.ini
export ODBCSYSINI=/opt/home/etc/db/unixodbc
unset PYTHONPATH


if [ "${home_ENV}" == "stabledev" ]
       then
               echo "${home_ENV} Setting conda env..."
               source /cigdev64/racct/anaconda2/bin/activate conda_racct27
elif [ "${home_ENV}" == "prod" ]
       then
               echo "${home_ENV} Setting conda env..."
               source /dataprod/racct/miniconda2/bin/activate conda_racct27
       else
               echo "Not a valid env...Exiting"
               exit
       fi

export PYTHONPATH=$RUNTIME64/racct/PyAcct/1.0/:$PYTHONPATH


export SIMBAINI=${RUNTIME64}racct/SSRSReportingServices/2.0/config/simba.snowflake.ini

DIR=`dirname $0`

echo "Argument provided to shell script: $@"
python ${DIR}/cli.py "$@"