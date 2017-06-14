def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
print intersect('tpam','scam')
print intersect([1,2,3],(1,3))   