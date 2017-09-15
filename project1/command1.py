# -*- coding: UTF-8 -*-
import paramiko ,color ,sys
reload(sys)
sys.setdefaultencoding('GBK')
col = color.Color()
def changetime():
    print u"你将改变测试环境（192.168.0.22）的日期。"
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect('192.168.0.22' ,22 ,'root' ,'fgoods.com')
    stdin, stdout, stderr = s.exec_command('ping -c  2 192.168.0.22')
    print stdout.read()
if  __name__ == '__main__':
    changetime()