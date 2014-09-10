import time
from database.sac_database import SACDatabase
from captchas.sac_recaptcha import SACReCaptcha
from captchas.sac_textcaptcha import SACTextCaptcha
from captchas.sac_asirra import SACAsirra

class CaptchaManager(object):
	
	captchas = {
		'SACReCaptcha' : SACReCaptcha,
		'SACTextCaptcha' : SACTextCaptcha,
		'SACAsirra' : SACAsirra
		}

	def __init__(self):
		super(CaptchaManager, self).__init__()
		self.db = SACDatabase()
		self.currentCaptcha = None

	def getAllCaptchas(self):
		return CaptchaManager.captchas

	def instanceCurrentCaptcha(self, captchaType):
		self.currentCaptcha = CaptchaManager.captchas[captchaType]()
		self.currentCaptcha.num = repr(time.time())

	def generateCaptcha(self):
		self.currentCaptcha.generate()
		self.db.saveCaptcha(self.currentCaptcha)
		return self.currentCaptcha

	def setCaptchaByNum(self, captchaNum):
		rows = self.db.getCaptchaRowsByNum(captchaNum)
		self.currentCaptcha = CaptchaManager.captchas[rows[0]['type']]()
		self.currentCaptcha.num = rows[0]['num']

		if (self.currentCaptcha.sac_type == 'SACTextCaptcha'):
			for row in rows:
				self.currentCaptcha.addAnswer(row['answer'])


	def checkCaptcha(self, form):
		self.currentCaptcha.submit(form)
