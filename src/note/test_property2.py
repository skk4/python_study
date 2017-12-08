# -*- coding:utf-8 -*-
import time
class Record(object):

    def __init__(self, name, b):
        self._name = name
        self.b = b
        self.time = ''

    def __get__(self, instance, owner ):
        self.time = time.ctime(time.time())
        getline = '%s,变量于北京时间  %s 被读取，%s = %s' % (self.b, self.time, self.b, self._name)
        with open('d:\\xrecord.txt', 'a') as f:
            f.write(getline+'\n')
        return self._name

    def __set__(self, instance, value):
        self.time = time.ctime(time.time())
        setline = '%s,变量于北京时间  %s 被修改 ，%s = %s' % (self.b, self.time, self.b, value)
        self._name = value
        with open('d:\\xrecord.txt', 'a') as f:
            f.write(setline + '\n')


    def __delete__(self, instance):
        print 'Deleting :%s' % self._name
        del self._name


class Test(object):
    x = Record(10, 'x')
    y = Record(8.8, 'y')


test = Test()
test.x
time.sleep(3)
test.x = 9
time.sleep(3)
test.x
time.sleep(3)
test.y
time.sleep(3)
test.y = 7.22
time.sleep(3)
test.y
test.x = 'xieshangji'
time.sleep(3)
test.x
