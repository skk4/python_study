'''
Created on 2017.7.18

@author: Administrator
'''
import socket, sys
script = sys.argv[0]
host = sys.argv[1]
result = socket.getaddrinfo(host, None)
print result
