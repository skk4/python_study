# -*- coding:utf-8 -*-
class Stack(object):

    def push(self, x):
        self.x = x
        stack_list.append(self.x)
        
        
    def top(self):
        return stack_list[0]
    
    def bottom(self):
        
        return stack_list[-1]
    
    def pop(self):
        stack_list.pop(0)
        return stack_list
    
    def isEmpty(self):
        
        if len(stack_list)==0:
            return True
        
        else:
            return False
        
        
        
            
        
        
        
stack_list = []
s = Stack()
s.push("F")
s.push("i")
s.push('s')
s.push('h')
s.push('C')
print s.top()
print s.bottom()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.isEmpty()
Stack.x
        