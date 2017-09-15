#coding=utf-8 
import os,sys
a=raw_input('Please input your path ')
d=raw_input('Please input you word ')
c=os.walk(a)
i=0
for e,f,g in c:
	for name in g:
		file_list=os.path.join(e,name)
		test=open(file_list)
		try:
		    if d in test.read():
				i += 1
				print file_list
		except:
			    print "%s不是个可读文件" %file_list
		test.close()
print "共有 %s 文件 包含关键字 %s" %(i,d)
raw_input('输入任意输退出')
