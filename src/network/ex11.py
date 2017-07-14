'''
Created on 2017.7.13

@author: Administrator
'''
import socket, sys
script = sys.argv[0]
host = sys.argv[1]
textport = sys.argv[2]
filename = sys.argv[3]

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
        
try:
    s.sendall('GET %s HTTP/1.0\r\n\r\n' % filename)
except socket.error, e:
    print 'Error sending data: %s' %e
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
             
