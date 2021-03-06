from sac_acaptcha import ACaptcha
from third_lib.recaptcha.client import captcha

class SACReCaptcha(ACaptcha):
	"""This the implementation of ReCaptcha API, as they provide a third library we implement it by following the displayhtml and the submit methods"""
	sac_type = 'SACReCaptcha'

	def __init__(self):
		super(SACReCaptcha, self).__init__()
		self.recaptcha = captcha
		self.publicKey = '6LdUQPgSAAAAAOoru8VhGXMPFub5DsJZJxVt2P3q'
		self.privateKey = '6LdUQPgSAAAAAIcSPVWI9_L_VpIuI6-frgOX7fwR'
	
	def generate(self):
		self.is_valid = False
		self.html = self.recaptcha.displayhtml(self.publicKey)+'<input type="hidden" name="sac_num" value="'+self.num+'"/>'

	def submit(self, params):
		response = self.recaptcha.submit(params['recaptcha_challenge_field'], params['recaptcha_response_field'], self.privateKey, params['remote_addr'])
		self.is_valid = response.is_valid
		
