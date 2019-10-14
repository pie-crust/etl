import gzip
import StringIO, subprocess
fn1='122289_ACCT_1KCG182946PositionSide.bcp.SSrvr.temp' #630M
fn='122271_ACCT_CEFL182946PositionSide.bcp.SSrvr.temp' #17M
dir='/auto/fina-data/share/FARepository/prod/CIGActgS11/position/processing/Priority_3/PositionSide'
if 0:
	pipe = subprocess.Popen(["cat %s/%s | gzip --stdout" % (dir,fn)], stdout=subprocess.PIPE, shell=True)
cmd="dd status=progress if=%s/%s count=100 bs=10M | gzip --stdout"% (dir,fn1)

cmd="./ddskip.sh 1 5333 333 %s/%s| gzip --stdout" % (dir,fn)
   
print cmd
#pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
pipe = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)

helper = StringIO.StringIO()

while pipe.poll() is None:
	out=pipe.stdout.read(5)
	#print out, len(out)
	helper.write(out)
	#print 'posision:',helper.tell()
#helper.seek(0)
#output = gzip.GzipFile(fileobj=helper)
print 'final pos:', helper.tell()
#skip 4 bytes: dd count=10 skip=4 bs=1 if=./in.tmp
gzo = gzip.GzipFile(fileobj=helper)
helper.seek(0)
print '#'*60
print '>>>%s<<<' % gzo.read()
print '#'*60
"""
 i=$(((t=19876543212)-(h=4)))
   { dd count=0 skip=$h bs=1
     dd count=4 bs=2
     dd count=1 bs=1
   } <./in.tmp>./out.tmp
   
 i=$(((t=19876543212)-(h=4)))
   { dd count=0 skip=1 bs="$h"
     dd count="$((i/(b=64*1024)-1))" bs="$b"
     dd count=1 bs="$((i%b))"
   } <infile >outfile"""