# -*- coding:utf-8 -*-
'''
Created on 2017.7.12

@author: Administrator
'''
#server代码
#导入socket模块
import socket               
#创建socket对象
#s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#获取本地主机名        
host = socket.gethostname()

#设置端口号 
port = 12345 

#将套接字绑定到地址，在AF_INET下，以元组(host, port)的形式表示地址               
s.bind((host, port))        

#开始监听TCP传入链接。backlog指定在拒绝链接之前，操作系统可以挂起的最大连接数。该值至少为1，大部分应用程序设为5.
s.listen(5)                 
while True:
    #accpet()建立客户端连接，接受TCP返回(conn, address),其中conn是新的套接字对象，可以用来接收和发送数，address是连接客户端地址
    c, addr = s.accept()
    print '链接地址', addr
    
    
    c.send('欢迎光临')
    
    #关闭套接字连接
    c.close()
s.close()     

