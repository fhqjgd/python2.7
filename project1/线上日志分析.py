# -*- coding: UTF - 8  -*-
import os, sys, re ,json
class tongji(object):
    def __init__(self):
        self.alllist = []
        self.iptimes = []
        self.times = []
        self.zset = {}
        self.urltimes = []
        self.b = 0
    def open_file(self ,path):
        with open(path) as f:
            for i in f:
                i = re.sub(r"\\" ,"&" ,i)  # 从读的每行里替换\为&,w
                self.alllist.append(i)
        return self.alllist.__len__()
    def number(self ,duixiang):
        for j in self.alllist:
            j = json.loads(j)         #json转换
            #print j
            self.iptimes.append(j[duixiang])     #字典里的key
        for x in self.iptimes:
            if x not in self.times:    #如果新字典没有这个value就添加
                self.times.append(x)
        for z in self.times:
            self.zset[z] = self.iptimes.count(z)     #转变成字典，并统计数量
        zset1 = sorted(self.zset.iteritems(), key = lambda  asd:asd[1], reverse=True)  #以降序排字典的key
        for y in zset1:
            print y[0]+" "*5+"The Number is" ,y[1]
    def number_url(self):
        templist = []
        for j in self.alllist:
            j = json.loads(j)
            self.urltimes.append(j["request"])
        re1 = re.compile(r'POST')
        for u1 in self.urltimes:
            if re.findall(re1 ,u1):
                self.b += 1
            else:
                templist.append(u1)
        for x in templist:
            if x not in self.times:
                self.times.append(x)
        for z in self.times:
            self.zset[z] = templist.count(z)
        zset1 = sorted(self.zset.iteritems(), key=lambda asd:asd[1], reverse=True)
        for y in zset1:
            y1 = re.sub('GET' ,'' ,y[0])
            y1 = re.sub('HTTP/1.1' ,'' ,y1)
            y1 = re.sub(' ' ,'' ,y1)
            print "http://192.168.1.248" + y1 + "    The times is  " + str(y[1])

    def number_ip_url(self):
        dict1 = {}
        j1 = {}
        templist = []
        templist1 = []
        templist2 = []
        dict1 = {}
        for j in self.alllist:
            j = json.loads(j)
            self.urltimes.append(j["remote_ddr"])
        re1 = re.compile(r'POST')
        for u1 in self.urltimes:
            if re.findall(re1 ,u1):
                self.b += 1
            else:
                templist.append(u1)
        for x in templist:
            if x not in self.times:
                self.times.append(x)
        for z in self.times:
            self.zset[z] = templist.count(z)
        zset1 = sorted(self.zset.iteritems(), key=lambda asd:asd[1], reverse=True)
        b1 = 0
        for xx in zset1:
            if b1 < 10:
                templist1 = []
                print xx[0]
                print "+++"*30
                b1 += 1
                j1 = {}
                for j1 in self.alllist:
                    j1 = json.loads(j1)
                    if j1["remote_ddr"] == xx[0]:
                        templist1.append(j1["request"])
                myset = set(templist1)
                print myset
                for item in myset:
                    #print "The IP  " + str(xx[0]) + " GET URL  %s Times is "%str(item) + str(templist1.count(item))
                    dict1[item] = templist1.count(item)
                #print dict1
                templist2 = sorted(dict1.iteritems(), key=lambda asd: asd[1], reverse=True)
                for xxx in templist2:
                    print "The ip %s access URL  %s       Times %s "%(xx[0] ,str(xxx[0]) ,str(xxx[1]))
            else:
                break


if __name__ == '__main__':
    b = tongji()
    b.open_file('D:\\test.log')
    #b.number("remote_ddr")
    #b.number_url()
    b.number_ip_url()