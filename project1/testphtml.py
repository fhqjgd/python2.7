# -*- coding:utf-8 -*-
import socket,time_myself,os,urllib,requests,urllib2
from multiprocessing import Pool
def ope(x):
    print 'Now task is %s,pid is %s' %(x,os.getpid())
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    headers = {'User-Agent': user_agent}
    try:
        req = urllib2.Request('http://cl.fatt.pw/index.php',data=None,headers=headers)
        response = urllib2.urlopen(req)
        #print response.read()
        print "OK"
        print "==========================================================="
    except:
        print "sorry"
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    for d in range(100):
        p = Pool(30)
        for i in range(30):
            p.apply_async(ope, (i,))
        p.close()
        p.join()
    print "Done"