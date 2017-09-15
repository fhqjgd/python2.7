import os,sys
a=raw_input('Please input your path ')
d=raw_input('Please input you word ')
c=os.walk(a)
i=0
sum=0
for e,f,g in c:
	for name in g:
                sum += 1
		file_list=os.path.join(e,name)
		try:
                 if d in open(file_list).read():
			print file_list
                        i += 1
                except:
                 print "This %s is not a file" %file_list   
print "Have %s files contains %s" %(i,d)
print "All Files Number is %s" %sum

