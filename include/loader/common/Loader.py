class Loader():
	def __init__(self):
		self.objtype='Loader'
	def get_creds(self):
		if 0:
			aws_ak, aws_sak=self.cli.aws_keys
		else:
			aws_ak, aws_sak=self.cli.get_aws_keys()
		return aws_ak, aws_sak
