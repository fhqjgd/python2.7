import os, sys, re
i = 0
zc = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
lst = []
f = open('d:\\jpg\\hehe.txt', 'r')
while f.readline():
   zd = re.findall(zc, f.readline())
   lst.append(zd)
f.close()
print lst
a = {}
for h in lst:
    i += 1
    d = tuple(h)
    if lst.count(h) > 1:
        a[d] = lst.count(h)
dd = sorted(a.iteritems(), key = lambda  asd:asd[1], reverse=True)
for z in dd[0:11]:
    print z