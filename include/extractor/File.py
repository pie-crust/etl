
(cli, conn_pool)=app_init
import os, sys, csv, time, math, glob
import pyodbc
import subprocess
import multiprocessing
import collections
from collections import OrderedDict
from pprint import pprint as pp
e=sys.exit
import logging
log=logging.getLogger('cli')

import requests, json
try:
	import __builtin__ as builtins
except:
	import builtins

from include.extractor.common.Extractor import Extractor

from include.utils import  ctimeit, api
from include.fmt import  pfmtd




class File(Extractor):
	def __init__(self, **kwargs):
		Extractor.__init__(self)
		self.cli 		= cli = kwargs.get('cli', None)
		self.file_name  = kwargs.get('file_name', None)
		self.scfg 		= kwargs.get('scfg', None)
		self.parse 		= kwargs.get('parse', True)
		self.cln=cln	= self.__class__.__name__
		self.cols=self.cols_alt=None

		if self.parse:
			self.set_header_cols()

	def get_value(self, coords,  skip=0):
		x, y = coords
		assert x>=0
		assert y>=0
		assert skip>=0
		colsep= self.scfg['columnDelimiter']
		with open(self.file_name, 'rb') as fh:
			line=None
			for i in range(skip+y+1):
				line = fh.readline()
			assert line 
			return line.strip().split(colsep.encode())[x].decode()

	def get_columns(self,cols,  skip=0):
		assert cols
		assert skip>=0
		colsep= self.scfg['columnDelimiter']
		with open(self.file_name, 'rb') as fh:
			for i in range(skip):
				_ = fh.readline()
			line= fh.readline().strip()
			while line:
				#pp(line)
				row= line.split(colsep.encode())
				
				out = [row[i] for i in cols]
				yield colsep.encode().join(out)+colsep.encode()
				line= fh.readline().strip()
	def delete(self):
		assert os.path.isfile (self.file_name)
		os.unlink (self.file_name)
		assert not os.path.isfile (self.file_name)

		
	def line_count(self, fn=None):
		if not fn : fn= self.file_name
		assert os.path.isfile(fn)
		p = subprocess.Popen(['wc', '-l', fn], stdout=subprocess.PIPE, 
												stderr=subprocess.PIPE)
		result, err = p.communicate()
		if p.returncode != 0:
			raise IOError(err)
		return int(result.strip().split()[0])
		
	def set_header_cols(self):
		
		assert os.path.isfile(self.file_name)
		cols=None
		with open(self.file_name, 'rb') as fh:
			colsep= self.scfg['columnDelimiter'].encode()
			assert colsep
			hsize= int(self.scfg['writeHeader'])
			if hsize in [2]:
				line=fh.readline()
				try:
					header= line.strip().strip(colsep)
				except Exception as ex:
					print (line)
					raise
				
				cnames=[col for col in header.split(colsep)]
				assert len(cnames)
				
				if 1:
					header2= fh.readline().strip().strip(colsep)
				
					ctypes=[col for col in header2.strip().split(colsep)]
					assert len(ctypes)
				cols = [(nm.decode(), ctypes[i].decode()) for i, nm in enumerate(cnames)]
			elif hsize in [1]:
				line=fh.readline()
				try:
					header= line.strip().strip(colsep)
				except Exception as ex:
					print (line)
					raise
				
				cnames=[col for col in header.split(colsep)]
				assert len(cnames)

				cols = cnames
				
			else:
				raise Exception('Wrong header size: [%d]' % hsize)
		assert cols
		self.cols=cols
	def set_alt_cols(self):

		if self.cli.scfg:
			acols= self.cli.get_alt_cols(self.cli.scfg)
			self.cols_alt=[acols.get(x.decode(),x.decode()) for x in  self.cols]
		else:
			self.cols_alt= self.cols
		
	def get_header_cols(self):
		self.set_header_cols()
		assert self.cols
		return self.cols
	def describe(self):
		pfmtd([dict(Column=x) for x in self.get_header()], 'File header: %s' % self.file_name)
	@api
	@ctimeit
	def get_header(self, fn=None, scfg=None):
		if not fn: fn = self.file_name
		if not scfg: scfg=self.scfg
		assert os.path.isfile(fn)
		with open(fn, 'rb') as fh:
			colsep= scfg['columnDelimiter']
			assert colsep
			hsize= int(scfg['writeHeader'])
			if hsize in [2]:
				
				header= fh.readline().strip()
				
				cnames=[col for col in header.strip().split(colsep)][:-1]
				assert len(cnames)
				
				if 1:
					header2= fh.readline().strip()
				
					ctypes=[col for col in header2.strip().split(colsep)][:-1]
					assert len(ctypes)
				return [(nm, ctypes[i]) for i, nm in enumerate(cnames)]
			elif hsize in [1]:
				
				header= fh.readline().strip()
				
				cnames=[col for col in header.strip().split(colsep.encode())][:-1]
				assert len(cnames)
				

				return cnames
			else:
				raise Exception('Wrong header size: [%d]' % hsize)
			return cols

