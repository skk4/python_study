# -*- coding:utf-8 -*-
'''
Created on 2017.7.18

@author: Administrator
'''
import socket, traceback
#绑定所有连接
host = ''
port = 51423
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while 1:
    try:
        clientsocket, clientaddress = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    #proces connection
    try:
        print "Got connection from：", clientsocket.getpeername()
        while 1:
            data = clientsocket.recv(4096)#接收数据给请求客户端
            if not len(data):
                break
            clientsocket.sendall(data)#返回数据给请求客户端
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
    # close connection
    try:
        clientsocket.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()        
