import datetime ,time ,os ,random
from multiprocessing import Pool
def t(x):
    while 6 > x:
        time.sleep(1)
        a =  datetime.datetime.now()
        print a, "my pid is " ,os.getpid() ,"\n"
if __name__ == '__main__':
    p = Pool(3)
    for i in range(3):
        p.apply_async(t ,(i, ))
    p.close()
    p.join()