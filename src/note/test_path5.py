# -*- coding:gbk -*-
import os
def search(path, keyword):
    os.chdir(path)
    files = os.listdir(os.curdir)
    files_list = []
    for each_file in files:
        #��ǰ��ַΪpath
        
        file_type = os.path.splitext(each_file)[1]
        #print file_type
        if file_type in search_target:
            #print each_file                                       
            #target_file =os.getcwd()+ os.sep + each_file
            #print target_file
            #target_list.append(target_file) 
            #target_list
            #print target_list
            files_list.append(each_file)

            
        if os.path.isdir(each_file):
            
            search(each_file) 
            #ִ����searchΪ��ǰ��ַ����һ���������践�ص���һ��
            os.chdir(os.pardir) 
              

    #print files_list
    decide = raw_input("�Ƿ���Ҫ��ӡ��%s�����ļ��еľ���λ�� YES/NO:" %keyword)
    decides = ['Yes', 'YES', 'yes']
    if decide in decides:
        
    
        for filelist in files_list:
            f = open(filelist, 'r')
            count = 0
            for each_line in f:
                count = count + 1
                if keyword in each_line:
                    print '�ļ�����%s,������%d,λ�ã�%d' %(filelist, count, each_line.find(keyword)+ 1)


keyword = raw_input("������ؼ��֣�")
search_target = ['.txt']
path = os.curdir
#target = raw_input("��������Ҫ���ҵ�Ŀ���ļ���")
search(path, keyword)
