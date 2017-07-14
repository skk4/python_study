name = 'Xie shangji'
age = 34
height = 1.70 #m
weight = 60 #kg
eyes = 'Black'
teeth = 'White'
hair = 'Black'

def meter_to_inch(h):
    return h*39.37
def kg_to_pounds(w):
    return w*2.2046226    

print "Let's talk about %s." %name
print "He is %.2f meter tall." %meter_to_inch(height)
print "He is %.2f kg heavy." %kg_to_pounds(weight)
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

print "If I add %d, %.2f, and %d I get %.2f." %(age, meter_to_inch(height), kg_to_pounds(weight), age+meter_to_inch(height)+kg_to_pounds(weight))

print 10*10
print "agree with me " * 2