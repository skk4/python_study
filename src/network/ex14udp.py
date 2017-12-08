# -*- coding:utf-8 -*-
'''
Created on 2017.7.17

@author: Administrator
'''
'''
需第3章 udp服务器作为服务器端;udpechoserver.py
'''
import socket, sys, time
'''
script = sys.argv[0]
host = sys.argv[1]
textport = sys.argv[2]
'''
host = '192.168.65.150'
textport = 51423
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    port =  socket.getservbyname(textport, 'udp')
s.connect((host, port))

print "sleep..."
time.sleep(10)
print "continue..."

print "Please enter data to transmit:"

data =  sys.stdin.readline().strip()

s.sendall(data)

print "Looking for repiles, press ctrl-c or ctrl-break to stop"

try:
    s.shutdown(1)
except socket.error, e:
    print 'Error sending data (detected by shutdown): %s' % e
    sys.exit(1)

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
