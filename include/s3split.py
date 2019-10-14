class Value(object):

	def __init__(self, file_object_cache, content=None, filename=None, md5=None, offset=0, path=None, size=100, bucket_name=None):
		self.file_object_cache = file_object_cache
		self.content = content
		self.filename = filename
		self.md5 = md5
		self.offset = offset
		self.path = path
		self.size = size
		self.bucket_name = bucket_name

	def get_content(self):
		if self.content is None:
			if self.filename:
				with self.file_object_cache.open(self.filename) as file_object:
					file_object.seek(self.offset)
					self.content = file_object.read(self.size)
			elif self.path:
				with open(self.path) as file_object:
					self.content = file_object.read()
			else:
				assert False
		return self.content

	def calculate_md5(self):
		if self.md5 is None:
			self.md5 = compute_md5(StringIO(self.get_content()))
		return self.md5

	def get_size(self):
		if self.size is None:
			if self.content:
				self.size = len(self.content)
			elif self.path:
				self.size = os.stat(self.path).st_size
			else:
				assert False
		return self.size

	def should_copy_content(self):
		return self.bucket_name is None