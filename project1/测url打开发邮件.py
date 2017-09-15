import smtplib
from email.mime.text import MIMEText
from email.header import Header
import urllib,time_myself


def SendEmail(fromAdd, toAdd, subject, attachfile, htmlText):
    strFrom = fromAdd
    strTo = toAdd
    msg = MIMEText(htmlText)
    msg['Content-Type'] = 'Text/HTML'
    msg['Subject'] = Header(subject, 'gb2312')
    msg['To'] = strTo
    msg['From'] = strFrom
    smtp = smtplib.SMTP('smtp.163.com')
    smtp.login('happytortoise@163.com', 'xiao99')
    try:
        smtp.sendmail(strFrom, strTo, msg.as_string())
    finally:
        smtp.close
if __name__ == "__main__":
    while 1 > 0:
        b = open('D:\\1.txt').readlines()
        c = len(b)
        for i in range(c):
            try:
                opurl = urllib.urlopen('http://'+str(b[i])).getcode()
                print 'Website %s is OK' % str(b[i])
            except:
                    print "Website %s can't Open " % str(b[i])
                    SendEmail("happytortoise@163.com", "82560651@qq.com", "Website Cant\'t Open!!", "", str(b[i])+' can\'t open')
        time_myself.sleep(5)