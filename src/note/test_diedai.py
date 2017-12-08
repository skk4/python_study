def f(n):
    year = 0
    if n == 1:
        year = 10
        return year
        
    else:
        return f(n-1)+2
     
print f(130)        
        