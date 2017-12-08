# -*- coding:utf-8 -*-
import os
#path = os.getcwd()
file_names = os.listdir('.')

#print file_names
length = len(file_names)
#print length
filename_list = []
filename_dict = {}

nametyp_list = []
for each_file in file_names:
    filesize = os.path.getsize(each_file)
    print each_file,':',filesize, 'bytes'
    file_name, file_type = os.path.splitext(each_file)

    if file_type == '':
        filename_list.append(file_name)
        #print '文件夹：%d个'  %len(filename_list)
       
    else:
        nametype = os.path.splitext(each_file)[1]
        filename_dict.setdefault(nametype, 0)
        filename_dict[nametype] = filename_dict[nametype] + 1
       
print '文件夹：%d个'  %len(filename_list)       
#print filename_dict
for key, value in filename_dict.items():
    print key ,':', value,'个'
#print filename_dict.items()
'''返回结果：
文件夹：2个
.html : 3 个
.mp3 : 1 个
.pyc : 2 个
.py : 43 个
.txt : 2 个
'''
  
