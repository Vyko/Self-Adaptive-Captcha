import imp

class ACaptcha(object):
	"""This class is an Abstract class of all CAPCTHAs to ensure that all CAPTCHA objects have submit and generate methods"""
	def __init__(self):
		super(ACaptcha, self).__init__()
		self.is_valid = False
		self.num = ''
		self.html = ''
		self.form_attr = ''

	def submit(self, params):
		  raise NotImplementedError("Submit method not implemented")
		
	def generate(self):
		  raise NotImplementedError("Submit method not implemented")
