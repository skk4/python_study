# -*- coding:gbk -*-

def replace_file(file_name, old, new):
    f1 = open(file_name, 'r')
    count = 0
    content = []
    for each_line in f1:
        count = count + each_line.count(old)
        #print count
        each_line = each_line.replace(old, new)
        #each_line = each_line.replace('л�м�', 'С����')
        content.append(each_line)
    f1.close()  
    print '''�ļ�%s�й���%d����%s��
��ȷ��Ҫ�����еġ�%s���滻�ɡ�%s����''' %(file_name, count, old, old, new)                            
    
    decide = raw_input("YES/NO:")
    
    if decide == 'YES':                         
        f2 = open(file_name, 'w')
        f2.writelines(content)
        f2.close()
 
 
file_name = raw_input("�ļ�����")
old = raw_input("���滻�����֣�")
new = raw_input("�滻�ɣ�")
     
replace_file(file_name, old, new)    