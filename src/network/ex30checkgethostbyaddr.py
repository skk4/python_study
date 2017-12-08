'''
Created on 2017.7.18

@author: Administrator
'''
import sys, socket
script = sys.argv[0]
ip = sys.argv[1]

def gethostname(ipaddr):
    '''Get the hostname from a given IP address. This is a reverse
    look up'''
    return socket.gethostbyaddr(ipaddr)[0]

def getipaddrs(hostname):
    '''Get a list of IP addresses from a given hostname . This is standard (forward)
    look up'''
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]    
try:
    #First , do the reverse lookup and get the hostname
    hostname = gethostname(ip) # could raise socket.herror
    #Now, do a forward lookup on the result from the earlier reverse
    #lookup
    ipaddr = getipaddrs(hostname)
    
except socket.herror, e:
    
    print "No hostname available for %s; this may be normal." % ip
    sys.exit(1)
except socket.gaierror, e:
    print "Got hostname %s, but it could not be forward-resolved: %s" % (hostname, str(e))
    sys.exit(1)
#if the forward look-up didn't yield the original IP address anywhere
#someone is playing tricks. explain the situation and exit    
if not ip in ipaddr :
    print "Got hostname %s, but on forward lookup," % hostname
    print "Original IP %s didn't appear in IP addresses list." % ip
    sys.exit(1)
    
#otherwise ,show the validates hostname
print "validated hostname:" ,hostname        
            