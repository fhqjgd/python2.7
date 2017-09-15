# -*- coding: UTF-8 -*-
import paramiko ,color ,sys
reload(sys)
sys.setdefaultencoding('GBK')
col = color.Color()
def changetime():
    print u"你将改变测试环境（192.168.1.232）的日期。"
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect('192.168.1.232' ,22 ,'root' ,'hello@123')
    stdin, stdout, stderr = s.exec_command('date')
    t2 = str(stdout.read())
    #t1 = stdout.read().split(' ')
    t1 = str(t2).split(' ')
    t1 = t1[3]
    print t1
    print u"现在测试服务器的时间是 %s " %str(t2)
    month = raw_input(u"请输入测试服务器的月份(1~12)")
    if month.isdigit():
        if  int(month) <= 12:
            if len(month) == 1:
                month = "0" + month
            else:
                month = month
            days = raw_input(u"请输入你的日期(1~31) ")
            if  days.isdigit():
                if int(days) <= 31:
                    if int(days) < 10:
                        days = "0" + days
                    else:
                        days = days
                    stdin1, stdout1, stderr1 = s.exec_command ('date -s 2017%s%s' %(month,days))
                    stdin2, stdout2, stderr2 = s.exec_command ('date -s %s' %(t1))
                    stdin3, stdout3, stderr3 = s.exec_command ('date')
                    print u'恭喜，测试服务器时间已被修改至' ,str(col.print_blue_text(stdout3.read())).replace('None' ,"")
                    c = raw_input(u"按任意键继续")
                    changetime()
                else:
                    print u"你的日期数太太或者日期格式不对", str(col.print_yellow_text(u'当前日期未修改依然是 %s' % t2)).replace('None' ,"")
                    c = raw_input(u"按任意键继续")
                    changetime()
            else:
                print u"马芸芸还逗我?你输入的是非整数吧", str(col.print_yellow_text(u'XXXXXXXXXXXXX当前日期未修改依然是 %s' % t2)).replace('None' ,"")
                c = raw_input(u"按任意键继续")
                changetime()
        else:
            print u"你的月份数过大或日期格式不对" ,str(col.print_yellow_text(u"XXXXXXXXXXXXXXX当前日期未修改依然是 %s" % t2)).replace('None' ,"")
            c = raw_input(u"按任意键继续")
            changetime()
    else:
        print u"马芸芸你逗我?你输入的是非整数吧" ,str(col.print_yellow_text(u"XXXXXXXXXXXXXX当前日期未修改依然是 %s" % t2)).replace('None' ,"")
        c = raw_input(u"按任意键继续")
        changetime()

if  __name__ == '__main__':
    changetime()