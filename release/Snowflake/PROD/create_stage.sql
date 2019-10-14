create or replace stage ACCOUNTINGBI.POSITION.POSITION_MODEL_STAGE  url='s3://home-pmt-accounting-prod/racct/'
file_format = (type = 'CSV' field_delimiter = '^' field_optionally_enclosed_by='\"')"