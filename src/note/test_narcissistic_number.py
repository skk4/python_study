# -*- coding:utf-8 -*-
'''
水仙花数：153 即 1^3 + 5^3 + 3^3 = 153 
迭代方式解题思路：
153%10 余 3
153/10 商15
15%10  余5
15/10  商1
1%10   余 1
1/10   商 0    

'''

def narcissisticnumber(mi, around):
    for n in range((10**around)/10,10**around):
        temp = n
        result = 0 
        while n:          
            m = n%10
            n = n/10
            result =result + m**mi
        if result == temp:
            print temp


narcissisticnumber(3, 3)