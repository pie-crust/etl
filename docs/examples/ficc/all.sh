#!/bin/sh

alias python=~/python27/bin/python

 time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/snow_rest_snow/DY_FiccDistribution.json \
 --proc_params  Repo '2019-05-31' e5569eb7-e333-4e28-ad77-0f224a7d2499@1
 
 time python cli.py -nopp 3 --dump  -dcf config/db_config.DEV.json -pcf config/proc/ficc/snow_rest_snow/ME_FiccDistribution.json \
 --proc_params  Repo '2019-05-31' e5569eb7-e333-4e28-ad77-0f224a7d2499@1