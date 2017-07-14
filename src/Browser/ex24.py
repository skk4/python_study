'''
Created on 2017.6.27

@author: Administrator
'''
'''
mylist = [1, 2, 3]
for i in mylist:
    print i

'''

'''
for x in range(3):
    print x
'''

'''
mylist2 = [x*x for x in range(5)]
print mylist2

mylist3 =[1 for x in range(5)]
print mylist3

words = "congratuation"
mylist4 =[x*2 for x in words]
print mylist4

'''

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
        
mygen = createGenerator()
print mygen

for i in mygen:
    print i
        

