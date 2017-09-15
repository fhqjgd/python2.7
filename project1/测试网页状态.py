
# -*- coding:utf-8 -*-
import  re, urllib ,urllib2 ,https
if __name__ == '__main__':
    urllib2.install_opener(urllib2.build_opener(https.HTTPSHandlerV3()))
    lsturlmain = []
    imglistmain = []
    imgremain = re.compile(r'href="[^"]*\"\B')  #这里是找源码内网址的
    rmain = urllib2.urlopen("https://www.forfarming.com/b.jsp")  #这里是地址
    imglistmain = re.findall(imgremain, rmain.read())
    for url in imglistmain:
        #print url[6:-1]
        if url[6:-1] <> 'javascript:void(0)' and url[6:-1] is not '' and url[6:-2] <> 'javascript:void(0)' :
            try:
                print urllib.urlopen(url[6:-1]).getcode()
                if  urllib.urlopen(url[6:-1]).getcode() == 500 or urllib.urlopen(url[6:-1]).getcode() == 404:
                    print url[6:-1]
            except:
                print url ,"This page can't open"