# -*- coding:utf-8 -*-
'''
Created on 2017.7.12

@author: Administrator
'''
#服务端
#导入
import socket

#创建socket对象，AF_INET，服务器之间网络连接；SOCK_STREAM，TCP,流式套接字
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#设置选项，SOL_SOCKET，是指正在使用的socket选项；
#SO_REUSEADDR，当socket关闭后，本地端用于该socket的端口号立刻就可以被重用。通常来说，只有经过系统定义一段时间后，才能被重用
#1，将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

#绑定套接字地址
phone.bind(('192.168.22.174',23456))

#开始TCP传人连接监听
phone.listen(5)
print('---------')


while True:
    
    #建立客户端连接，接受TCP返回(conn, address)
    conn,addr=phone.accept()

    print "电话线路",conn
    print "客户端手机号码",addr
    while True:  #通讯循环
        try:
            #接收客户端信息
            msg=conn.recv(1024)
            if not msg:
                break
            print'客户端信息：',msg
            #服务端发送信息
            conn.send(msg.upper())
        except Exception:
            break
    conn.close()
phone.close()