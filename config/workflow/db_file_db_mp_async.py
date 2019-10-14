"""
"""

import sys
from collections import OrderedDict
from multiprocessing import Process, Value, Lock
import multiprocessing
from pprint import pprint as pp
from include.utils import create_reader, create_writer, create_actor, InOut
e=sys.exit
cli, conn_pool=app_init


Email 		= create_actor ('Email',app_init=app_init )

Dir 	= create_reader('Dir', 		app_init=app_init ) 

file_stats= InOut(dump_files=[], ins_stats={})



data_files	= InOut()
data_files.file_names=[]
#uploaded_files.file_names=[]

email_args={'email_subject':'DB->file'}

class Counter(object):
	def __init__(self, initval=0):
		self.val = Value('i', initval)
		self.cnt = Value('i', initval)
		self.lock = Lock()

	def increment(self):
		with self.lock:
			self.val.value += 1
			self.cnt.value += 1
		return self.val.value
	def decrement(self):
		with self.lock:
			self.cnt.value -= 1
	def running(self):
		with self.lock:
			return self.cnt.value
	def value(self):
		with self.lock:
			return self.val.value
			
counter = Counter(0)


def producer (cli, _source):
	val		= cli.cfg['source'][_source]
	_dbname = val["sourceDb"]
	DB  	= create_reader(_dbname,	app_init=app_init )
	cnt		= cli.get_src_row_count(DB)

	if not cli.lame_duck:
		assert cli.dop>0
		cli.src_chunk_size= round(cnt/cli.dop) +1
	else:
		cli.src_chunk_size=cli.lame_duck
		
	FileWriter 	= create_writer('File',	app_init=app_init ) 
	data_files.file_names=[]
	#uploaded_files.file_names=[]
	#ext_files=[]
	if 1:
		cli.set_source(_source)
		DB.set_loader(FileWriter)
		
		total_read= 0
		
		scfg= cli.get_scfg()
		source_chunk_size= int(float(cli.get_parsed(ckey='sourceChunkSize', cfg=scfg)))
		
		cid=0

		skew_pct= int(float(cli.get_parsed(ckey='fileSkewPct', cfg=scfg)))
		log.debug('Skew percentile = %s' % skew_pct)
		if skew_pct and cli.dop>=2:
			delta=source_chunk_size*(skew_pct/100.0)
			num_of_files=cli.dop
			increment= int(delta/num_of_files)
			chunk_map={}
			accum_skew = sum([increment*(num_of_files-i) for i in range(num_of_files)])
			for i in range(num_of_files):
				
				skew=((cnt-accum_skew)/num_of_files)+increment*(num_of_files-i) 
				chunk_map[i]=skew+1  if not cli.lame_duck else cli.lame_duck
			pp(chunk_map)
			#e()
			if not cli.lame_duck:
				assert sum(chunk_map.values())>=cnt, 'Chunk map has to cover all source records [%s <> %s]' % (sum(chunk_map.values()),cnt)
			#dfiles=[]
			for iq_data in DB.fetch_many_async ( chunk_map=chunk_map, counter=counter,  source = scfg, qname = 'sourceStmt', out=InOut(), skip_header=0 ):
				dump_file = InOut(source_cnt=cnt)
				FileWriter.open_file(id=cid, out = dump_file )
				if 1: #not total_ins:
					dump_cfg=cli.get_dcfg()
					FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg = dump_cfg)
				FileWriter.append_data ( file = dump_file,  data = iq_data, cfg = dump_cfg)
				total_read+=len(iq_data.data)
				FileWriter.close_file(file = dump_file)
				#ext_files.append(dump_file.fpath)
			
				#dfiles.append(dump_file)
				dump_file.extracted_cnt=total_read

				yield dump_file
				cid +=1

		else: #lame duck
			print source_chunk_size
			#e()
			assert source_chunk_size
			for iq_data in DB.fetch_many ( chunk_size=source_chunk_size,   source = scfg, qname = 'sourceStmt', out=InOut(), skip_header=0 ):
				dump_file = InOut(source_cnt=cnt)
				FileWriter.open_file(id=cid, out = dump_file )
				if 1: #not total_ins:
					dump_cfg=cli.get_dcfg()
					FileWriter.create_header(file = dump_file, header = DB.get_header(), cfg = dump_cfg)
				FileWriter.append_data ( file = dump_file,  data = iq_data, cfg = dump_cfg)
				total_read+=len(iq_data.data)
				FileWriter.close_file(file = dump_file)
				#ext_files.append(dump_file.fpath)
				log.debug('File %d created:file: %d,  %d records' % (cid, len(iq_data.data), source_chunk_size))
				cid +=1
				dump_file.extracted_cnt=total_read
				yield dump_file
			
		log.debug('Done extracting.....')

insert_stats= InOut(source_cnt=-1, inserted_cnt=-1)
manager = multiprocessing.Manager()
return_dict = manager.dict()
def run():
	stats={}

				
	for _source, val in cli.cfg['source'].items():
		val		= cli.cfg['source'][_source]
		_dbname = val["sourceDb"]
		DB  	= create_reader(_dbname,	app_init=app_init )
		
		if 1: #Load to DB
			cli.set_source(_source)
			file_scfg = cli.cfg['dump'][_source]
	
		if 1:
			to_conn	= InOut()
			#file_stats.ins_stats[_dbname]=ins={}
			
			for _target, val in cli.cfg['target'][_source].items() or []:
				tcfg =  cli.cfg['target'][_source][_target]
				_todbname=val["targetDb"]

				toDB 	= create_writer(_target,	app_init=app_init )
				rec_delim='\n'
				skip_header=0
				#ins[_todbname]=manager.dict()
				toDB.insert_files (producer=(producer,(  cli,_source)), out = file_stats, skip_header=skip_header, rec_delim=rec_delim, cfg= (file_scfg, tcfg), return_dict=return_dict)

		pp(file_stats.dump_files)
		extracted_cnt=0
		for fobj in file_stats.dump_files:
			extracted_cnt += fobj.extracted_cnt
			print toDB.counter.value()
		pp(return_dict.values())
		stats['%s->%s' % (_dbname, _todbname)] =st=  OrderedDict()
		st['source_cnt']		= insert_stats.source_cnt if not cli.lame_duck else cli.lame_duck
		st['total_extracted'] 	= extracted_cnt
		st['total_inserted'] 	= toDB.total_ins
	pp(stats)
	for k, v in stats.items():
		assert v['source_cnt'] == v['total_extracted']
		assert v['source_cnt'] == v['total_inserted']
		
		
	if 1:
		email_args.update(dict(cli_stats=stats))
		Email.send_email( **email_args )




