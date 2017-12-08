'''
Created on 2017.7.17

@author: Administrator
'''
import socket, traceback
host = ''
port = 51423
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
while 1:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
    #process the connection    
    try:
        print "Got connect from", clientsock.getpeername()
        
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
        
    #close connection    
    try:
        clientsock.close()
        
    except KeyboardInterrupt:
        raise            
    except:
        traceback.print_exc()