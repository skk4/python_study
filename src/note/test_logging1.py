# -*- coding:utf-8 -*-
import logging
#获取日志实例，如果参数为空，则返回root logger
myloggerx = logging.getLogger('logging_app')
#指定logger输入格式
formatter = logging.Formatter('%(name)-12s: %(asctime)s, %(levelno)s, %(filename)s, \
%(funcName)s, %(threadName)s, %(message)s')
#文件日志
file_handler = logging.FileHandler('D:\\python_save_path\\foo2.log')
file_handler.setFormatter(formatter)
#控制台日志
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
#指定日志初始最低等级
myloggerx.setLevel(logging.INFO)
#添加日志处理器
myloggerx.addHandler(file_handler)
myloggerx.addHandler(console_handler)


i=10
def foo():
    global i 
    while i:
        i = i-1
        
        myloggerx.info('hello number %s' %i)
        
        

def foo2():
    try:
        1/0
    except:
        myloggerx.exception('this is error message!')
        
        
foo() 
foo2()         