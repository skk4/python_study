# -*- coding:utf-8 -*-
e = iter(range(5))
while 1:
    try:
        each = next(e)
        print each
    except StopIteration:
            
        break
            
    
    