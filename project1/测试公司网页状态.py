# -*- coding:utf-8 -*-
import  re, urllib ,msendmail
if __name__ == '__main__':
    lsturlmain = []
    imglistmain = []
    imgremain = re.compile(r'href="[^"]*html\b')  #这里是找源码内网址的
    rmain = urllib.urlopen("http://192.168.1.76:8080/jeesite")  #这里是地址
    imglistmain = re.findall(imgremain, rmain.read())
    for imain in imglistmain:
        if imain[6] == '/':
            lsturlmain.append('http://192.168.1.76:8080'+imain[6:])  #这里是截网址的
        else:
            lsturlmain.append(imain[6:])
    lsturlmain = list(set(lsturlmain))
    print lsturlmain,len(lsturlmain)
    for i in lsturlmain:
        try:
            print urllib.urlopen(i,).getcode(),'OK'
        except:
            print "error",i
            msendmail.zhsendmail('Can not open url' ,'www.ygline/'+str(i))