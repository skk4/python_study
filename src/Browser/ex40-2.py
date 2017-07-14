'''
Created on 2017.7.10

@author: Administrator
'''
#a_dict = {'1': 'x', '2':'y', '3':'z'}
#print len(a_dict)
#print a_dict['2']
#key_list = a_dict.keys()
#print key_list
def get_key(dict_data, value):
    key_list = dict_data.keys()
    for i in range(len(dict_data)):
        if dict_data[key_list[i]] == value:
            key = key_list[i]
            
            
    return key    

print get_key({'id':'p', 'cd':'x', 'pd':'z'}, 'x')    