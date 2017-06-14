#-*-coding=utf-8-*-
class A():
    cls_i=0
    cls_j={}
    def __init__(self):
        self.instance_i=0
        self.instance_j={}
a=A()
print a.__dict__
print A.__dict__
a.cls_i =0
a.instance_i=0
print a.__dict__
print A.__dict__
A.cls_i=1
print a.__dict__
print A.__dict__