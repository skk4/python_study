'''
Created on 2017.7.13

@author: Administrator
'''

import socket, sys
print 'creating socket......'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print  'create done'

print 'look up port number......'
try:
    port = socket.getservbyname('http', 'tcp')
    print 'done'


    print 'conneting to remote host ,the port number is %d......' % port
    s.connect(('www.baidu.com', port))
    print 'done'
    print s.getsockname()
    print s.getpeername()

except socket.error, e:
    print 'error:',e

