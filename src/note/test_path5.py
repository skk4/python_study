# -*- coding:gbk -*-
import os
def search(path, keyword):
    os.chdir(path)
    files = os.listdir(os.curdir)
    files_list = []
    for each_file in files:
        #当前地址为path
        
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
            #执行完search为当前地址的下一级，所以需返回到上一级
            os.chdir(os.pardir) 
              

    #print files_list
    decide = raw_input("是否需要打印【%s】在文件中的具体位置 YES/NO:" %keyword)
    decides = ['Yes', 'YES', 'yes']
    if decide in decides:
        
    
        for filelist in files_list:
            f = open(filelist, 'r')
            count = 0
            for each_line in f:
                count = count + 1
                if keyword in each_line:
                    print '文件名：%s,行数：%d,位置：%d' %(filelist, count, each_line.find(keyword)+ 1)


keyword = raw_input("请输入关键字：")
search_target = ['.txt']
path = os.curdir
#target = raw_input("请输入需要查找的目标文件：")
search(path, keyword)
