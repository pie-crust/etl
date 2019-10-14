import sys
import pyodbc
from pprint import pprint as pp
e=sys.exit

if __name__=="__main__":
					
	if 1:
		pyodbc.pooling = False


	if 0:
		
		keyTabFile=os.getenv('SSRSREPORTINGKEYTABFILE'); assert keyTabFile
		keyTabPrincipal=os.getenv('DATASTAGINGSQLUSER'); assert keyTabPrincipal
		#setKeytabCache(KEYTABFILE, os.getenv('DATASTAGINGSQLUSER'), None)
		print ("kinit -k -t {} {}".format(keyTabFile, keyTabPrincipal))
		#e()
		os.system("kinit -k -t {} {}".format(keyTabFile, keyTabPrincipal))
		
	connS='DSN=MDIR01;Database=DataStaging;Trusted_Connection=yes;POOL=0;App=FiccApi'
	connS='DSN=MDFIN4;Database=MDFIN4;Trusted_Connection=yes;POOL=0;App=people-soft-bridge'
	#connS='DSN=MDDATAMART1;Database=Accounting;Trusted_Connection=yes;POOL=0;App=PositionReader'
	sconn = pyodbc.connect(connS)	
	scur = sconn.cursor()
	scur.arraysize=50000
	#scur.setinputsizes([(pyodbc.SQL_WVARCHAR, 0, 0)])
	if 1:
		
		stmt="SELECT COUNT(*) from DY_FiccDistribution"

		scur.execute(stmt)