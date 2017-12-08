class Ticket:
    ticket = 100
    def day(self):
        return self.ticket
    
    def weekend(self):
        return self.ticket*1.2
    
    def children(self):
        return self.ticket/2
    
    def childrenweekend(self):
        return self.ticket*1.2/2
        
        
    
    
t = Ticket()
print t.day()
print t.weekend()
print t.children()  
print t.childrenweekend()  