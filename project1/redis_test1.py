import  redis ,re
pool = redis.ConnectionPool(host='192.168.0.5',port=6379)
r = redis.Redis(connection_pool=pool)
z = []
b = []
imgre = re.compile(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}')
str1 = r.get('test').split('\n')
for i in str1:
    imglist = re.findall(imgre, str(i))
    b.append(imglist)
for f in range(len(b)):
    x = str(b.count(b[f]))+' '+str(b[f])
    z.append(x)
print list(set(z))
r.set(b ,'hehehe')
print r.get(b)