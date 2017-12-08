'''
Created on 2017.7.18

@author: Administrator
'''
import socket, sys
from click.testing import Result
script = sys.argv[0]
host = sys.argv[1]
try:
    
    #Perform the lookup
    result = socket.gethostbyaddr(host)
    
    #Display the looked-up hostname 
    print "All hostname list:"
    print result
    print "Primary hostname:"
    print " " + result[0]
    #Display the list of available address that is also returned
    print "\n Address:"
    for item in result[2]:
        print " " + item
        
except socket.herror, e:
    print "Couldn't look up hostname.", e
    