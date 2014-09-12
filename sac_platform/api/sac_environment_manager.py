class EnvironmentManager(object):
	"""This class is a data class where all the data related to the system environment are stocked"""

	def __init__(self, params):
		super(EnvironmentManager, self).__init__()
		
		self.media = params.get('media','blog')
		self.isMobile = params.get('is_mobile', '')
		if (self.isMobile == ''):
			self.isMobile = False
		self.userIP = params.get('ip_address', '')
		self.lang = params.get('lang', '')
