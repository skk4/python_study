'''
Created on 2017.6.29

@author: Administrator

'''

from Browser.ex32 import GameMap
class Engine(object):
    def __init__(self, start):
        self.start = start
    
    def play(self):
        GameMap('b').a_a()
        
    
a_e = Engine('a')  
a_e.play()        