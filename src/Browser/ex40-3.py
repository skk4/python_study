'''
Created on 2017.7.10

@author: Administrator
'''
a_list  = [{'test01':('type', 'id=>kw')}, {'test01':('search', 'id=>su')},{'test02':('type', 'id=>do')}]
print len(a_list)
print a_list[1]['test01'][0]
j = len(a_list)
i = 0
while i < j:
    i = i+1
    print a_list[i-1]
    

'''
a_dict = {'test01':[('type', 'id=>kw'), ('search', 'id=>su')], 'test02':[('type', 'id=>do')]}
print len(a_dict)
print a_dict['test01'][0][0]
'''