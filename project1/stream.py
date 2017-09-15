# -*- coding: utf-8 -*-
import sys ,re ,urllib2 ,chardet ,struct
s = '中文'
print len(s)
data = struct.pack('6s' ,s)
print repr(data) ,data
data1 = struct.unpack('6s' ,data)
print data1 ,repr(data1)