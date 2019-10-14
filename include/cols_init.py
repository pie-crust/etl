cmd={}; result={}; a={'Snow':{},'IQ':{},'S3':{}}
if 1:
	cmd['DY_FinancingPosition']={
	'IQ':	{'proc':'CIGActgH.spTDPFinancialPosRptCnsldtd_WRAPPER', 
			'params':"223906 05/01/2019 05/01/2019 EOD EOD '*' '*' '*' NONE '*' NOW 0"},
	'Snow':	{'table':"DY_FinancingPosition"},
	'S3':	{'key':"file_0.IQStreamer.7epMzJ.20190527_140953.csv.gz" ,"num_of_cols":100},
	}
	

	 
if 1:
	cmd['ME_FinancingPosition']={
	'IQ':	{'proc':'CIGActgH.spTDPFinancialPosRptCnsldtd_WRAPPER', 
			'params':"223906 05/01/2019 05/31/2019 EOD EOD '*' '*' '*' NONE '*' NOW 0"},
	'Snow':	{'table':"ME_FinancingPosition"},
	'S3':	{'key':"file_0.IQStreamer.7epMzJ.20190527_140953.csv.gz" ,"num_of_cols":100},
	}
	

	 

if 1:
	cmd['ME_13F']={
	'IQ':	{'proc':'CIGActgH.sp_Util_13F_WRAPPER', 
			'params':"'03/31/2019' 223906 'EOD' '*' '0' 'ALL' 'DETAIL' '*' 0 'N' 'N' 'N' "},
	'Snow':	{'table':"ME_13F"},
	'S3':	{'key':"file_0.IQ.RSEVpo.20190607_091206.csv.gz","num_of_cols":40},
	}
	
	

	
if 1:
	cmd['DY_Position_SD']={
	'IQ':	{'proc':'CIGActgH.spSettleDatePosition_WRAPPERR', 
			'params':'223906 05/01/2018 "EOD" "ACCT" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" '},
	'Snow':	{'table':"DY_Position_SD"},
	'S3':	{'key':"file0.IQStreamer.q6Co8n.20190523_151911.csv.gz","num_of_cols":40},
	}
	 
if 1:
	cmd['ME_Position_SD']={
	'IQ':	{'proc':'CIGActgH.spSettleDatePosition_WRAPPER', 
			'params':"""223906 05/01/2018 'EOD' 'ACCT' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" """},
	'Snow':	{'table':"ME_Position_SD"},
	'S3':	{'key':"file0.IQStreamer.q6Co8n.20190523_151911.csv.gz","num_of_cols":40},
	}
	 
	

	
if 1:
	cmd['DY_Position_TD']={
	'IQ':	{'proc':'CIGActgH.spSOI_Cnsldtd_WRAPPER', 
			'params':" '223906' 'EOD' '05/01/2019' 'ACCT' 'CEFL' 'DEFAULT' 'REGULAR' '1' '0' 'NONE' '*' '*' 'N' '0' '0' 'NONE' 'NONE' 'ALL' '0' 'MONTH_END' 'N' 'ALL' '*' '0' '*' 'N' '*' "},
	'Snow':	{'table':"DY_Position_TD"},
	'S3':	{'key':"file0.IQStreamer.q6Co8n.20190523_151911.csv.gz","num_of_cols":40},
	}
	
	
	
if 1:
	cmd['ME_Position_TD']={
	'IQ':	{'proc':'CIGActgH.spSOI_Cnsldtd_WRAPPER', 
			'params':"  '223906' 'EOD'  '05/31/2019' 'ACCT' '*' 'DEFAULT' 'REGULAR' '1' '0' 'NONE' '*' '*' 'N' '0' '0' 'NONE' 'NONE' 'ALL' '0' 'FULL' 'N' 'ALL' '*' '0' '*' 'Y' '*' "},
	'Snow':	{'table':"ME_Position_TD"},
	'S3':	{'key':"file0.IQStreamer.q6Co8n.20190523_151911.csv.gz","num_of_cols":40},
	}
	
for key in cmd.keys():
	result[key]=a
if __name__ == "__main__":
	for key, val  in cmd.items():
		params= val['IQ']['params']
		print (key )
		print ('time python cli.py -nopp %d --no-dump  -dcf config/db_config.json -pcf config/proc/iq_s3_snow/%s.json --proc_params \
%s  2>&1| tee %s.log' % (len(params.split()), key ,params, key))
