from multiprocessing import Pool
import os, time_myself, random,urllib
def prt(x):
    try:
         print urllib.urlopen(x).getcode() ,'ok'
    except:
         print 'error'

if __name__ == '__main__':
    #print 'Parent process %s.' % os.getpid()
    p = Pool(100)
    for i in range(30):
        x = "http://192.168.1.192:8080"
        p.apply_async(prt, (x,))
    p.close()
    p.join()
    print "Done"
