'''
print 'How old are you?',
age = raw_input()

print "How tall are you?",
tall = raw_input()

print "How much do you weight?",
weight = raw_input()

print "So you're %r old,%r tall and %r heavy. " %(age, tall, weight)
'''

#f = open('D:\marks.txt', 'w')
#f.write('hello ,world')
#f.write('\nmy name is xieshangji')
f = open('D:\marks.txt', 'r')
print f.read()
print f.readline()
print f.readline()
f.close()