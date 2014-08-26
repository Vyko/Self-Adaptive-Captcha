import os
import sqlite3 as sqlite

class SACDatabase(object):
	def __init__(self):
		super(SACDatabase, self).__init__()
		self.dbPath = os.getcwd()+'/api/database/sac.db'
	def saveCaptcha(self, captcha):
		if (captcha.sac_type == 'SACTextCaptcha'):
			self.saveTextCaptcha(captcha)
		else:
			self.saveGenericCaptcha(captcha)

	def saveTextCaptcha(self, captcha):
		con = sqlite.connect(self.dbPath)
		with con:
			cur = con.cursor()
			for asw in captcha.answers:
				cur.execute("INSERT INTO captchas VALUES (NULL,'"+captcha.sac_type+"', '"+captcha.num+"', '"+asw+"')")
		con.commit()
		con.close()
		
	def saveGenericCaptcha(self, captcha):
		con = sqlite.connect(self.dbPath)
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO captchas VALUES (NULL,'"+captcha.sac_type+"', '"+captcha.num+"', '')")
		con.commit()
		con.close()

	def getCaptchaRowsByNum(self, num):
		con = sqlite.connect(self.dbPath)
		with con:
			con.row_factory = sqlite.Row
			cur = con.cursor()
			cur.execute("SELECT * FROM captchas WHERE num = '"+num+"'")
			rows = cur.fetchall()
		con.close()
		if (len(rows) == 0):
			return None
		return rows
        
