'''
Created on 2017.7.4

@author: Administrator
'''
class MufCalc(object):
    m = False
    def calc(self, exp):
        try:
            return eval(exp)
        except ZeroDivisionError:
            if self.m :
                print "cool"
            else:
                raise
app = MufCalc()
app.calc(2/0)            