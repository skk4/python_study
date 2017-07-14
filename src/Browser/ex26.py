'''
Created on 2017.6.28

@author: Administrator
'''
def start():
    print "start......"
    next = raw_input(">")
    
    if next == "left":
        bear_room()
         
    elif next == "right":
        cthulhu_room()
        
    else:
        dead("middle dead")
    
def gold_room():
    print "enter gold_room"
    next = raw_input(">")
    
    if next.isdigit():
        how_much = int(next)
        
    else:
        print "type a number"
        
    if how_much <50:
        print "success"
        exit(0)
            
    else:
        dead("you dead")
        
        
def dead(why):
    print "good job!",why
    exit(0)
    
def cthulhu_room():
    
    next = raw_input(">")
    if next == "flee":
        start()
        
    elif next == "head":
        dead("head")
        
    else:
        cthulhu_room()
        
        
            

def bear_room():
    
    
    bear_moved = False
    
    while True:
        next = raw_input(">")
    
        if next == "take honey":
            dead("honey")
        elif next == "taunt bear" and not bear_moved:
            print "go ahead"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("taunt bear again to be eat")
        
        elif next == "open door" and bear_moved:
            
            gold_room()
        
        else:
            print "again"
        
        
    
start()            
        
    
    
    