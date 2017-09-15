import smtplib
from email.mime.text import MIMEText
from email.header import Header
import urllib,
smtp = smtplib.SMTP('smtp.163.com')
smtp.login('happytortoise@163.com', 'xiao99')
msg = '''\
From:happytortoise@163.com
Subject: test

This is a test '''
smtp.sendmail("happytortoise@163.com","happytortoise@163.com",msg)