# -*- coding:utf-8 -*-
class FileObject():
    
    def __init__(self, filename):
        self.filename = filename
        self.f = open(self.filename, 'r')
        print '打开文件'
    
    def __del__(self):
        self.f.close()
        del self.f
        print '关闭文件'
        
        
a = FileObject('some.txt')  

del a      