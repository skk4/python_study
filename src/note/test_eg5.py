# -*- coding:utf-8 -*-
import os
import easygui as g 

def show_result():
    text = ''
    total = 0
    lines = 0
    for file_type in source_dict:
        lines = source_dict[file_type]
        total += lines 
        text += '[%s]源代码%d个，源代码%d行\n' %(file_type, filetype_dict[file_type], lines)
    title = '统计结果'
    msg='您 目前共累计编写%d行代码，完成进度：%.2f%%\n离10万行还差%d，请继承努力！' %(total, total/1000, 100000-total)
    g.textbox(msg=msg, title=title, text=text)    
         


def codecalc(file_name):
    count = 0
    f = open(file_name, 'r')
    for each_line in f:
        if each_line != '\n':
            count += 1
           
    f.close       
    return count       


def searchfile(dir_path):
    os.chdir(dir_path)
#print os.getcwd()

    allfiles = os.listdir(os.curdir)
    for file_name in allfiles:
        if os.path.isdir(file_name):
            searchfile(file_name)
            os.chdir(os.pardir)


        else:

            #if file_name == 'setup.py':

            file_type = os.path.splitext(file_name)[1]
            if file_type in code_type:
               
                count = codecalc(file_name)
                source_dict.setdefault(file_type, 0)
                source_dict[file_type] += count
               

               
               

                #full_file_name = os.getcwd()+ os.sep+ file_name
                #countlist.append(full_file_name)

                filetype_dict.setdefault(file_type, 0)
                filetype_dict[file_type] += 1

source_dict = {}
filetype_dict ={}
code_type = ['.py', '.java']
#dir_path = '/Users/apple'
#dir_path='/Users/apple/Documents/workspace'
g.msgbox(msg='请打开所有存放代码的文件夹', title='代码统计')
dir_path = g.diropenbox('请选择代码库')
#dir_path = 'D:\\je_workspace'
searchfile(dir_path)
print 'source_dict', source_dict
print 'filetype_dict', filetype_dict
show_result()
#file_name = 'ex_path.py'
