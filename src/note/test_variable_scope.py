def outside():
    #print 'I am outside'
    var = 5
    
    def inside():
        print var
        var = 3
        
        #print 'I am inside'
    inside()


outside()         