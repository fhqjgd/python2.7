# -*- coding: UTF - 8  -*-
import os, sys, re ,json ,urllib
def getlocal(x):
    url1 = urllib.urlopen( 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' %x)
    data = url1.read()
    datadict = json.loads(data, encoding='utf-8')
    local1 = datadict['data']
    local = local1['city']
    return local
i = 0
zc = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
lst = []
f = open('d:\\jpg\\catalina.out', 'r')
zd = re.findall(zc, f.read())
f.close()
a = {}
for c in zd:
    if zd.count(c)>1:
        a[c] = zd.count(c)
dd = sorted(a.iteritems(), key = lambda  asd:asd[1], reverse=True)
for key in dd:
    print " IP  "  +  unicode(key[0]) + " Times " + unicode(key[1])  + '  City  ' +  getlocal(key[0])
