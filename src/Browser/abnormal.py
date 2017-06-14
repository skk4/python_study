# conding=utf-8 -*-
a= 'ok'
b='false'
try:
    open("a.txt",'r')
    print a
except BaseException,m:
    print m