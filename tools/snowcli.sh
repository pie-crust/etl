export PAGER='less -S'
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8


. ~/.FARprofile
. ~/ab_ssrs_reporting_services/.envs/.odbc
. ~/ab_ssrs_reporting_services/.envs/.DEV.Snowflake


~/python3/bin/python3 ~/snowcli/main.py
