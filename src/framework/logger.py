#-*- coding:utf-8 -*-
import logging
import os.path
import time

class Logger(object):
    def __init__(self, logger):
        '''
        #制定保存文件的路径，日志级别，以及调用文件
        #将制定格式的日志，存入到文件中
        '''
        
        
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        
        #创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        #log_path = os.path.dirname(os.getcwd())+'/logs/' #项目根目录下/logs保存日志
        #如果case组织结构是 /testsuit/featuremodel/xxx.py,那么得到的相对路径的父路径就是项目根目录
        log_path = os.path.dirname(os.path.abspath('.'))+'/logs/' 
        log_name = log_path + rq +'.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        
        #再创建一个handler，用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        #用于定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger