# -*- coding:utf-8 -*-
'''
Created on 2017.7.18

@author: Administrator
'''
import sys
print "Welcome..."
print "Please enter a string:"
sys.stdout.flush()
line = sys.stdin.readline().strip()
print "You entered %d characters." % len(line)

'''
UNIX用xinetd处理socket服务端
service pythontestserver
{
   flags          = NAMEINARGS
   type           = UNLISTED
   port           = 51423
   socket_type    = stream
   protocol       = tcp
   wait           = no
   user           = root
   server         = /root/example.py
   server_args    = /root/example.py
}
'''