import smtplib
from email.mime.text import MIMEText
class zhsendmail():
    'This is ZhaoHao\'s Frist model'
    def __init__(self, subject, neirong):
        self.smtp = smtplib.SMTP('smtp.163.com')
        self.smtp.login('happytortoise@163.com', 'xiao99')
        self.subject = subject
        self.neirong = neirong
        self.msg = MIMEText(self.neirong)
        self.msg["Subject"] = self.subject
    def send(self):
        try:
            self.smtp.sendmail("happytortoise@163.com", "happytortoise@163.com", self.msg.as_string())
        finally:
            self.smtp.close()
if __name__ == '__main__':
    a = 'abcdefghijk'
    b = 'hehe'
    c = zhsendmail('jsqdfs', b).send()