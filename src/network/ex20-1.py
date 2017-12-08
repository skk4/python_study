'''
Created on 2017.7.17

@author: Administrator
'''
import time, struct
print "time.time(): %d" %int(time.time()) #int 1500270074
x = int(time.time())
x -= 60 * 60 *24
#x += 2208988800
timenow = struct.pack('I', x)
print timenow
print repr(timenow)
print time.ctime(int(x))