# -*- coding:gbk -*-
def compa(name1, name2):
    f1 = open(name1, 'r')
    f2 = open(name2, 'r')
    num_list = []   
    count = 0
    for line1 in f1:
        line2 = f2.readline()
        count = count + 1
        if line1 != line2:            
            num_list.append(count)
    f1.close()
    f2.close()        
    return num_list    

           
num_list = compa('some.txt', 'someone.txt')
total_num = len(num_list)
print '����%d��ͬ' % total_num 
for i in num_list:
    
    print '��%d�в�һ��' % i     
    
'''
���ؽ����
����4��ͬ
��1�в�һ��
��3�в�һ��
��6�в�һ��
��9�в�һ��
'''      