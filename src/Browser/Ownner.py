class Ownner():
    usename = 'xiesj'
    password = '123456'
    
    def next(self):
         return Ownner.password
     
     
x=Ownner()
y=x.next()
print y
