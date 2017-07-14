'''
Created on 2017.7.3

@author: Administrator
'''
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def live(self):
        print 'it is live!'
        

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
        

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    def river(self, name):
        print "%s in the river" %name
    def sea(self):
        print "sea"

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Animal()
rover.live()
Salmon().river('Grass carp')

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()