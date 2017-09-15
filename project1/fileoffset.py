import os ,sys
f = open("D:\\jpg\hehe.txt" ,'r')
for i in range(1 ,2):
    f.seek(i)
    print f.read()
    print "===="