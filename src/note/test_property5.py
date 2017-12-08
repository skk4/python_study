# -*- coding:utf-8 -*-
class Descriptor(object):
    
    def __init__(self):
        self._name = ''
        
    def __get__(self, instance, owner ):
        print 'Getting: %s' % self._name
        return self._name
    
    def __set__(self, instance, value):
        print 'Setting :%s' % value
        self._name = value.title()
        
        
    def __delete__(self, instance): 
        print 'Deleting :%s' % self._name
        del self._name 
        
        
class Person(object):
    name = Descriptor()
    
user = Person()

user.name = 'xie shangji'

user.name

del user.name


class Person2(object):
    def __init__(self):
        self._name = ''
        
    def fget(self):
        print 'Getting: %s' % self._name
        
        return  self._name 
    
    
    def fset(self, value):
        
        print 'Setting %s'% value
        self._name = value.title() 
        
        
    def fdel(self):
        print 'Deleting %s' % self._name
        del self._name
        
        
        
    name = property(fget, fset, fdel) 
    
    
user2 = Person2()
user2.name = 'xie shangji'
user2.name 
del user2.name         


class Person3(object):
    
    def __init__(self):
        self._name = ''
        
    @property
    def name(self):
        print 'Getting :%s' % self._name
        return self._name
    @name.setter    
    def name(self, value):
        print 'Setting :%s' % value
        self._name = value.title()
        
    @name.deleter
    def name(self):
        print 'Deleting: %s' %self._name 
        del self._name      

user3 = Person3 
user3.name = 'xie shangji'
user3.name
del user3.name           
                  