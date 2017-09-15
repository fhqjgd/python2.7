# -*- coding:utf-8 -*-

import re
import urllib
x = 0
url = 'http://m2.media.videoszoofilia.org/flv/'
for i in range(362,364):
    try:
        urllib.urlretrieve(url+str(i), 'D:\jpg\%s.flv' % x)
        x += 1
    except:
        print 'Sorry Can \'t open '
        exit()