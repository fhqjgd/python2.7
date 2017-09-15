# -*- coding:utf-8 -*-
import re
import urllib
x = 0
url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%CC%EC%BA%A3%D2%ED&hs=2&xthttps=000000&fr=ala&ori_query=%E5%A4%A9%E6%B5%B7%E7%BF%BC&ala=0&alatpl=sp&pos=0'
try:
    page = urllib.urlopen(url)
except:
    print "Sorry,Can't open URL"
    exit
html = page.read()
imgre = re.compile(r'data:image(.+?\.jpg)')
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