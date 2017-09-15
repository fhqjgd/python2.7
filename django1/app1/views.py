# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from dwebsocket import accept_websocket ,require_websocket
import os ,sys ,re ,time ,sys ,subprocess
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
        destination = open(os.path.join("d:\\test", myFile.name), 'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        try:
            t = paramiko.Transport(('47.93.49.248',3322))
            t.connect(username='root', password='hello@123')
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put('D:\\test\\%s' %myFile.name  ,'/tmp/auto/%s' %myFile.name )
            t.close()
            return render(request, 'uploadsuccess.html')
        except Exception, e:
            return HttpResponse(e)
def auto(request):
    l = []
    import paramiko
    a = time.strftime('%Y%m%d', time.localtime(time.time()))
    b = '/etrade/fgoods_nerp/webapps/' + str(a) + '.tar.gz'
    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect('192.168.0.22', 22, 'root', 'fgoods.com')
        stdin, stdout, stderr = s.exec_command('/tmp/auto/auto1.sh')
    except Exception, e:
        return HttpResponse(e)
    return render(request, 'auto.html' ,{'b' : b})


@require_websocket
def ws(request):
    message = request.websocketr.ead('b')
    request.websocket.send(message)

def hehe(request):
    return render(request, 'ws.html')
