#-*- coding:gbk -*-
def file_seek(filename, filerow):
    f = open(filename, 'r')
    for i in range(filerow):
        print f.readline()
    f.close()   
file_seek('some.txt', 10)