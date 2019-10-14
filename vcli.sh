#!/usr/bin/bash
export PAGER='less -S'
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

. ./tools/vcli/odbc.sh
. ./tools/vcli/venv.sh
export VERTICA_USER=s_dev_actwrt

#kinit s_dev_rdm -k -t ../s_dev_rdm.keytab
kinit s_dev_actwrt -k -t /home/s_dev_racct/s_dev_actwrt.keytab


#./tools/vcli/dist/vcli

~/python27/bin/python2 ./tools/vcli/vcli.py
