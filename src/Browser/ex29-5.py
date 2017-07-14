'''
Created on 2017.6.29

@author: Administrator
'''
'''
class test(object):
    name = 'shangji'
    def run(self):
        return "hello"
t = test()
print getattr(t, "name")

print getattr(t, "run")()

from sys import exit
from random import randint
'''
class GameMap(object):

    def __init__(self, start):
        self.quips = [
            "You died.  You kinda suck at this.",
             "Your mom would be proud. If she were smarter.",
             "Such a luser.",
             "I have a small puppy that's better at this."
        ]
        self.start = start

    def a_a(self):
        print "a" 
        return 'b_b'
    
    def b_b(self):
        print "b"       
            