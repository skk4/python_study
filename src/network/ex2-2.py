# -*- coding:utf-8 -*-
'''
Created on 2017.7.12

@author: Administrator
'''
import commands
status, output = commands.getstatusoutput("ipconfig")

print status
print output