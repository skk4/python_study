# -*- coding:utf-8 -*-
import logging


def my_logger(log_obj):
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')
    
    #################################################################################################
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    #################################################################################################
    
    logging.debug('This is debug message %s' %log_obj)
    logging.info('This is info message %s' %log_obj)
    logging.warning('This is warning message %s' %log_obj)
 
if __name__ == '__main__':
    a = '1115.16平米'.strip('平米')
    my_logger(a)
    
    