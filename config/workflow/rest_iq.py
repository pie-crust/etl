cli, conn_pool=app_init
import sys
from collections import OrderedDict
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
from include.fmt import ppe
e=sys.exit


	


Email 		= create_actor (aname ='Email',app_init=app_init )


insert_stats= InOut(inserted_cnt=-1)
read_stats= InOut(total_read=-1)

email_args={'email_subject':'IQ->REST->IQ'}




from_conn  = InOut()
trans_ids = InOut()
rest_pipe = InOut()


to_conn	= InOut()


def run():
	lite_tbl={}
	stats={}
	

	if 1: #REST
		for _rest, val in cli.cfg['rest'].items():
			cli.set_source(_rest)
			cli.set_rest(_rest)
			_rest_class = list(val.keys())[0]
			
			cli.rcfg= rcfg=cli.get_rcfg(_rest_class)
		pp(cli.rcfg)
		REST = create_reader(aname =_rest_class, app_init=app_init )
		#REST.read_stream	 		( pipe  = from_conn, skip_header = 0, 	out=trans_ids)

			
		
	#e()
	if 1: #//Load data
		for _trg_class, val in cli.cfg['target'][_rest].items() or []:

			cli.tcfg= tcfg =  cli.get_tcfg(_trg_class)

				

			_todbname=tcfg["targetDb"]

			toDB 	= create_writer (aname =_trg_class,	app_init=app_init )
			
			toDB.begin_transaction  ( env =tcfg['targetDb'] , out 	= to_conn )
			if 1: #//reset date in case of AccountingDate=="auto"
				cli.set_default_acct_date(toDB, tcfg)
				acct_date=cli.get_parsed(ckey='accountingDate', cfg=tcfg)

			if 1: #//set acct_year, acct_mon for new target table naming
				fmt = cli.get_parsed(ckey='accountingDateFmt', cfg=tcfg) 
				cli.set_target_table(tcfg=tcfg, acct_date=acct_date, fmt = fmt)
				
			#//count existing recs
			if 1:
				if 1:
					stmt = cli.get_parsed(ckey='preCountTablePartitionStmt', cfg=tcfg)
					cur = toDB.exec_query(stmt)
					pre_part_cnt= cur.fetchall()[0][0]
				if 1:
					stmt = cli.get_parsed(ckey='preCountTableStmt', cfg=tcfg)
					cur = toDB.exec_query(stmt)
					pre_tab_cnt= cur.fetchall()[0][0]
				assert pre_part_cnt == pre_tab_cnt, 'Extra records in table other than" %s" for AccountingDate "%s".' % (_todbname, acct_date)
				
			table='%s.%s' % (tcfg['targetSchema'], tcfg['targetTable'])
			toDB.desc_table(schema=tcfg['targetSchema'], tbl=tcfg['targetTable'], col_ord=False)
			
			if 1: 
				cli.rest_acct_date= acct_date.replace('/','')
				REST.read_json_data ( cfg= cli.rcfg, skip_header = 0, out = rest_pipe, read_stats=read_stats)
			xref=cli.tcfg["columnMap"]
			cols = toDB.get_table_cols(schema = cli.get_parsed(ckey='targetSchema', cfg=tcfg), tab=cli.get_parsed(ckey='targetTable', cfg=tcfg))
			#ppe(set(cols) - set([x[0] for x in xref.values()]))
			pp(set([x[0] for x in xref.values()]))
			pp(set(cols))
			assert not (set([x[0] for x in xref.values()]) - set(cols)), 'There are columns in config, but not in target table: %s' % (set([x[0] for x in xref.values()]) - set(cols))
			assert not (set(cols) - set([x[0] for x in xref.values()])), 'There are columns in target table, but not in config: %s' % (set([x[0] for x in xref.values()]) - set(cols))
			
			
			toDB.insert_RC_data ( trans	= to_conn, target = cli.tcfg, source = rest_pipe, stmt = 'insertStmt' , insert_stats=insert_stats)
			
			if 1:
				stmt = cli.get_parsed(ckey='afterCountStmt', cfg=tcfg)
				cur = toDB.exec_query(stmt)
				after_cnt= cur.fetchall()[0][0]

			stats['%s->%s' % (_rest, _todbname)] =st=  OrderedDict()
			st['source_cnt']		= len(toDB.rows) 
			st['total_extracted'] 	= read_stats.total_read
			st['total_inserted'] 	= insert_stats.inserted_cnt
			st['after_count'] 		= after_cnt
			st['rollback']			= cli.get_parsed(ckey='rollbackStmt', cfg=tcfg)
			st['purge']				= cli.get_parsed(ckey='purgeStmt', cfg=tcfg)
			
			

			try:
				
				assert v['source_cnt'] == v['total_extracted'], "source_cnt %s <> total_extracted %s" 	% ( v['source_cnt'], v['total_extracted'])
				assert v['source_cnt'] == v['total_inserted'],  "source_cnt %s <> total_inserted %s" 	% ( v['source_cnt'], v['total_inserted'])
				assert v['source_cnt'] == v['after_count'] , 	"source_cnt %s <> after_count %s" 		% ( v['source_cnt'], v['after_count'])
			except Exception as ex:
				del_cnt = toDB.exec_dml( dml=st['rollback'], trans=to_conn, commit=True) 
				log.info('Rolled back recs: %d' % del_cnt)
				raise 
				
			if 1: #//purge
				purge_cnt = toDB.exec_dml( dml=st['purge'], trans=to_conn, commit=True) 
				log.info('Purged old recs: %d' % purge_cnt)
			toDB.commit_transaction( trans	= to_conn )
		
	if 0:
		email_args.update(dict(cli_stats=stats))
		Email.send_email( **email_args)


		
		




