# -*- coding:utf-8 -*-

def findstr(input_string, sub_str):
    length = len(input_string)
    count = 0
    for i in range(length-2):
        eachdivstr = input_string[i]+input_string[i+1]
        if eachdivstr == sub_str:
            count = count+1
    return count   

input_string = raw_input("string>:")
sub_str = raw_input("sub_str>:") 
print '%s 中含有 %s个数为：%d' %(input_string, sub_str, findstr(input_string, sub_str))