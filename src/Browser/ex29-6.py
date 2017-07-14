'''
Created on 2017.6.29

@author: Administrator
'''
class Game(object):
    def __init__(self, start):
        print self        
        self.start = start
    
 #play方法其实就是游戏引擎   
    def play(self):
        
        next = self.start
        print self
        print "\n--------"
        room = getattr(self, next,'18')
        next = room()
        
        
    def a(self):
        print "a"     
        
        
'''
        while True:
            print self
            print "\n--------"
            room = getattr(self, next,'18')
            next = room()
'''           
       
a_game = Game("a")
print a_game
a_game.play()