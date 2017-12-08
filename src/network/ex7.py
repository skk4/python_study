# -*- coding:utf-8 -*-
'''
Created on 2017.7.13

@author: Administrator
'''
#客户端访问 quux.org /首页
import socket,sys
'''
script = sys.argv[0]
port =70
host=sys.argv[1]

filename=sys.argv[2]
'''
port = 51423
host = '192.168.65.150'
filename = 'hello ,xieshangji from xiamen'
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    
    s.connect((host,port))
except socket.gaierror ,e:
    print 'error %s' %e
    sys.exit(1)

fd = s.makefile('rw', 0)
fd.write(filename +"\r\n")
#fd.write(filename)
for line in fd.readlines():
    sys.stdout.write(line)    