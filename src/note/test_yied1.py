       
def su(num):
    for i in range(2, num):
        yield num%i
num = 2000000 
sum_su = 0
for i in range(2, num):       
    if 0 not in su(i):
        sum_su = sum_su+i
         
print sum_su