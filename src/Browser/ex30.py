'''
Created on 2017.6.29

@author: Administrator
'''
class GoldRoom(object):
    
    def __init__(self, start):
        self.start = start
        
    def dead(self):
        print "you are dead"
        exit(0)
        
    def go(self):
        if self.start == 'left':
            return "left"
                  
b = GoldRoom('left')
b.dead()
print b.go()       