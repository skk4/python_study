# -*- coding:utf-8 -*-
'''
要求搜索当前所有文件夹下面，规定后缀的文件
用户输入开始搜索路径下（包含子文件夹）所有视频格式的文件（要求查找mp4，rmvb，avi格式文件）
并创建一个videoList.txt文件，存放所有找到的文件的路径

'''

import os
def search(path):
    os.chdir(path)
    files = os.listdir(os.curdir)
    for each_file in files:
        #当前地址为path
        
        file_type = os.path.splitext(each_file)[1]
        #print file_type
        if file_type in search_target:
            #print each_file
        
        #if each_file == target:
            
            target_file =os.getcwd()+ os.sep + each_file
            target_list.append(target_file) 
            target_list

            
        if os.path.isdir(each_file):
            
            search(each_file) 
            #执行完search为当前地址的下一级，所以需返回到上一级
            os.chdir(os.pardir) 
              

search_target = ['.avi', '.rmvb', '.mp4']
path = raw_input("请输入待检查的初始目录：").decode('utf-8')
#target = raw_input("请输入需要查找的目标文件：")
target_list = []
search(path)
file_name = path + os.sep+'\\videoList.txt' 
#print target_list
#print file_name


f = open(file_name, 'w')
for i in target_list:
    f.writelines(i+'\n')
    
f.close() 
print '搜索结束！' 
'''
请输入待检查的初始目录：d:\\test
搜索结束！

'''
