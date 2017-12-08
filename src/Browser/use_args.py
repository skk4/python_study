def test_var_args(fa, *a):
    print 'formal a:', fa
    for i in a:
        print "another a", i
test_var_args('1', '2', '3')    


def test_var_kargs(fa, **a):
    print 'formal a :', fa
    for i in a:
        print 'another key:',i
        print 'another values',a[i] 
        
        
test_var_kargs(fa='1', faa='2', faaa='3')       