3 procs, Sample call below: 

alias python=~/python27/bin/python

#DY_DeskPLRSRange03
time python cli.py -nopp 17  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params \
223906 '01/01/2017'  '01/04/2017' EOD '*' \
'*' '*' '*' 'HORZ' '*' '*' 'ALL' \
'LOOK_BACKWARD_BUC' 'NYS' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'\
 2>&1| tee DY_DeskPLRSRange03.log

 #DY_DeskPLRSRange03
time python cli.py -nopp 18  -dcf config/db_config.json -pcf config/proc/3/iq_stream_s3_snow/DY_DeskPLRSRange03.json --proc_params \
223906 '01/04/2017' '01/04/2017'   'EOD' '*'  'HORZ'  '*' '*'  '*' '*' '*' 'ALL' 'TABLE_EDITOR_DEFAULT' 'TABLE_EDITOR_DEFAULT' 'DESK_PL_RANGE_03' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'

 
 223906, '01/04/2017', '01/04/2017',   'EOD', '*',  'HORZ',  '*', '*',   '*', '*', '*',  'ALL',  'TABLE_EDITOR_DEFAULT',  'TABLE_EDITOR_DEFAULT', 'DESK_PL_RANGE_03',  'FUND',  'ABOVE_THE_WALL', 's_prod_racct'

 SET TEMPORARY OPTION DATE_ORDER=MDY exec CIGActgS11.spDeskPLBUC_Inner_Range_01 '223906','01/04/2017','01/04/2017','EOD','*','HORZ','*','*','*','*','*','ALL', 'TABLE_EDITOR_DEFAULT','TABLE_EDITOR_DEFAULT','DESK_PL_RANGE_03','FUND','ABOVE_THE_WALL','s_prod_racct'
 
 SET TEMPORARY OPTION DATE_ORDER=MDY
IEXEC CIGActgS11.spDeskPLBUC_Inner_Range_01  @pClientID= 223906, @pStartDate= '01/04/2017', @pEndDate = '01/04/2017',
	@pStage = 'EOD', @pDesk= '*', @pBuName = 'HORZ', @pInstrument = '*', @pStrategy = '*',  @pMCRollup = '*', @pPosBlock = '*',
	@pFund= '*', @pAdjustmentLogic = 'ALL', @pWeekendLogic = 'TABLE_EDITOR_DEFAULT', @pCalendar = 'TABLE_EDITOR_DEFAULT', @pStoredProcedure = 'DESK_
PL_RANGE_03',
	@pAllocationLogic = 'FUND',  @FirewallAllowedDeskIDs='ABOVE_THE_WALL', @pUserId ='s_prod_racct'

			
 s
IEXEC CIGActgS11.spDeskPLBUC_Inner_Range_01
@pClientID= 223906, @pStartDate= '01/04/2017', @pEndDate = '01/04/2017',
	  @pStage = 'EOD', @pDesk= '*', @pBuName = 'HORZ', @pInstrument = '*', @pStrategy = '*',  @pMCRollup = '*', @pPosBlock = '*',
	  @pFund= '*', @pAdjustmentLogic = 'ALL', @pWeekendLogic = 'TABLE_EDITOR_DEFAULT', @pCalendar = 'TABLE_EDITOR_DEFAULT', @pStoredProcedure = 'DESK_PL_RANGE_03',
	  @pAllocationLogic = 'FUND',  @FirewallAllowedDeskIDs='ABOVE_THE_WALL', @pUserId ='s_prod_racct'

		  
		  

exec CIGActgH.spDeskPLRSRange03_WRAPPER @pClientID = 223906, @pStartDate = '01/01/2017', @pEndDate = '01/04/2017', @pStage = 'EOD', @pDesk = '*',
 @pPosBlock = '*', @pInstrument = '*', @pStrategy = '*', @pBuName = '*', @pFund = '*', @pMCRollup = '*', @pAdjustmentLogic = 'ALL', 
 @pWeekendLogic = 'LOOK_BACKWARD_BUC', @pCalendar = 'NYS', @pAllocationLogic = 'NONE', @FirewallAllowedDeskIDs='ABOVE_THE_WALL', @pUserId='s_prod_racct'                                                                                                                                                                                                                                                                             


 #DY_DeskPLRVCRange02
time python cli.py -nopp 15  -dcf config/db_config.json -pcf config/proc/3/iq_s3_snow/DY_DeskPLRVCRange02.json --proc_params \
223906 '01/01/2017'  '01/04/2017' EOD '*' \
'*' 'HORZ' '*' '*' 'ALL' \
'LOOK_BACKWARD_BUC' 'NYS' 'FUND' 'ABOVE_THE_WALL' 's_prod_racct'\
 2>&1| tee DY_DeskPLRVCRange02.log
 
 
exec CIGActgH.spDeskPLRVCRange02_WRAPPER @pClientID = 223906, @pStartDate = '01/01/2017', @pEndDate = '01/04/2017', @pStage = 'EOD', @pDesk = '*', 
@pStrategy = '*', @pBuName = '*', @pFund = '*', @pMCRollup = '*', @pAdjustmentLogic = 'ALL', 
@pWeekendLogic = 'LOOK_BACKWARD_BUC', @pCalendar = 'NYS', @pAllocationLogic = 'NONE', @FirewallAllowedDeskIDs='ABOVE_THE_WALL', @pUserId='s_prod_racct'