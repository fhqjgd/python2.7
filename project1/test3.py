# -*- coding: UTF - 8  -*-
import os
import re


if __name__ == '__main__':
#    re1 = re.compile('\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}')
#    with open('D:\\test.log') as f:
#        while True:
#            with open('D:\\test1.log' ,'a') as f1:
#                    f1.write(f.readline())
#
     with open('d:\\test.log') as f:
         if "POST" in f.readline():
             print f.readline()
             print "yes"