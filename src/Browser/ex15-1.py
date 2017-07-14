people = 30
cars =20
buses = 25

if cars > people and cars > buses:
    print "We should take the cars"
    
elif cars < people and cars < buses:
    print "We should not take the cars"
    
else:
    print "We can't decide"    
    
    
if buses > cars:
    print "That's too many buses"
    
elif buses < cars:
    print "Maybe we can take the cars"
    
else:
    print "We still can't decide"   
    
if people > buses:
    print "Alright, let's just take the buses" 
    
else:
    print "Fine, let's stay home then"       