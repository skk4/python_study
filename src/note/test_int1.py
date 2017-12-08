# -*- coding:utf-8 -*-
class Nint(int):
    def __new__(cls, string): 
        sumasc = 0     
        if isinstance(string, str):
            for each in string:
                ascnum = ord(each)
                sumasc = sumasc + ascnum
            return sumasc        
                
        else:
            return int.__new__(cls, string)
               
 
 
print Nint('FishC')                                               