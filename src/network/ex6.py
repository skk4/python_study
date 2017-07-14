# -*- coding:utf-8 -*-
'''
Created on 2017.7.12

@author: Administrator
'''
#windows 执行 python ex6.py quux.org /
import socket,sys
script = sys.argv[0]
port =70
host=sys.argv[1]

filename=sys.argv[2]

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    
    s.connect((host,port))
except socket.gaierror ,e:
    print 'error %s' %e
    sys.exit(1)

s.sendall(filename+"\r\n")

while 1:
    buf=s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
    
