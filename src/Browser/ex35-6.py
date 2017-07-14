'''
Created on 2017.7.4

@author: Administrator
'''

'''
a = 10
b = 0
c = a/b 
print c
'''

a = 10
b = 0
try:
    c = a/b 
    print c  
except Exception, e:
    print e.message
    print '1'
    
print 'done'   



 