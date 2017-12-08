# -*- coding:utf-8 -*-
'''
Created on 2017年7月20日

@author: Administrator
'''
import sys, urllib2, getpass
class TerminalPassword(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        retval = urllib2.HTTPPasswordMgr.find_user_password(self, realm, authuri)    