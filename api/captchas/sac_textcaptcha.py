import xml.sax.handler
import md5
from sac_acaptcha import ACaptcha

class TextCaptchaXMLHandler(xml.sax.handler.ContentHandler):
    def __init__(self, sacTextCaptcha):
        self.sacTC = sacTextCaptcha

    def startElement(self, name, attributes):
        self.buffer = ''
 
    def characters(self, data):
        self.buffer += data
  
    def endElement(self, name):
        if name == "question":
            self.sacTC.setQuestion(self.buffer)
        elif name == 'answer':
            self.sacTC.addAnswer(self.buffer)


class SACTextCaptcha(ACaptcha):
    """This is the implementation of the TextCaptcha API"""

    sac_type = 'SACTextCaptcha'

    def __init__(self):
        super(SACTextCaptcha, self).__init__()
        self.privateKey = '74sauxmyk944k4gwkwkk8kkk85giku1v'
        self.question = ''
        self.answers = []
                
    def fetchCaptcha(self):
        """This method instantiate an XMLParser to retrieve the question its list of answers"""
         parser = xml.sax.make_parser()
         handler = TextCaptchaXMLHandler(self)
         parser.setContentHandler(handler)
         parser.parse('http://api.textcaptcha.com/'+self.privateKey)

    def generate(self):
        self.is_valid = False
        self.fetchCaptcha()
        self.html = '<label for="sac">'+self.question+'</label><input id="sac" name="sac_field" value="" />'
        self.html += '<input type="hidden" name="sac_num" value="'+self.num+'"/>'

    def submit(self, params):
        """To verify user answers, we compare the md5sum of the clear lowercase answer to ones saved in database"""
        for answer in self.answers:
            if (answer == md5.new((params['answer'].lower().strip())).hexdigest()):
                self.is_valid = True
                break

    def setQuestion(self, q):
        self.question = q

    def addAnswer(self, a):
        self.answers.append(a)
