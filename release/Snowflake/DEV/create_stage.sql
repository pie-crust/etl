create or replace stage ACCOUNTINGBI.POSITION.POSITION_MODEL_STAGE_TEST_2 url='s3://home-pmt-accounting-dev/racct/'
file_format = (type = 'CSV' field_delimiter = '^' field_optionally_enclosed_by='\"');


create or replace stage ACCOUNTINGBI.POSITION.POSITION_MODEL_STAGE_TEST_PIPE 
url='s3://home-pmt-accounting-dev/racct/'
file_format = (type = 'CSV' field_delimiter = '|' field_optionally_enclosed_by='\"');


