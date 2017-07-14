'''
Created on 2017.6.28

@author: Administrator
'''
from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died.  You kinda suck at this.",
             "Your mom would be proud. If she were smarter.",
             "Such a luser.",
             "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print "\n--------"
            room = getattr(self, next)
            print "room:",room
            next = room()
            print next
    def a_a(self):
        print "a" 
        return 'b_b'
    
    def b_b(self):
        print "b"       
            
a_game = Game('a_a')
a_game.play()            