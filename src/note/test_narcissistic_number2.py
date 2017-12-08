# -*- coding:utf-8 -*-
'''  
把数字转换为字符串，然后拆分成各个数字，然后立方相加
'''
def narcissisticnumber(n,around): 

    for num in range((10**around)/10,10**around):
        
        numtostr = str(num)
        numlist = []
        for i in range(around):
            numdiv = int(numtostr[i])
            numlist.append(numdiv**n)
            sum_numdiv = sum(numlist)  
        if num == sum_numdiv:
            return sum_numdiv  
        
print narcissisticnumber(4, 4)         
                        