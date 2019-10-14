import sys
import gzip
import StringIO, subprocess
e=sys.exit
fn='122289_ACCT_1KCG182946PositionSide.bcp.SSrvr.temp' #630M
fn='122265_DESK_BC2M182952PositionSide.bcp.SSrvr.temp' #2.7G
#fn='122271_ACCT_CEFL182946PositionSide.bcp.SSrvr.temp' #17M
fn='122261_DESK_CDRG182952PositionSide.bcp.SSrvr.temp'
dir='/auto/fina-data/share/FARepository/prod/CIGActgS11/position/processing/Priority_3/PositionSide'
#cat test_0.csv  test_1.csv  test_2.csv  test_3.csv  test_4.csv  test_5.csv  test_6.csv  test_7.csv  test_8.csv  test_9.csv  test_10.csv  test_11.csv  test_12.csv  test_13.csv  test_14.csv  test_15.csv  test_16.csv  test_17.csv  test_18.csv  test_19.csv  test_20.csv  test_21.csv  test_22.csv  test_23.csv  test_24.csv  test_25.csv  test_26.csv  test_27.csv  test_28.csv  test_29.csv  test_30.csv  test_31.csv  test_32.csv  test_33.csv  test_34.csv  test_35.csv  test_36.csv  test_37.csv  test_38.csv  test_39.csv  test_40.csv  test_41.csv  test_42.csv  test_43.csv  test_44.csv  test_45.csv  test_46.csv  test_47.csv  test_48.csv  test_49.csv  test_50.csv  test_51.csv  test_52.csv  test_53.csv  test_54.csv  test_55.csv  test_56.csv  test_57.csv  test_58.csv  test_59.csv  test_60.csv  test_61.csv  test_62.csv  test_63.csv  test_64.csv  test_65.csv  test_66.csv  test_67.csv  test_68.csv  test_69.csv  test_70.csv  test_71.csv  test_72.csv  test_73.csv  test_74.csv  test_75.csv  test_76.csv  test_77.csv  test_78.csv  test_79.csv  test_80.csv  test_81.csv  test_82.csv  test_83.csv  test_84.csv  test_85.csv  test_86.csv  test_87.csv  test_88.csv  test_89.csv  test_90.csv  test_91.csv  test_92.csv  test_93.csv  test_94.csv  test_95.csv  test_96.csv  test_97.csv  test_98.csv  test_99.csv>/auto/fina-data/share/FARepository/prod/CIGActgS11/position/processing/Priority_3/PositionSide/all.csv


if 0:
	for i in range(100):
		print 'test_%d.csv ' % i, 
	e()
cs=10<<23
print cs
proc=[]
for i in range(20):
	skip_to, read_to, chunk= i*cs,cs,cs/2-1
	cmd="./skipscan.sh %d %d %d %s/%s | gzip --stdout>test_%d.gz" % (skip_to, read_to, chunk, dir,fn, i)
	print cmd
	#pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	pipe = subprocess.Popen([cmd], stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
	proc.append(pipe)
if 1:
	out={}
	for pid, pipe in enumerate(proc):
		out[pid]=[]
		line= pipe.stdout.readline()
		while line: #pipe.poll() is None:
			out[pid].append(line)
			line= pipe.stdout.readline()

		line= pipe.stderr.readline()
		while line: #pipe.poll() is None:
			out[pid].append(line)
			line= pipe.stderr.readline()

		while	pipe.poll() is None:
			print 'Waiting...%d' % i
		
		
	
if 0:
	out=[]
	line= pipe.stdout.readline()
	while line: #pipe.poll() is None:
		out.append(line)
		line= pipe.stdout.readline()

	line= pipe.stderr.readline()
	while line: #pipe.poll() is None:
		out.append(line)
		line= pipe.stderr.readline()


	for id, l in enumerate(out):
		print('[%d]: %s' % ( id,l))
	while	pipe.poll() is None:
		print 'Waiting...%d' % i
	


