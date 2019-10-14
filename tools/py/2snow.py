import snowflake.connector

OKTA_USER = 's_dev_racct@homegroup.com'
OKTA_PASSWORD = 'home312!'
con = snowflake.connector.connect(
  user=OKTA_USER,
  password=OKTA_PASSWORD,
  account='e855cad',
  authenticator='https://home.okta.com',
  warehouse='LOAD_WH',
  database='ACCOUNTINGBI',
  schema='POSITION'
)

