'''
Created on 2017.7.18

@author: Administrator
'''
#windwos系统上无法使用fork()方法，windows程序员用多线程编程技术来完成并发任务
import sys, time
print "loli"
print os.getpid()
pid = os.fork()
print "lolita"
if pid != 0:
#    print "old pid",os.getpid()
    sys.exit(0)
#    os._exit(0)
print os.getpid()

'''
loli
2571
lolita
[root@localhost python]# lolita
2572
'''
#!usr/bin/python
import syslog
try:
    
    f = file(r'/root/test.py')
except IOError, e:
    syslog.syslog(syslog.LOG_ERR, "%s" % e)
else:
    syslog.syslog(syslog.LOG_INFO, "no exception caught\n")
finally:
    f.close()