# -*- coding:utf-8 -*-
'''
Created on 2017.7.17

@author: Administrator
'''
import socket, sys, struct, time
#hostname = 'time.nist.gov'
hostname = 'localhost'
#hostname2 = 'www.baidu.com'
#port = 37
port = 51423
host = socket.gethostbyname(hostname)
#host2 = socket.gethostbyname(hostname2)
#print host
#print host2

s = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
s.sendto('', (host, port))

print "Looking for repiles, press ctrl-c or ctrl-break to stop"
#recvform 返回一个tuple(实际返回数据，发送数据机器的地址)
buf = s.recvfrom(2048)[0]
if len(buf) != 4:
    print "Wrong-sized reply %d: %s" %(len(buf), buf)
    sys.exit(1)
secs = struct.unpack("!I",buf)[0]
secs -= 2208988800
print time.ctime(int(secs))   