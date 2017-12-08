#help(zip)
print zip([1,2,3,4],[5,6,7],[8,9])
#[(1, 5, 8), (2, 6, 9)]

print [x**2 for x in range(10)]  
print map((lambda x: x**2), range(10)) 


f = lambda x,y: x**2*y
print f(5,6)

l = [(lambda x: x**2),  
    (lambda x: x**3),  
    (lambda x: x**4)]  
print l[0](2),l[1](2),l[2](2) 

d = {'f1':(lambda: 2+3),  
    'f2':(lambda: 2*3),  
    'f3':(lambda: 2**3)}  
print d['f1'](), d['f2'](), d['f3']() 




 
