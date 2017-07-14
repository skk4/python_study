'''
Created on 2017.6.30

@author: Administrator
'''

class R(object):
    def __init__(self):
        self.dict = {}
    def R_R(self):
        print R_R


y = R()
a_dict = {}
print a_dict.get('x')

b_dict = {'x': y}

a_dict.update(b_dict)
print R()
print a_dict
print a_dict.get('x', None)


