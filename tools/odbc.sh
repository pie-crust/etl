
unset LD_PRELOAD;
export LD_LIBRARY_PATH=/opt/unixodbc/lib64:/opt/vertica/lib64:/opt/sybase/IQ/Client/15.4/ESD7/IQ-15_4/lib64/:$LD_LIBRARY_PATH
export ODBCINI=/opt/home/etc/db/unixodbc/odbc.ini
export ODBCSYSINI=/opt/home/etc/db/unixodbc
export PYTHONPATH=$RUNTIME64/racct/PyAcct/1.0/:$PYTHONPATH
export KRB5_CLIENT_KTNAME=$SSRSREPORTINGKEYTABFILE

export SIMBAINI=/home/s_dev_racct/ab_ssrs_reporting_services/simba.snowflake.ini

export DB_IQ_UID=CIGActgDownload
export DB_IQ_PWD='m0n3ybuck3t'
export DB_IQ_DATABASE=CIGActgH
export IQREADERSERVER=IQPROD9
export IQREADERSERVER_DEV=IQDEV9
