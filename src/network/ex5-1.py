# -*- coding:utf-8 -*-
'''
Created on 2017.7.12

@author: Administrator
'''
'''
import sys
sys.stdout.write("abc\n")
sys.stdout.write("efg\n")
'''
# coding=utf-8
import sys, os
import time
for i in range( 100 ):
    time.sleep( 0.5 )
    sys.stdout.write( "File transfer progress :[%3d] percent complete!\r" % i )
    sys.stdout.flush()