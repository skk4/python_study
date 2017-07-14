'''
Created on 2017.7.3

@author: Administrator
'''

setence = raw_input(">")
print setence.split(' ')
words_list = setence.split(' ')
word_pool = ('go', 'kill', 'do')
try:
    for word in words_list:
        if word.lower()in word_pool:
            print 'a'
        
        else:
            print 'b'
        
except ValueError:
    print 'c'        
             
    
    
