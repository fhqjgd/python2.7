import os ,sys ,multiprocessing ,time

def write_txt(x):
    lock.acquire()
    time.sleep(10)
    print "1"
    with open("D:\\jpg\\1\\test" ,'a') as f:
        f.write(str(os.getpid())+'%s \n' %x)
    lock.release()

if __name__ == '__main__':
    p = multiprocessing.Pool(1)
    lock = multiprocessing.Lock()
    for i in range(5):
        p.apply_async(func=write_txt ,args=(i,))
    p.close()
    p.join()
    print "Done"