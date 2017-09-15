import socket,time
ip=raw_input("Input your IP or Hostname ")
port=input("Input you port ")
ci=int(input("Input you try times "))
print "         "
for i in range(ci):
 time.sleep(1)
 sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 sk.settimeout(2)
 try:
  sk.connect((ip,port))
  print 'Server %s  port %s is OK!' %(ip,port)
 except Exception:
  print 'Server %s port %s  not connect!' %(ip,port)
 b=i+1
 print "This is times %s"  %b
 print "                "
 print "                "
 con
 sk.close()
