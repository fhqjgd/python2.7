# -*- coding:utf-8 -*-
from ftplib import FTP
import os
def ftpconnect():
    ftp_server = '192.168.0.23'
    username = 'ximage'
    password = 'ximages'
    ftp=FTP()
    ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
    ftp.connect(ftp_server,21) #连接
    ftp.login(username,password) #登录，如果匿名登录则用空串代替即可
    return ftp
def ftpupload():
    b = []
    for root, dirs, files in os.walk('d:\\test\\'):
        b = files
    for i in b:
       ftp = ftpconnect()
       ftp.cwd('ERP/InOrder/20170414/')
       ftp.set_pasv(False)
       #bufsize = 1024
       localpath = 'd:\\test\\'
       localpath = localpath + str(i)
       str(localpath)
       # print localpath + "sssssssssssssssssssssssss"
       fp = open(localpath, 'rb')
       ftp.storbinary('STOR %s' %i+'zhaohao', fp)
       ftp.set_debuglevel(0)
       fp.close()
       ftp.quit()
if __name__ == '__main__':
    ftpupload()



