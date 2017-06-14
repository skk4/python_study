class speaker():
    topic=''
    name=''
    def __init__(self,n,t):
        self.Name=n 
        self.Topic=t 
    def speak(self):
        print ("I am %s,I am a speaker!My topic is %s" %(self.Name,self.Topic))   
x=speaker("mike","tiger").speak()
print x

class sample(speaker):
    a=''
    def __init__(self,n,t,a):
        speaker.__init__(self, n, t)
        self.Article=a 
    def article(self):
        print ("I am %s,I am a speaker!My topic is %s,my landwge is %s!" %(self.Name,self.Topic,self.Article))        
y=sample("lincon","fruit","english").article()  
print y      