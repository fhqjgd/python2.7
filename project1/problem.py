#!/usr/bin/python
# -*- coding:utf-8 -*-
import os ,sys ,re
i = 0
sysprint = re.compile(r'\/\bsys.*')
procprint = re.compile(r'\/\bproc.*')
with open('/tmp/noproblem.txt' ,'r') as f:
    a = f.read()
    sysfind = re.findall(sysprint ,a)
    procfind = re.findall(procprint ,a)
    for x in  f.readlines():
        if x not in sysfind and x not in procfind:
            i +=1
            print x
print i


