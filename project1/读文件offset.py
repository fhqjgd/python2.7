import os, sys, re ,time
i = 0
zc = re.compile(r'except')
lst = []
while 2 > 1:
    f = open('d:\\1.log', 'r')
    b = f.readlines()[-1]
    zc1 = zc.findall(b)
    if zc1:
        print  b
    time.sleep(5)
    f.close()
