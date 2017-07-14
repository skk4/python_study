# -*- coding:utf-8 -*-
'''
Created on 2017.6.27

@author: Administrator
'''
# -- coding: utf-8 --

def ThorwErr():
    raise Exception("抛出一个异常")
    print "bbb"


print "aaa"

# Exception: 抛出一个异常
ThorwErr()