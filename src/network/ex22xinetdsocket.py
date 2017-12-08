'''
Created on 2017.7.18

@author: Administrator
'''
import socket, sys, time
#s = socket.fromfd(sys.stdin.fileno(), socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.sendall("Welcom.\n")
s.sendall("According to our records,you are connected from %s.\n" % str(s.getpeername()))
s.sendall("The local time is %s.\n" % time.asctime())
