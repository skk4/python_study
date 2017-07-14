# -*- coding:utf-8 -*-
'''
Created on 2017.7.12

@author: Administrator
'''

#客户端代码
#导入socket模块
import socket
               
#创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#获取本地主机地址
host = socket.gethostname()

#设置端口 
port = 12345               

#连接到address地址:(host, port)处套接字，如果连接出错，返回socket.error错误
s.connect((host, port))

#接收TCP套接字的数据，返回字符串数据，bufsize指定接收的最大数据量
print s.recv(1024)

#关闭套接字连接
s.close()  