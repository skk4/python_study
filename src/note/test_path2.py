# -*- coding:utf-8 -*-
'''
创建一个简单的搜索引擎：用户输入文件以及开始搜索的路径，搜索文件是否存在。
如遇到文件夹，则进入文件夹继续搜索
如：请输入待查找的初始目录：E:\\TestFolder
       请输入需要查找的目标文件：测试3.txt

'''

import os
def search(path, target):
    os.chdir(path)
    files = os.listdir(os.curdir)

    for each_file in files:
        #当前地址为path
        if each_file == target:
            print os.getcwd()+ os.sep + each_file
            
        if os.path.isdir(each_file):
            
            search(each_file, target) 
            #执行完search为当前地址的下一级，所以需返回到上一级
            os.chdir(os.pardir) 


path = raw_input("请输入待检查的初始目录：")
target = raw_input("请输入需要查找的目标文件：")
search(path, target)
'''
返回结果：
请输入待检查的初始目录：d:\\python
请输入需要查找的目标文件：setup.py
d:\python\distribute-0.7.3\setup.py
d:\python\Django-1.11.3\setup.py
d:\python\nose-1.3.7\examples\html_plu
'''
