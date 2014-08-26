class Environment(object):
	"""docstring for Environment"""
	
	mediasUtils = {
				'bank':{'security':10, 'accessibility':4, 'mobile':0, 'ease':0},
				'email':{'security':8, 'accessibility':5, 'mobile':4, 'ease':3},
				'blog':{'security':4, 'accessibility':8, 'mobile':6, 'ease':6},
				'chat':{'security':0, 'accessibility':8, 'mobile':8, 'ease':10}
				}

	def __init__(self, media, is_mobile = False, ip_address = ""):
		super(Environment, self).__init__()
		self.media = media
		self.isMobile = is_mobile
		self.userIP = ip_address

		if (Environment.mediasUtils.get(self.media, None) == None):
			self.media = 'blog'

	def getUtility(self, captcha):
		mediaUtils = Environment.mediasUtils[self.media]

		util = mediaUtils['security'] * captcha.utils['security'] + \
			mediaUtils['accessibility'] * captcha.utils['accessibility'] + \
			mediaUtils['ease'] * captcha.utils['ease']

		if (self.isMobile):
			util += mediaUtils['mobile'] * captcha.utils['mobile']
		return util