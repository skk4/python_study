def odd():
    n = 1
    while 1:
        yield n
        n = n + 2
        
        
odd_num = odd()
count = 0
for o in odd_num:
    if count >= 5:
        break
    print o
    count = count + 1        