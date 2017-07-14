from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copy from %s to %s" %(from_file, to_file)

input_file = open(from_file)
input_file_data = input_file.read()

print "The input file is %d bytes long" % len(input_file_data)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output_file = open(to_file, 'w')
output_file.write(input_file_data)

print "Alright, all done"

output_file.close()
input_file.close()

