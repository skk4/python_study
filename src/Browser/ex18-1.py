'''
Created on 2017.6.23

@author: Administrator
'''
def number_append(number, j):
    number_list = []
    unm = ''
    i = 0
    while i < number:
        print "At the top i is %d" %i
        number_list.append(i)
        i = i+j
        
    for num in number_list:
       print unm
       
number_append(6, 3)       