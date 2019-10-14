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