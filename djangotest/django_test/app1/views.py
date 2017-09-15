# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import os ,re ,time ,sys ,subprocess
reload(sys)
sys.setdefaultencoding('gbk')


def index(request):
    return render(request, 'index.html')#

def uploadFile1(request):
    import paramiko
    if request.method == "POST":
        myFile = request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("/tmp/war/", myFile.name), 'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        try:
            t = paramiko.Transport(('192.168.6.24', 22))
            t.connect(username='root', password='hello@123')
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put('/tmp/war' %myFile.name  ,'/tmp/war/%s' %myFile.name )
            t.close()
            return render(request, 'uploadtip.html')
        except Exception, e:
            return HttpResponse(e)
def autofront(request):
    l = []
    import paramiko
    a = time.strftime('%Y%m%d%mm', time.localtime(time.time()))
    b = '/webapps/bbcdev/' + str(a) + '.tar.gz'
    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect('192.168.6.24', 22, 'root', 'hello@123')
        stdin, stdout, stderr = s.exec_command('/tmp/auto/test.sh')
    except Exception, e:
        return HttpResponse(e)
    return render(request, 'baktip.html' ,{'b' : b})
