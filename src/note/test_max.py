'''
在列表中取第一个数假设它是最大值max，然后列表中所有值比较each与max比较:
如果列表中有each值大于max，那么把each赋值给max（max = each）
如果列表中没有each值大于max，那么max肯定是最大
'''
def max(x):
    max_one = x[0]
    for each in x:
        if each > max_one:
            max_one = each
    return max_one                     