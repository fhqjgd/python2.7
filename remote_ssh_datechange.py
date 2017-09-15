import paramiko
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect('192.168.0.22' ,22 ,'root' ,'fgoods.com')
stdin, stdout, stderr = s.exec_command ('date')
t1 = stdout.read().split(' ')
t1 = t1[4]
month = raw_input("Please Input you month(1~12) ")
if len(month) == 1:
    month = "0" + month

days = raw_input("Please Input you days(1~31) ")
if int(days) < 10:
    days = "0" + days
stdin1, stdout1, stderr1 = s.exec_command ('date -s 2017%s%s' %(month,days))
stdin2, stdout2, stderr2 = s.exec_command ('date -s %s' %(t1))
stdin3, stdout3, stderr3 = s.exec_command ('date')
print "Now your time is %s" %stdout3.read()