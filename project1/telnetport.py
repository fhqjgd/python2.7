import socket,time_myself,os
from multiprocessing import Pool

def tenet(ip,port,ci):
    print "         "
    for i in range(ci):
     time_myself.sleep(1)
     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     sk.settimeout(0.1)
     try:
      sk.connect((ip,port))
      print 'Server %s  port %s is OK!' %(ip,port)
     except Exception:
      print 'Server %s port %s  not connect!' %(ip,port)
     b=i+1
     print "This is times %s,Pid is %s"  %(b,os.getpid())
     print "                "
     print "                "
     sk.close()
if __name__ == '__main__':
    p = Pool(3)
    for i in range(4):
        p.apply_async(tenet('202.102.72.3',81,1), (i,))
    p.close()
    p.join()
    print "Done"