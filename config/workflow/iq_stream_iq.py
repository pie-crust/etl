from include.utils import create_reader, create_writer, create_actor, InOut

cli, conn_pool=app_init


IQ 				= create_reader('IQ',  	app_init=app_init )
IQ_Writer		= create_writer('IQ', 	app_init=app_init )
Email 	  		= create_actor ('Email',app_init=app_init )


IQ_cursor		= InOut()
s3_file_names	= InOut()
snow_conn		= InOut()

##
##
email_args={'email_subject':'IQ.procedure->IQ'}
##
##

def run():	
	IQ.set_loader(IQ_Writer)
	IQ.open_stream				( dbcfg = cli.scfg, qname = 'sourceStmt', out=IQ_cursor )
	
	IQ_Writer.begin_transaction ( out = snow_conn )
	IQ_Writer.purge_data		( trans	= snow_conn, stmt = 'purgeStmt' )
	IQ_Writer.bulk_copy			( trans	= snow_conn, file_names = s3_file_names, target=cli.tcfg, qname = 'copyStmt', )
	IQ_Writer.commit_transaction( trans	= snow_conn )
	IQ_Writer.delete_files ( file_names=s3_file_names)
	if 0:
		Email.send_email			( **email_args )
		cli.done					()




