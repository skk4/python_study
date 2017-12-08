'''
Created on 2017.7.20

@author: Administrator
'''
import sys
a_dict = {'Date': 'Thu, 20 Jul 2017 09:11:10 GMT','Content-Type': 'text/html; charset=utf-8','Transfer-Encoding': 'chunked','Connection': 'Close','Vary': 'Accept-Encoding'}
print "a_dict:\n", a_dict
#sys.stdout.write(str(a_dict))
print"aaaaaa", a_dict.keys()
'''
print a_dict.items()
for key , value in a_dict.items():
    print "%s : %s" %(key, value)
    
for a_list in a_dict.items():
    print a_list    
    
    '''