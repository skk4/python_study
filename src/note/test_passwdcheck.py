# -*- coding:utf-8 -*-
#密码安全性检查代码
#低级密码要求:
#1.密码由单纯的数字或字母组成
#2.密码长度小于等于8位
#中级密码要求:
#1.密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）
#2.任意两种组合
#3密码长度不能低于8位
#高级密码要求:
#1.密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）
#2.必须三种组合
#3.密码只能由字母开头密码长度不能低于16位
chars = 'abcdefghijklmnopqrstuvwxyz'
symbols = r'''~!@#$%^&*()_+{}|[]\:";'<>?,./"'''
nums ='1234567890'

passwd = ''
length = 0

#输入为空格，没有字符情况，实现重新输入
while passwd.isspace() or length == 0:
    passwd = raw_input(">")
    length = len(passwd)
    continue

'''***密码长度判断，分为三个等级length_flag :
1:为密码长度小于等于8(length<8)
2:为密码小于16大于8(8<length<16)
3：为密码大于 等于16(length>=16)
'''
length_flag = 0
if length <= 8:
    length_flag = 1
    
elif 8 < length < 16:
    length_flag = 2
else:
    length_flag = 3    

'''***密码字符类型，也分为三个等级element_flag：
1:为密码中只有单一数字、子母、符号
2：为密码中有数字、字母、符号中任意2种元素
3：包含三中数字、字母、符号元素
三个for语句，element_flag为递加关系，
密码中只有单一种类元素，element_flag最终结果为1
密码中包含2类元素，element_flag最终结果为2
3个都满足则返回3
'''
element_flag = 0
#第一个元素包含字母，length_flag标为1 
for _element in passwd:   
    if _element in chars:
        element_flag += 1
        break
#元素包含符号，length_flag在前面的基础上再加上1    
for _element in passwd:
    if _element in symbols:
        element_flag += 1
        break
#元素包含符号，length_flag在前面的2个层次的基础上再加上1    
for _element in passwd:
    if _element in nums:
        element_flag += 1 
        break   
#首个密码为字母标记
startchar_flag =0
if passwd[0] in chars:
    startchar_flag = 1

#密码长度和密码元素只要满足一个条件即被降到对应的等级    
if element_flag == 1 or length_flag == 1:
    print '低级密码'
    
elif element_flag == 2 or length_flag == 2:  
    print '中级密码'   
    
else:
    #满足长度和元素组成前提下，再判断是否首个密码为字母
    if startchar_flag == 1:
        print '高级密码'
        
    else:
        print '中级密码'
