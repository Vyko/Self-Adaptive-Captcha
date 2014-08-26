from sac_captcha_manager import CaptchaManager
from sac_environment import Environment

class Controller(object):
	"""docstring for Controller"""

	def __init__(self):
		super(Controller, self).__init__()
		self.env = None
		self.cm = CaptchaManager()

	def generateCaptcha(self, form):
		utilities = []

		self.env = Environment(form.get('media', 'blog'))
		captchas = self.cm.getAllCaptchas()
		
		for (captchaType, captcha) in captchas.items():
			utilities.append({'type': captchaType, 'util' : self.env.getUtility(captcha)})

		captchaType = self.selectCaptchaTypeBestUtil(utilities)
		self.cm.instanceCurrentCaptcha(captchaType)
		self.cm.generateCaptcha()
		return {'type' : self.cm.currentCaptcha.sac_type, 'html' : self.cm.currentCaptcha.html}

	def selectCaptchaTypeBestUtil(self, utilities):
		best = None
		for item in utilities:
			if (best == None or best['util'] <= item['util']):
				best = item
		return best['type']

	def getCaptchaType(self, num):
		self.cm.setCaptchaByNum(num)
		return {'type':self.cm.currentCaptcha.sac_type}

	def verifyCaptcha(self, form, num):
		self.cm.setCaptchaByNum(num)
		self.cm.checkCaptcha(form)
		if (self.cm.currentCaptcha.is_valid == False):
			self.cm.instanceCurrentCaptcha(self.cm.currentCaptcha.sac_type)
			self.cm.generateCaptcha()
		return {'success':self.cm.currentCaptcha.is_valid, 'html':self.cm.currentCaptcha.html}
