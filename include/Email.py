(cli, conn_pool)=app_init
import os, sys, time, re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from operator import itemgetter
from subprocess import Popen, PIPE
from pprint import pprint as pp
from include.utils import get_emails
from collections import OrderedDict
from email.mime.application import MIMEApplication
from os.path import basename
from email.utils import COMMASPACE, formatdate

SENDMAIL	= "/usr/lib/sendmail", "-t", "-oi"

e=sys.exit

from include.utils import ctimeit

class Email(object):
	#@csource
	def __init__(self, **kwargs):
		self.cli =cli= kwargs.get('cli', None)
		assert cli
		self.sender, self.to = get_emails(env=cli.rte)
		self.subject    = None
		self.body       = None
		self.html_body   = None
		self.headers    = {}
		self.attachments = []
		self.sendmail=SENDMAIL
	@ctimeit
	def send_email(self,  **kwargs):
		self.email_init(**kwargs)
		
		msg = MIMEMultipart('alternative')
		msg['Subject'] = self.subject
		msg['From'] = self.sender
		msg['To'] 	= self.to

		html = self.html_body

		part1 = MIMEText(html, 'html')

		msg.attach(part1)
		p = Popen(self.sendmail, stdin=PIPE)
		if 1:
			if sys.version_info[0] >= 3:
				p.communicate(msg.as_string().encode())
			else:
				p.communicate(msg.as_string())
			stdout, stderr = p.communicate()
			if stdout: log.info('Sendmail: %s', stdout)
			if stderr: log.error('Sendmail: %s', stderr)
		log.info('Email sent.')
	def send_email_att(self,  **kwargs):
		self.email_init_att(**kwargs)
		
		msg = MIMEMultipart('alternative')
		msg['Subject'] = self.subject
		msg['From'] = self.sender
		msg['Date'] = formatdate(localtime=True)
		msg['To'] 	= self.to

		html = self.html_body

		part1 = MIMEText(html, 'html')

		msg.attach(part1)
		#pp(self.att_files )
		for f in self.att_files or []:
			#print 345, f
			
			#e()
			with open(f, "rb") as fil:
				part = MIMEApplication(
					fil.read(),
					Name=basename(f)
				)
			# After the file is closed
			part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
			msg.attach(part)

		
		p = Popen(self.sendmail, stdin=PIPE)
		if 1:
			if sys.version_info[0] >= 3:
				p.communicate(msg.as_string().encode())
			else:
				p.communicate(msg.as_string())
			stdout, stderr = p.communicate()
			if stdout: log.info('Sendmail: %s', stdout)
			if stderr: log.error('Sendmail: %s', stderr)
		log.info('Email sent.')
		
	def email_init(self, **kwargs):
		cli=self.cli

		if 1:
			sec=round((time.time() - cli.start_time),2)
			lll=open(log.file_name, 'r').read().split(os.linesep)

			ll= [x.split('|')[6].strip() for x in lll if x and '|INFO|' in x]
			lll=[x for x in ll if not x.strip().startswith('Entering') and not x.strip().startswith('Exiting')]
			#pp(ll)
		html_body, log_stats = cli.get_log_stats(lll, kwargs.get('cli_stats', None))
		
		if self.cli.rte in ['DEV']:
			if 1:
				html_body = '<br>'.join(lll) +'<br><br>'+'<br>'.join(['<pre>%s</pre>' % s for s in  log_stats.values()])


		if 1:

			subj= kwargs.get('email_subject')
			assert subj, 'Email subject is missing. Set it in *.py flow.'
			self.subject="[%s] %s [%s] [%s]" % (cli.rte,subj, cli.proc_key,','.join(cli.pa))
			self.html_body= html_body
	def email_init_att(self, **kwargs):
		cli=self.cli

		if 1:
			sec=round((time.time() - cli.start_time),2)
			lll=open(log.file_name, 'r').read().split(os.linesep)

			ll= [x.split('|')[6].strip() for x in lll if x and '|INFO|' in x]
			lll=[x for x in ll if not x.strip().startswith('Entering') and not x.strip().startswith('Exiting')]
			#pp(ll)
		html_body, log_stats, self.att_files = cli.get_log_stats(lll)
		
		if self.cli.rte in ['DEV']:
			if 1:
				html_body = '<br>'.join(lll) +'<br><br>'+'<br>'.join(['<pre>%s</pre>' % s for s in  log_stats.values()])


		if 1:

			subj= kwargs.get('email_subject')
			assert subj, 'Email subject is missing. Set it in *.py flow.'
			self.subject="[%s] %s [%s] [%s]" % (cli.rte,subj, cli.proc_key,','.join(cli.pa))
			self.html_body= html_body			
