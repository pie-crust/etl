"""
time python cli2.py -nopp 18 -dcf config/db_config.json -pcf config/proc/iq_s3_snow/DY_Position_SD.json --proc_params  \
223906 05/30/2019 'EOD' 'DESK' "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" "*" -ld 100\
 2>&1| tee DY_Position_SD.log 
"""
import time
import threading
import subprocess
from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init


IQ 				= create_reader('IQ',  app_init=app_init			)
Snowflake 		= create_writer('Snowflake',  app_init=app_init		) 
S3StreamLoader	= create_writer('S3StreamLoader', app_init=app_init )
Email 	  		= create_actor ('Email', app_init=app_init 			)


IQ_cursor		= InOut()
s3_file_names	= InOut()
snow_conn		= InOut()
iq_data			= InOut()
file_size_rows=200000
##
##
email_args={'email_subject':'IQ->Snowflake'}
##
##
threads={}
s3_file_names.file_names=[]

def compress_file(from_fn):
	subprocess.call(['gzip', from_fn], shell=False)
def s3_upload(cmd):
	
	print cmd
	subprocess.call([cmd], shell=True)	

def upload_file(fname, cmd, rmcmd,snow_conn):
	print('Starting %s' % fname)
	compress_file(fname)
	subprocess.call([cmd], shell=True)	
	to_file='%s.gz' % fname
	s3fn	= InOut()
	s3fn.file_names=[]
	s3fn.file_names.append(to_file)
	Snowflake.bulk_copy( trans	= snow_conn, file_names = s3fn, target=cli.tcfg, qname = 'copyStmt')
	os.remove(to_file)
	subprocess.call([rmcmd], shell=True)	
	
	
def run():	
	running_procs=[]
	IQ.set_loader(Snowflake)
	Snowflake.begin_transaction ( out = snow_conn )	
	for tid, out in enumerate(IQ.fetch_many(chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=iq_data,skip_header=0)):
		fname='file_%s_%s.csv' % (tid , len(iq_data.data))
		s3_file_names.file_names.append('%s.gz' % fname)
		with open(fname, 'wb') as fh:
			for l in iq_data.data:
				fh.write(l)
			
		
		if 0:
			cmd='aws s3 cp %s.gz s3://home-pmt-accounting-dev/racct/DY_Position_SD/' % fname
			rmcmd='aws s3 rm s3://home-pmt-accounting-dev/racct/DY_Position_SD/%s.gz' % fname
			threads[tid]=threading.Thread(target=upload_file, kwargs={'fname':fname, 'cmd': cmd, 'rmcmd': rmcmd,'snow_conn':snow_conn})
			threads[tid].start()
		if 1:
			from subprocess import Popen, PIPE
			import time

			running_procs.append(Popen(['/usr/bin/my_cmd', '-i %s' % path], stdout=PIPE, stderr=PIPE))



				# Here, `proc` has finished with return code `retcode`
				if retcode != 0:
					"""Error handling."""
				handle_results(proc.stdout)
	
		
		tid +=1
	if 1:
	
		while running_procs:
		
			for proc in running_procs:
				retcode = proc.poll()
				print(retcode)
				time.sleep(5)
				if 0:
					if retcode is not None: # Process finished.
						running_procs.remove(proc)
						break
					else: # No process is done, wait a bit and check again.
						time.sleep(.1)
						continue

	if 0:
		for t in threads.values():
			t.join()

	if 0:
		#Snowflake.begin_transaction ( out = snow_conn )	
		Snowflake.purge_data		( trans	= snow_conn, stmt = 'purgeStmt' )
		#Snowflake.bulk_copy			( trans	= snow_conn, file_names = s3_file_names, target=cli.tcfg, qname = 'copyStmt')
		Snowflake.commit_transaction( trans	= snow_conn )
	if 0:
		S3StreamLoader.delete_files ( file_names=s3_file_names)
	Email.send_email			( **email_args )

def run2():	
	IQ.set_loader(Snowflake)
	IQ.fetch_many(chunk_size=file_size_rows,  source = cli.scfg, qname = 'sourceStmt', out=iq_data,skip_header=0)
	tid=0
	
	while iq_data.data:
		fname='file_%s_%s.csv' % (tid , len(iq_data.data))
		s3_file_names.file_names.append('%s.gz' % fname)
		with open(fname, 'wb') as fh:
			for l in iq_data.data:
				fh.write(l)
			
		
		if 1:
			cmd='aws s3 cp %s.gz s3://home-pmt-accounting-dev/racct/DY_Position_SD/' % fname
			rmcmd='aws s3 rm s3://home-pmt-accounting-dev/racct/DY_Position_SD/%s.gz' % fname
			threads[tid]=threading.Thread(target=upload_file, kwargs={'fname':fname, 'cmd': cmd , 'rmcmd': rmcmd })
			threads[tid].start()
		
		IQ.fetch_next(out=iq_data)
		tid +=1
	
	for t in threads.values():
		t.join()

	if 1:
		Snowflake.begin_transaction ( out = snow_conn )	
		Snowflake.purge_data		( trans	= snow_conn, stmt = 'purgeStmt' )
		Snowflake.bulk_copy			( trans	= snow_conn, file_names = s3_file_names, target=cli.tcfg, qname = 'copyStmt')
		Snowflake.commit_transaction( trans	= snow_conn )

	#S3StreamLoader.delete_files ( file_names=s3_file_names)
	#Email.send_email			( **email_args )




