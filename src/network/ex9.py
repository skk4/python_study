'''
Created on 2017.7.13

@author: Administrator
'''
import socket, sys
print 'creating socket......'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print  'create done'

print 'conneting to remote host......'
s.connect(('www.baidu.com', 80))
print 'done'

    