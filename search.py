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
			    print "%s���Ǹ��ɶ��ļ�" %file_list
		test.close()
print "���� %s �ļ� �����ؼ��� %s" %(i,d)
raw_input('�����������˳�')
