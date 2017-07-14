'''
Created on 2017.6.28

@author: Administrator
'''

ten_things = "Apples Oranges Crows Telephone Light Sugar"
for i in ten_things:
    print i

print "Wait there is not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

print more_stuff

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one
    stuff.append(next_one)
    print "There's %d items now" % len(stuff)
    
print "There we go :", stuff


print "let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])    
