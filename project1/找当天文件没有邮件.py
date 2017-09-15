import os, sys,time_myself,datetime,smtplib
smtp = smtplib.SMTP('smtp.163.com')
smtp.login('happytortoise@163.com', 'xiao99')
msg = '''\
From:happytortoise@163.com
Subject: Sorry Backup failue

The backup is failue '''

a = os.walk('D:\\test')
now1 = str(datetime.datetime.now()).split(' ')[0].split('-')
now = now1[0] + now1[1] + now1[2]
n = 0
for c, d, e in a:
     for x in range(len(e)):
         b = os.path.getatime(c+'\\'+e[x])
         k = str(datetime.datetime.fromtimestamp(b)).split(' ',)[0].split('-')
         fnow = k[0] + k[1] + k[2]
         if fnow == now:
             print 'yes'
             n = n + 1
         else:
             print 'no'
if n <= 0:
    s = smtp.sendmail("happytortoise@163.com", "happytortoise@163.com", msg)




#f = str(e)
#g = f.split(' ',)
#h = str(g[0]).split('-')
#print h
#i = h[0] + h[1] + h[2]
#print i