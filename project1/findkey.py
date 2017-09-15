# -*- coding:utf-8 -*-
import os ,sys ,re
a = raw_input('Please input your path ')
d = raw_input('Please input you word ')
c = os.walk(a)
re = re.compile(d)
i = 0
hehe = 0
for e, f, g, in c:
    for name in g:
        hehe += 1
        file_list = os.path.join(e, name)
        try:
            with open(file_list) as f1:
                    if d in f1.read():
                        print file_list
                        i += 1
        except:
            print "This %s is not a file" % file_list
print "Have %s files contains %s" % (i, d)
print "All Files Number is %s" % hehe
while True:
    a = raw_input('Exit')
    exit()