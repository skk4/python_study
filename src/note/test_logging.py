# -*- coding:utf-8 -*-
import sys
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s, %(levelno)s, %(filename)s, \
%(funcName)s, %(threadName)s, %(message)s', datefmt='[%d/%b/%Y %H:%M:%S]',
filename=r'D:\\python_save_path\\foo.log')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

i=10
def foo():
    global i 
    while i:
        i = i-1
        
        logging.info('hello number %s' %i)
        
        
foo()        