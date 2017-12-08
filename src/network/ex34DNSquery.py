# -*- coding:utf-8 -*-
'''
Created on 2017.7.20

@author: Administrator
'''

import sys, DNS, re
def hierquery(qstring,qtype):
    reqobj=DNS.Request()
    try:
        answerobj=reqobj.req(name=query,qtype=qtype)
        answers=[x['data'] for x in answerobj.answers if x['type']==qtype]
    except DNS.Base.DNSError:
        answers=[]
    if len(answers):
        return answers
    else:
        remainder=qstring.split(".",1)
        if len(remainder)==1:
            return None
        else:
            return hierquery(remainder[1],qtype)
def findnameservers(hostname):
    return hierquery(hostname,DNS.Type.NS)
def getrecordsfromnameserver(qstring,qtype,nslist):
    for ns in nslist:
        reqobj=DNS.Request(server=ns)
        try:
            answers=reqobj.req(name=qstring,qtype=qtype).answers
            if len(answers):
                return answers
        except DNS.Base.DNSError:
            pass
    return []

def nslookup(qstring,qtype,verbose=1):
    print qstring
    nslist=findnameservers(qstring)
    print nslist
    if nslist==None:
        raise RuntimeError,'找不到服务器'
    if verbose:
        print "服务器:",",".join(nslist)
    return getrecordsfromnameserver(qstring,qtype, nslist)

def getreverse(query):
    """Given the query, returns an appropriate reverse lookup string
    under IN-ADDR.ARPA if query is an IP address; otherwise, returns None.
    This function is not IPv6-compatible."""
    if re.search('^/d+/./d+/./d+/./d+$', query):
        octets = query.split('.')
        octets.reverse()
        return '.'.join(octets) + '.IN-ADDR.ARPA'
    return None

def formatline(index, typename, descr, data):
    retval = "%-2s %-5s" % (index, typename)
    if isinstance(data,list):
        return retval
    else:
        
        data = data.replace("/n", "/n         ")
        if descr != None and len(descr):
            retval += " %-12s" % (descr + ":")
        return retval + " " + data

DNS.DiscoverNameServers()
query1=raw_input('输入网站：')
queries = [(query1, DNS.Type.ANY)]
donequeries = []
descriptions = {'A': 'IP address',
                'TXT': 'Data',
                'PTR': 'Host name',
                'CNAME': 'Alias for',
                'NS': 'Name server'}
              
while len(queries):
    (query, qtype) = queries.pop(0)
    if query in donequeries:
        # Don't look up the same thing twice
        continue
    donequeries.append(query)
    print "-" * 77
    print "Results for %s (lookup type %s)" %(query, DNS.Type.typestr(qtype))
    print
    rev = getreverse(query)
    if rev:
        print "IP address given; doing reverse lookup using", rev
        query = rev
       
    answers = nslookup(query, qtype, verbose = 0)
    if not len(answers):
        print "Not found."

    count = 0
    for answer in answers:
        count += 1
        if answer['typename'] == 'MX':
            print formatline(count, answer['typename'],
                             'Mail server',
                             "%s, priority %d" % (answer['data'][1],
                                                  answer['data'][0]))
            queries.append((answer['data'][1], DNS.Type.A))
        elif answer['typename'] == 'SOA':
            data = "/n" + "/n".join([str(x) for x in answer['data']])
            ##print data
            print formatline(count, 'SOA', 'Start of authority', data)
        elif answer['typename'] in descriptions:
            ##print answer['data']
            print formatline(count, answer['typename'],
                             descriptions[answer['typename']], answer['data'])
        else:
            print formatline(count, answer['typename'], None,
                             str(answer['data']))
        if answer['typename'] in ['CNAME', 'PTR']:
            queries.append((answer['data'], DNS.Type.ANY))
        if answer['typename'] == 'NS':
            queries.append((answer['data'], DNS.Type.A))