# -*- coding:utf-8 -*-

import re
import urllib
x = 0
url = 'http://www.baidu.com'
try:
    page = urllib.urlopen(url)
except:
    print "Sorry,Can't open URL"
    exit
html = page.read()
imgre = re.compile(r'src="(.*?\.jpg)"')
imglist = re.findall(imgre,html)
for i in imglist:
    print i
for t in imglist:
    if 'http://' not in t:
        urllib.urlretrieve(url+t, 'D:\jpg\%s.jpg' % x)
        x = x +1
    else:
        urllib.urlretrieve(t,'D:\jpg\%s.jpg' % x)
        x = x + 1



