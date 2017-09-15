from multiprocessing import Pool
import os, time_myself, random
def prt(x):
    print 'Now run task %s ,pid is %s ' % (x, os.getpid())
    start = time_myself.time_myself()
    time_myself.sleep(random.random() * 3)
    end = time_myself.time_myself()
    print 'Now run %s times to excute use %s time' % (x, (end-start))
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(3)
    for i in range(3):
        p.apply_async(prt, (i,))
    p.close()
    p.join()
    print "Done"
