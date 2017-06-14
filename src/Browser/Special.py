class A:
    pass 
class B: 
    def __init__(self,a,b="b"):
        self.a=a
        self.b=b
a = A()
b1 = B("a")
b2 = B("a","c")
b=B(a,"d")
b.a