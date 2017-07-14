'''
Created on 2017.6.28

@author: Administrator
'''

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 
          'FL': 'Jacksonville' }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

if 'MI' in cities:
    print 'yes'
else:
    print "no"
'''
print cities
print cities.items()[1][1]
print cities.keys()

state = 'NY'

if state in cities.keys():
    print 'yes'
    
else:
    print "no"
'''    
#print ' '.join(cities.keys())


#print cities['NY']
#def find_city():
    

'''
def find_city(state):
    print cities[state]
    
while True:
    
    try:
        
        state = raw_input(">")

        find_city(state)
        
    except Exception, e:
        print e.message
        print "Not Found"

    
'''    

'''
def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# ok pay attention!
print find_city(cities, 'NY')
'''
'''
cities['_find'] = find_city

print find_city

while True:
    print "State? (ENTER to quit)",
    state = raw_input("> ")

    if not state: break

    # this line is the most important ever! study!
    city_found = cities['_find'](cities, state)
    print city_found

'''
'''
state = 'NY'
if state in cities[state]:
    print "ok"
else:
    print "not in"
'''    
