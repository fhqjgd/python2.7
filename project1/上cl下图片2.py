# -*- coding:utf-8 -*-
import httplib, ssl, urllib2, socket,re,urllib,time,multiprocessing,os
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

def  write_txt(i):
    for xmain in i:
        print os.getpid()
        try:
            r1main = urllib2.urlopen(xmain ,timeout=15).read()
            print r1main
            imgre1main = re.compile(r'src=\'http[^\']*jpg\'\B')
            imglist1main = re.findall(imgre1main ,r1main)
            imglist1main = list(set(imglist1main))
            imglist2main = []
            imglist2main.append(imglist1main)
            imglist2main = list(set(imglist2main))
            print imglist2main ,"hehehehehehehhe"
            #lock.acquire()
            with open('D:\\jpg\\1\\jgpnew0305.txt', 'a') as tt:
                for jmain in imglist2main:
                    print jmain
                    tt.write(str(jmain))
            #lock.release()
            print '##########################Print  to txt Done \n ###############################'*20
        except:
            print "sorry"

if __name__ == '__main__':
    urllib2.install_opener(urllib2.build_opener(HTTPSHandlerV3()))
    p = multiprocessing.Pool(16)
    lock = multiprocessing.Lock()
    lsturlmain = []
    imglistmain = []
    #imglist2main = []
    imgremain = re.compile(r'href="htm_data[^"]*"\B')  #这里是找源码内网址的
    rmain = urllib2.urlopen("http://cl.fatt.pw/thread0806.php?fid=16&search=&page=6")  #这里是地址
    imglistmain = re.findall(imgremain, rmain.read())
    for imain in imglistmain:
        lsturlmain.append('http://cl.fatt.pw/'+imain[6:-1])  #这里是截网址的
    lsturlmain = list(set(lsturlmain))
    print lsturlmain
    for i in lsturlmain:
        print i,"+++++"
        p.apply_async(write_txt ,(i,))
    p.close()
    p.join()
    print "Done"
    #x = []
    #imglist2 = []
    #f = open('D:\\jpg\\jgpnew0305.txt' ,'r')   #这里图片目录文件名
    #for i in f.readlines():
    #    imgre1 = re.compile(r'http[^\']*jpg\b')
    #    imglist1 = re.findall(imgre1, i)
    #    imglist2.append(imglist1)
    #j = 1
    #for g in imglist2:
    #    print g,len(g)
    #    if len(g) >= 1:
    #        for b in g:
    #            c = open('D:\\jpg\\new0305%s.jpg' %j ,'wb')  #这里改图片格式文件名
    #            try:
    #                c.write(urllib2.urlopen(b,timeout=3).read())
    #            except:
    #                continue
    #            j += 1
    #            c.close()