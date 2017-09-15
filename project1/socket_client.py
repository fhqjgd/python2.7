if __name__ == '__main__':
    import socket ,time ,struct
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.connect(('192.168.64.17', 20000))
    #print "Done"
    #time.sleep(2)
    #a = '{"ClassName":"com.ygline.erp.server.nexs.web.OutOrderAction","ClassMethod":"exportdetail","ParamJson":"\\"2c9854815aee75eb015aee86c5580003,2c9854815aee4c7a015aee7009d3000a\\"","ParamJsonSize":0,"MethodType":"json\\"}'#
    #sock.send(a)
    #data1 = sock.recv(1024)
    #print data1
    #sock.close()
    a = ('{"ClassName":"com.ygline.erp.server.nexs.web.OutOrderAction","ClassMethod":"exportdetail","ParamJson":"\\"2c9854815aee75eb015aee86c5580003,2c9854815aee4c7a015aee7009d3000a\\"","ParamJsonSize":0,"MethodType":"json\\"}')
    b= struct.Struct(a)
    packed_data = b.pack(a)
    unpacked_data = b.unpack(packed_data)
    print a
    print b
    print packed_data
    print unpacked_data