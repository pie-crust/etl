
Back to [README](../README.md)


# Ficc examples (Snowflake->REST->Snowflake)

## Daily process:

 * Cli gets ref codes from Snowflake **DY_FinancingPosition** and calls REST API.
 * Snowflake loader uses conventional insert to load data to Snowflake **DY_FiccDistribution** table.
 
## Monthly process:

 * Cli gets ref codes from Snowflake **ME_FinancingPosition** and calls REST API.
 * Snowflake loader uses conventional insert to load data to Snowflake **ME_FiccDistribution** table.

## Examples

 --proc_params
 
* pa[0] = ReferenceType
* pa[1] = AccountingDate
* pa[2] = gatoken


### Daily 
```
export GA_TOCKEN=<>

 time python cli.py -nopp 4 -rte DEV -dcf config/db_config.DEV.json -pcf config/proc/snow_rest_snow/DY_FiccDistribution.json \
 --proc_params  Repo '2019-05-31' $GA_TOCKEN
 
```

### Monthly

```
export GA_TOCKEN=<>

 time python cli.py -nopp 4 --dump  -dcf config/db_config.DEV.json -pcf config/proc/snow_url_snow/ME_FiccDistribution.json \
 --proc_params  Repo '2019-05-31' $GA_TOCKEN

```
