unset LD_PRELOAD;
export LD_LIBRARY_PATH=/opt/unixodbc/lib64:$PWD/tools/vcli/vertica:$LD_LIBRARY_PATH
export ODBCINI=$PWD/tools/vcli/unixodbc/odbc.ini
export ODBCSYSINI=$PWD/tools/vcli/unixodbc
export PYTHONPATH=$RUNTIME64/racct/PyAcct/1.0/:$PYTHONPATH
export KRB5_CLIENT_KTNAME=$SSRSREPORTINGKEYTABFILE

