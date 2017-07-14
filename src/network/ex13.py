'''
Created on 2017.7.14

@author: Administrator
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
        
            