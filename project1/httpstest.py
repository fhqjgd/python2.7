# -*- coding:utf-8 -*-
import httplib, ssl, urllib2, socket,re,urllib
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


# install opener


if __name__ == "__main__":
    lsturl = []
    imglist = []
    imgre = re.compile(r'href="htm_data[^"]*"\B')
    urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))
    r = urllib2.urlopen("http://cl.fatt.pw/thread0806.php?fid=16")
    imglist = re.findall(imgre, r.read())
    for i in imglist:#
        lsturl.append('http://cl.fatt.pw/'+i[6:-1])
    print lsturl
    lenlst = len(lsturl)
    p = Pool(30)
    for x in lsturl:
        r1 = urllib2.urlopen(x)
        jpg = r1.read()
        imgre1 = re.compile(r'src=\'http[^\']*jpg\'\B')
        imglist1 = re.findall(imgre1 ,jpg)
    f = open('D:\\jpg\\jgp.txt', 'w')
    for j in imglist1:
        f.writelines(j+'\n')
    f.close()


    #print(r.read())
    #b = r.read()
    #f = open('D:\/2.jpg' ,'wb')
    #f.write(b)