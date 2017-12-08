# -*- coding:utf-8 -*-
a = '你好好啊！'
for i in a.decode('utf-8'):
    if i == '你'.decode('utf-8'):
        print 'yes'
    else:
        print 'no'