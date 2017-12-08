# -*- coding:utf-8 -*-
'''
Created on 2017.7.18

@author: Administrator
'''
import socket, sys
host = 'localhost'
port = 51423
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((host, port))
data = "x" * 10485760
s.connect((host, port))
byteswritten = 0
while byteswritten < len(data):
    startpos = byteswritten
    endpos = min(byteswritten + 1024, len(data)) #
    byteswritten += s.send(data[startpos:endpos])
    sys.stdout.write("Wrote %d bytes\r" % byteswritten)
    sys.stdout.flush()
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf)
'''    
s.shutdown(1)
print "All data sent."
while 1:
    buf = s.recv(1024)
    if not len(buf):
        break
    sys.stdout.write(buf) 
'''       