'''
Created on 2017.7.4

@author: Administrator
'''


while True:
    input_a = raw_input("a>")

    
    if input_a.isdigit() == True:
        print 'digit'
        break
    else:
        print 'str'
 
while True:
    input_b = raw_input("b>")
    
    if input_b.isdigit() == True:        
        print 'digit'
        break
    else:
        print 'str'
               

try:
    c = int(input_a)/int(input_b) 
    if int(c) < 1:
        raise
    else:
        print c
except TypeError:
    print 'a'
    
print int(c)*int(c)    

        
'''
input_b = raw_input("b>")

c = a/b

if
'''

a_list = [('a', 'abc'), ('b', 'bcd')]
word_list = a_list.pop(0)
print word_list