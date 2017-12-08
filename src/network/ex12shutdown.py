# -*- coding:utf-8 -*-
'''
Created on 2017.7.14

@author: Administrator
'''
'''
服务端可以运行web服务器，或者第3章中的某个例子
运行这个例子并连接服务器，客户端会刚连上就马上断掉服务器。例如第16章的basichttp.py
'''
import socket, sys, time
'''script = sys.argv[0]
host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]'''

#script = sys.argv[0]
host = '192.168.65.150'
textport = 51423
filename = '大家好 ,我是谢尚记！'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error,e:
    print 'strange error creating socket: %s' %e
    sys.exit(1)
#Try parsing it as a numberic port number
try:
    port = int(textport)
except ValueError:
    #That didn't work, so it's probably a protocol name
    #Look it up instead
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error:
        print "Couldn't find your port :%s" %e
        sys.exit(1)
        
try:
    s.connect((host, port))
except socket.gaierror, e:
    print "Address-related error connecting to server: %s" %e
    sys.exit(1)
    
except socket.error, e:
    print "Connect error: %s" %e
    sys.exit(1)

#10秒钟内关闭服务器
print 'sleeping......'
time.sleep(10)
print "continuing."
        
try:
    #s.sendall('GET %s HTTP/1.0\r\n\r\n' % filename)
    s.sendall('GET %s \n' % filename)
except socket.error, e:
    print 'Error sending data: %s' %e
    sys.exit(1)

try:
    s.shutdown(1)
except socket.error, e:
    print 'Error sending data (detected by shutdown): %s' % e
    sys.exit(1)
#如果这一段时间内服务器连通信出现问题，就会发生异常，但这边没做异常处理!    
while 1:
    try:
        
        buf = s.recv(2048)
    except socket.error, e:
        print 'Error recieving data: %s' %e 
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)        
             
