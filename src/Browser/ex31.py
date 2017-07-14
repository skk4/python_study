'''
Created on 2017.6.29

@author: Administrator
'''
class Animal(object):
    def __init__(self, name):
        self.name = name
    def foo(self, name):
        print self.name   

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        print self.name +' ' + self.name
        
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
class Person(object):
    def __init__(self, name):
        self.name = name
        
        self.pet = None
        
        
class Employee(Person):
    def __init__(self, name, salary):
        self.salary = salary
        super(Employee, self).__init__(name)
        

class Fish(object):
    pass

class Salmon(object):
    pass

class Halibut(object):
    pass                 

rover = Dog("Rover")