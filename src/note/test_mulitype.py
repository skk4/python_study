'''
f = lambda x ,:x*3
lambda x: x if x%2 else None
'''
def fun(x):
    if x%2 == 0:
        return x
    else:
        return None   

print fun(18)