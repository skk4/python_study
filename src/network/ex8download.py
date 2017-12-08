'''
Created on 2017.7.13

@author: Administrator
'''
import urllib
import sys
script = sys.argv[0]
host = sys.argv[1]
file = sys.argv[2]
f = urllib.urlopen('http://%s%s' %(host, file))
for line in f.readlines():
    sys.stdout.write(line)

