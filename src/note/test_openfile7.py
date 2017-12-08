# -*- coding:utf-8 -*-
'''
接收用户输入并保存为新的文件
'''
def work(file):
    f = open(file, 'w')
    print "请输入内容【单独输入':w'保存退出】："
    while 1:
        input_setences = raw_input()
        
        if input_setences != ':w':
            f.write(input_setences.decode('utf-8','ignore').encode('gb2312') +'\n')
            
        else:
            break       
    
    f.close()
    
file_name = raw_input("请输入文件名：")

work(file_name)