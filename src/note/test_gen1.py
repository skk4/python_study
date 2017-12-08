class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def fibs(self):
        while 1:
            self.c = self.a + self.b 
            yield self.b
            self.a = self.b
            self.b = self.c 
        
f = Fibs()
print type(f)
print type(f.fibs())
count = 0
for i in f.fibs():
    if count >= 12:break
    print i
    count = count + 1            