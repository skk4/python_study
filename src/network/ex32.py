# -*- coding: utf-8 -*-
'''
Created on 2017.7.20

@author: Administrator
'''
##@小五义 http://www.cnblogs.com/xiaowuyi

import DNS
query=raw_input('输入DNS:')
DNS.DiscoverNameServers()

reqobj=DNS.Request()
answerobj=reqobj.req(name=query,qtype=DNS.Type.ANY)
if not len(answerobj.answers):
    print "Not found"
for i in answerobj.answers:
    print answerobj.answers
    print "%-5s %s" % (i['typename'], i['data'])