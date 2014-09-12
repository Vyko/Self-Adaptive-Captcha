import xml.sax.handler
from sac_acaptcha import ACaptcha

class AsirraXMLHandler(xml.sax.handler.ContentHandler):
    def __init__(self, sacAsirra):
        self.sacAsirra = sacAsirra

    def startElement(self, name, attributes):
        self.buffer = ''
 
    def characters(self, data):
        self.buffer += data
  
    def endElement(self, name):
        if name == "Result":
            self.sacAsirra.result = self.buffer
        
class SACAsirra(ACaptcha):
    """This is the implementation of the ASIRRA API through an XML Parser"""
    sac_type = 'SACAsirra'

    def __init__(self):
        super(SACAsirra, self).__init__()
        self.result = ''
                                
    def generate(self):
        self.is_valid = False
        self.html = '<script type="text/javascript" src="http://challenge.asirra.com/js/AsirraClientSide.js"></script>'
        self.html += '<input type="hidden" name="sac_num" value="'+self.num+'"/>'
        self.html += self.getSubmitForm()
        self.form_attr = 'id="SACForm" onsubmit="return SACAsirraSubmitForm();"'

    def submit(self, params):
        parser = xml.sax.make_parser()
        handler = AsirraXMLHandler(self)
        parser.setContentHandler(handler)
        parser.parse('http://challenge.asirra.com/cgi/Asirra?action=ValidateTicket&ticket='+params['asirra_ticket'])
        if (self.result == 'Pass'):
            self.is_valid = True

    def getSubmitForm(self):
        return '<script type="text/javascript"> var passThroughFormSubmit = false;function SACAsirraSubmitForm(){if (passThroughFormSubmit) {return true;}Asirra_CheckIfHuman(HumanCheckComplete);return false;}'+ \
            'function HumanCheckComplete(isHuman){if (!isHuman){alert("Please correctly identify the cats.");}else{passThroughFormSubmit = true;formElt = document.getElementById("SACForm");formElt.submit();}}</script>'
