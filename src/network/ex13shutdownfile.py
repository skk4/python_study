# -*- coding:utf-8 -*-
'''
Created on 2017.7.14

@author: Administrator
'''
'''
服务端可以运行web服务器，或者第3章中的摸个例子
运行这个例子并连接服务器，客户端会刚连上就马上断掉服务器。例如第16章的basichttp.py
'''
import socket, sys, time
script = sys.argv[0]
host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
except socket.error, e:
    print 'Strange error creating socket: %s' % e
    sys.exit(1)
# Try parsing it as numeric port number
try:
    port =  int(textport)
except ValueError:
    #That it did't work . look it up instead
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error, e:
        print "Couldn't find  your port :%s" % e
        sys.exit(1)
try:
    s.connect((host, port))
except socket.gaierror, e:
    print "Address-related error connecting to server: %s" % e
    sys.exit(1)
except socket.error, e:
    print "Connect error :%s" % e
    sys.exit(1)
#0:不使用缓冲器，1：使用缓冲器    
fd = s.makefile('rw', 0)
print 'sleeping......'
time.sleep(10)
print 'continuing......'

try:
    fd.write("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, e:
    print "Error send date : %s" % e
    sys.exit(1)
try:
    fd.flush()
except socket.error, e:
    print "Error sending data (detected by flush) : %s" % e
    sys.exit(1)

try:
    s.shutdown(1)
    s.close()
except socket.error, e:
    print "Error sending data detect by shutdown: %s" % e
    sys.exit(1)
while 1:
    try:
        buf = fd.read(2048)
    except socket.error, e:
        print 'receiving data error: %s' % e
        sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf)        
                                            
    
    
        
                        

            