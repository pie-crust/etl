# sql-over-outlook
* [Max Elapsed] (tools/posix/max_elapsed.py)
Executes SQL over Outlook emails using Python.

## Email example
```
Parameters provided: ['/prod64/rest/SSRSReportingServices/2.0/cli.py', '-nopp', '27', '-rte', 'PROD', '-dcf', 'config/db_config.PROD.json', '-pcf', 'config/proc/position/test/DY_Position_TD.json', '--proc_params', '223907', 'EOD', '2019-07-23', 'DESK', '*', 'DEFAULT', 'REGULAR', '1', '0', 'NONE', '*', '*', 'N', '0', '0', 'NONE', 'NONE', 'ALL', '0', 'MONTH_END', 'N', 'ALL', '*', '0', '*', 'N', '*']
Source: IQ - SCHEMA1.sp0007_WRAPPER
Target: Snowflake - DY_Position_TD
Started On: 2019-07-24 12:00:20
Ended On: 2019-07-24 13:12:18
Records Added: 4,180,659
Logs Path: /auto/pric/DUSF/PROD/cli/test/DY_Position_TD/20190724_120019/cli_6447_4HP1qB.log

```
## SQL used
```SQL
SELECT tname, asodt, max(  Cast ((  JulianDay(ended_on) - JulianDay(started_on)) * 24 * 60  As Integer)) diff 
from stats 
group by 1, 2 
order by 1 desc,2 desc
```

## Result
```
C:\temp\Python37-32>python max_elapsed.py
DY_Position_TD,  2019-07-23      71
DY_Position_TD,  2019-07-22      67
DY_Position_TD,  2019-07-19      79
DY_Position_SD,  2019-07-23      6
DY_Position_SD,  2019-07-22      6
DY_Position_SD,  2019-07-19      6
DY_FinancingPosition,    2019-07-23      16
DY_FinancingPosition,    2019-07-22      15
DY_FinancingPosition,    2019-07-19      15
```

