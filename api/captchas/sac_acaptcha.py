import imp

class ACaptcha(object):
	def __init__(self):
		super(ACaptcha, self).__init__()
		self.is_valid = False
		self.num = ''
		self.html = ''

	def submit(self, params):
		  raise NotImplementedError("Submit method not implemented")
		
	def generate(self):
		  raise NotImplementedError("Submit method not implemented")
