# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import urllib, re ,time

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
        with open('D:\\ip.txt') as hehe:
            hehe1 = hehe.read()
            print type(hehe1)
        ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        context = urllib.urlopen('http://1212.ip138.com/ic.asp')
        html = context.read()
        iplist = re.findall(ip ,html)
        for i in iplist:
            print i
            if  i == hehe1:
                print 'ok'
            else:
                write1 = open('D:\\ip.txt' ,'wb')
                write1.write(i)
                print 'writeok'
                SendEmail("happytortoise@163.com", "82560651@qq.com", u"福农的IP变了", "",
                          u"新的IP地址是 %s" %i)
        time.sleep(5)

