# -*- coding:utf-8 -*-
import httplib, ssl, urllib2, socket,re,urllib,time_myself
from multiprocessing import Pool
class HTTPSConnectionV3(httplib.HTTPSConnection):
    def __init__(self, *args, **kwargs):
        httplib.HTTPSConnection.__init__(self, *args, **kwargs)

    def connect(self):
        sock = socket.create_connection((self.host, self.port), self.timeout)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        try:
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv23)
        except ssl.SSLError, e:
            print("Sorry SSL Can't Open.")



class HTTPSHandlerV3(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSConnectionV3, req)

if __name__ == '__main__':
    urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))
    j = 0
    lsturlmain = []
    imglistmain = []
    imglist2main = []
    imgremain = re.compile(r'href="htm_data[^"]*"\B')  #这里是找源码内网址的
    rmain = urllib2.urlopen("http://cl.fatt.pw/thread0806.php?fid=16&search=&page=7")  #这里是地址
    imglistmain = re.findall(imgremain, rmain.read())
    for imain in imglistmain:
        lsturlmain = 'http://cl.fatt.pw/'+imain[6:-1]  #这里是截网址的
        print lsturlmain+ '#'*50
        r1main = urllib2.urlopen(lsturlmain).read()
        imgre1main = re.compile(r'src=\'http[^\']*jpg\'\B')
        imglist1main = re.findall(imgre1main ,r1main)
        for i in imglist1main:
            imgre1 = re.compile(r'http[^\']*jpg\b')
            imglist1 = re.findall(imgre1, i)
            for g in imglist1:
                print g,len(g)
                if len(g) >= 1:
                   c = open('D:\\jpg\\new0307%s.jpg' %j ,'wb')  #这里改图片格式文件名
                   try:
                       c.write(urllib2.urlopen(g,timeout=3).read())
                       print "OK"
                   except:
                       print "no"
                       c.close()
                       continue
                   j += 1