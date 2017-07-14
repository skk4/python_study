# -*- coding:utf-8 -*-
'''
Created on 2017.7.12

@author: Administrator
'''
#客户端
#导入客户端
import socket

#创建客户端对象
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接address套接字
phone.connect(('192.168.22.174',23456))
while True:
    msg=raw_input(">>>:").strip()
    if not msg:
        continue
    
    #发送信息给服务器端
    phone.send(msg)
    
    #接收服务器端信息
    data=phone.recv(1024)
    print'收到服务端发来的信息',data
phone.close()