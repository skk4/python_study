'''
Created on 2017.6.27.

@author: Administrator
'''
with open("D:/a.txt") as file:  
    data = file.read()
    print data
    
    
'''
finally����try�Ӿ��ڲ��Ƿ����쳣����������ִ��finally�Ӿ��ڵĴ��롣
����һ������£�finally�Լ��������ڹر��ļ�������Socket�С�  
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