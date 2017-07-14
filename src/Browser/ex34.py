'''
Created on 2017.6.29

@author: Administrator
'''
from Browser.ex33 import Room
from nose.tools import *
'''
def test_room():
    gold = Room("GoldRoom", 
                """This room has gold in it you can grab. There's a
                door to the north.""")
    print gold.name
    print gold.paths
    print gold.description
    
def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    print center.add_paths({'north': north, 'south': south})
    print center
    
test_room_paths()    
'''

def test_room():
    gold = Room("GoldRoom", 
                """This room has gold in it you can grab. There's a
                door to the north.""")
    #assert_equal(gold.name, "GoldRoom")
    #assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    center.go('north')
    #assert_equal(center.go('north'), north)
    #assert_equal(center.go('south'), south)
    
def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    print start.go('west').go('east')

    #assert_equal(start.go('west'), west)
    #assert_equal(start.go('west').go('east'), start)
    #assert_equal(start.go('down').go('up'), start)
    
test_map()    