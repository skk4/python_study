# -*- coding:utf-8 -*-
import time


class LeapYear(object):
    
    def __init__(self):
        self.year = int(time.localtime()[0])+1
    
    def __iter__(self):
        
        return self
    
    def next(self):
        self.year = self.year - 1
        if self.year % 4 == 0 and self.year %100 != 0:
            return self.year
                            

l = LeapYear()            
for e in l:
    if e >=2000:
        
        print e
