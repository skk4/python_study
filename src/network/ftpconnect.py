# -*- coding:utf-8 -*-
'''
Created on 2017年7月25日

@author: Administrator
'''
import ftplib
from ftplib import FTP
def writeline(data):
    fd.write(data+'\n')
    
f = FTP('ftp.ibiblio.org')
print 'welcome:', f.getwelcome()
f.login()
print 'CWD:', f.cwd('/pub/docs')
print 'pwd:',f.pwd()
fd = open('README','wt')
f.retrlines('RETR README', writeline)
f.quit()