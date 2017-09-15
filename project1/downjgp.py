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
            print("Trying SSLv3.")
            self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file, ssl_version=ssl.PROTOCOL_SSLv23)


class HTTPSHandlerV3(urllib2.HTTPSHandler):
    def https_open(self, req):
        return self.do_open(HTTPSConnectionV3, req)

if __name__ == '__main__':
    x = []
    imglist2 = []
    urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))
    f = open('D:\\jpg\\jgp.txt' ,'r')
    #print  f.read()
    for i in f.readlines():
        imgre1 = re.compile(r'http[^\']*jpg\b')
        imglist1 = re.findall(imgre1, i)
        imglist2.append(imglist1)
    j = 1
    for g in imglist2:
        print g,len(g)
        if len(g) >= 1:
            for b in g:
                c = open('D:\\jpg\\%s.jpg' %j ,'wb')
                try:
                    c.write(urllib2.urlopen(b,timeout=3).read())
                except:
                    continue
                j += 1
                c.close()

#


