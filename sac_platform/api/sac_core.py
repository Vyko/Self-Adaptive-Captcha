from sac_utility import Utility
from sac_captcha_manager import CaptchaManager
from sac_environment_manager import EnvironmentManager

class Core(object):
	"""This class is the main link between the different feedback loop parts."""

	def __init__(self):
		super(Core, self).__init__()
		self.envManager = None
		self.utility = None
		self.cm = CaptchaManager()

	def generateCaptcha(self, form):
		self.collectEnvironment(form)
		self.utility = Utility()
		captchaType = self.getBestUtility()
		captcha = self.getCaptcha(captchaType)

		return {'html' : captcha.html, \
			'form_attr':captcha.form_attr}

	def collectEnvironment(self, form):
		"""This method instantiate an environmentManager where all the data from the environment system will be collected"""
		self.envManager = EnvironmentManager(form)

	def getBestUtility(self):
		"""This method retreives the type of the CAPTCHA having the best utility according to the Utility class"""
		bestUtil = self.utility.getBestUtility(self.envManager)
		return bestUtil['type']

	def getCaptcha(self, captchaType):
	    	"""This method generate the chossen CAPTCHA through the CaptchaManager"""
		self.cm.instanceCurrentCaptcha(captchaType)
		return self.cm.generateCaptcha()


	def getCaptchaType(self, num):
		self.cm.setCaptchaByNum(num)
		return {'type':self.cm.currentCaptcha.sac_type}

	def verifyCaptcha(self, form, num):
		"""This method check the CAPTCHA answer and return if it valid or not. If not the response is composed of an html and form_attr attributes which contain new code for a new CAPTCHA"""
		self.cm.setCaptchaByNum(num)
		self.cm.checkCaptcha(form)
		if (self.cm.currentCaptcha.is_valid == False):
			self.cm.instanceCurrentCaptcha(self.cm.currentCaptcha.sac_type)
			self.cm.generateCaptcha()
		return {'success':self.cm.currentCaptcha.is_valid, 'html':self.cm.currentCaptcha.html, 'form_attr':self.cm.currentCaptcha.form_attr}
