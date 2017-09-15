# -*- coding:utf-8 -*-
y = 0
hello = raw_input( "Hello,we well help you to Find you Keys Are you ready(NO to Exit) ? ")
if __name__ == '__main__':
    if hello == 'no' :
        print "Sorry"
        exit
    else:
        pth = raw_input('Please input you path and  filename ')
        keys = raw_input('Please input you keys ')
        f = open(pth)
        r = f.read()
        if keys in r:
            print keys
            print "locate is ",r.index(keys)
            y=y+1
        if y == 0:
            print "sorry no keys"