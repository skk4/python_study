class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *=(1.0+percent)
        
bob = Worker('Bob Smith', 60000)
print bob.lastName()
bob.giveRaise(0.5)
print bob.pay        
                
                