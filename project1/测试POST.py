
# -*- coding:utf-8 -*-
import  re, urllib ,urllib2 ,https
if __name__ == '__main__':
    urllib2.install_opener(urllib2.build_opener(https.HTTPSHandlerV3()))
    n = 0
    for i in range(2):
        reqheaders = {'Content-type': 'application/x-www-form-urlencoded',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Host': 'web.umeng.com',
                      'Origin': 'https://web.umeng.com',
                      'Referer': 'https://web.umeng.com',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1', }
        #data = {'username':'wangkai@forfarming.com' ,'password':'3fn@123456' }
        #a = urllib2.Request('https://web.umeng.com/main.php?c=site&a=show&from=login' ,data = urllib.urlencode(data) ,headers = reqheaders)
        b = urllib2.urlopen("https://i.umeng.com/loginframe?app_id=cnzz&redirectURL=https%3A%2F%2Fweb.umeng.com%2Fmain.php%3Fc%3Dsite%26a%3Dshow%26from%3Dlogin")
        print b.read()
        #if b: n +=# 1
        #print 'ok'
        #print n