'''
Created on 2017.6.27.

@author: Administrator
'''
with open("D:/a.txt") as file:  
    data = file.read()
    print data
    
    
'''
finally不管try子句内部是否有异常发生，都会执行finally子句内的代码。
所有一般情况下，finally自己常常用于关闭文件或者在Socket中。  
'''  
file = open("D:/b.txt")  
try:  
    data2 = file.read()
    print "data2:\n",data2  
finally:  
    file.close()    
    
    
file = open("D:/a.txt")
data3 = file.read() 
print "data3:\n",data3      