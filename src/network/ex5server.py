'''
Created on 2017.7.12

@author: Administrator
'''
#服务端 运行，可打开终端执行输入 telnet localhost 51423
import socket
host=''
port=51423
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

print "Server is running on port %d;press Ctrl-C to terminate." %port
while 1:
    clientsock,clientaddr=s.accept()
    clientfile=clientsock.makefile('rw',0)
    clientfile.write("welcome,"+str(clientaddr)+'\n')#类似于send发送
    clientfile.write("Please enter a string:")
    line=clientfile.readline().strip()#类似于recv,接收数据
    clientfile.write("You entered %d characters ,filename is :%s \n" %(len(line), line))
    clientfile.close()
    clientsock.close()