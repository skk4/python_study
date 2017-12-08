# -*- coding:utf-8 -*-
import os

def searchfile(dir_path):
    os.chdir(dir_path)

    allfiles = os.listdir(dir_path)
    for file_name in allfiles:
        if os.path.isdir(file_name)!= 1:
            if os.path.splitext(file_name)[1] == '.py':
                print file_name
        
        
        else:
            print file_name
            searchfile(file_name)
            os.chdir(os.pardir)
        
        
dir_path = 'D:\\je_workspace'
searchfile(dir_path)
print 'over！'


