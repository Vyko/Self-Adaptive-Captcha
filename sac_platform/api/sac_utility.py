class Utility(object):
    """This class decides the most suitable CAPTCHA according to the currrent environment by calculating the best utility of each Captcha"""

    def __init__(self):
        self.mediasUtils = {
            'bank':{'security':10, 'accessibility':4, 'mobile':0, 'ease':0},
            'email':{'security':8, 'accessibility':5, 'mobile':4, 'ease':3},
            'blog':{'security':4, 'accessibility':8, 'mobile':6, 'ease':6},
            'chat':{'security':0, 'accessibility':8, 'mobile':8, 'ease':10}
            }
        self.captchasUtils = {
            'SACReCaptcha' : { 'security':10,'accessibility':3, 'mobile':5, 'ease':3},
            'SACTextCaptcha' : {'security':7,'accessibility':7, 'mobile':7, 'ease':5},
            'SACAsirra' : {'security':9,'accessibility':5, 'mobile':3, 'ease':6}
            }

    def getBestUtility(self, envManager):
        mediaUtils = self.mediasUtils.get(envManager.media, self.mediasUtils.get('blog'))
        bestUtil = None
        
        for (captchaType, captchaUtil) in self.captchasUtils.items():
            util = mediaUtils['security'] * captchaUtil['security'] + \
                mediaUtils['accessibility'] * captchaUtil['accessibility'] + \
                mediaUtils['ease'] * captchaUtil['ease']
            if (envManager.isMobile):
                util += mediaUtils['mobile'] * captchaUtil['mobile']

            if (bestUtil == None or bestUtil['util'] <= util):
                bestUtil = {'type':captchaType,'util': util}
        return bestUtil

