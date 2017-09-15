information = []
for i in range(20):
 name = raw_input('Please Input you name ')
 while len(name) < 1 or name.isspace():
    name = raw_input('Please Input you name ')
 information.append(name)
 age = raw_input('Please Input you age(must be a number) ')
 while len(age) <= 0 or not age.isdigit():
    age = raw_input('Please Input you age(must be a number) ')
 information.append(age)
 locate = raw_input('Please Input you locate ')
 while len(locate) <= 0 or locate.isspace():
    locate = raw_input('Please Input you locate ')
 information.append(locate)
 print 'Your name is ' + name
 print 'Your age is ' + age
 print 'Your locate is ' + locate
 print len(information)
 print information
 i = +i
 qui = raw_input('Do you want to Exit ? YES,NO ')
 if qui == 'yes':
     break
print information