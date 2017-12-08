# -*- coding:utf-8 -*-
'''
解题思路：
 正整数转成二进制。要点一定一定要记住哈：除二取余，然后倒序排列，高位补零。
'''
def b(num):
    blist=[]
    while 1:
        s = num%2
        temp = num/2
        num= temp
        blist.append(str(s))
        if num == 0:
            blist.reverse()
            break
    b=''.join(blist)
    return b  
print b(42)