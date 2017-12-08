# -*- coding:utf-8 -*-
#sum(['iloveyou','kevin'])

def sum(x):
    sum_result = 0
    for each in x:
        if isinstance(each, int)or isinstance(each, float):
            sum_result = sum_result + each                            
        else:
            continue
        
    return sum_result 
        
