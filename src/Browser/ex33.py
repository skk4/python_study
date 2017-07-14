'''
Created on 2017.6.29

@author: Administrator
'''
class Room(object):
    


    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}



    def add_paths(self, paths):
        self.paths.update(paths)
        return self.paths
        

    def go(self, direction):
        return self.paths.get(direction, None)
center = Room("Center","Test room in the center")
north = Room("North", "Test room in the north.")
south = Room("South", "Test room in the south.")       
print Room("Center","Test room in the center").add_paths({'north': north, 'south': south}).go('north')
print Room("Center","Test room in the center").go('north')
    