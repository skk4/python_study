'''
Created on 2017.7.18

@author: Administrator
'''
import socket
'''
a_tuple = [('1', ('2', '22', '222'), '3'),('4',('5', '55', '555'), '6'), ('1', ('7', '77', '777'), '3')]
print [x[1][1] for x in a_tuple]
'''
localip = socket.gethostname()
print localip

fdqdn = socket.getfqdn(localip)

print fdqdn

result = socket.getaddrinfo(localip, None, 0, socket.SOCK_STREAM)

ips = [x[4][0] for x in result]
new_ips = ', '.join(ips)

print new_ips
