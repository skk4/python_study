from sys import argv
script, filename = argv

txt = open(filename)

print "Here is your file %r:" % filename
print 'argv[0]:', argv[0]
print 'argv[1]:', argv[1]

print txt.read()
txt.close()

print "Type the filename again:"

file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()
