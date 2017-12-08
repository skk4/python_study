def gcd(big,small):
    
    remainder = big % small
    if remainder == 0:
        return small
    else:
        return gcd(small,remainder) 
    
    
print gcd(49,14)    