'''
Created on 2017.7.20

@author: Administrator
'''
import struct, sys
'''a_tuple = (0, 1)
a_list = [0,1]
print "welcom ," + str(a_tuple)+ " :" + str(a_list)'''

def htons(num):
    return struct.pack('!H', num)

def htonl(num):
    return struct.pack('!I', num)

def ntohs(data):
    return struct.unpack('!H', data)[0]

def ntohl(data):
    return struct.unpack('!I', data)[0]

def sendstring(data):
        return htonl(len(data)) + data
print "Enter a string:"
astr = sys.stdin.readline().rstrip()   

print repr(sendstring(astr)) 