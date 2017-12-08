# -*- coding:utf-8 -*-
'''
Created on 2017.7.20

@author: Administrator
'''
##在python2.7上执行会出错，其中x['type'] == qtype 条件跑不起来
import DNS
def hierquery(qstring,qtype):
    reqobj=DNS.Request()
    try:
        print query
        answerobj=reqobj.req(name=query,qtype=qtype)
        answers=[x['data'] for x in answerobj.answers if x['type']==qtype]
        '''
        answers = []
        for x in answerobj.answers:
            if x['type'] == qtype:
                answers.append(x['data'])
             
        '''
        print answers
    except DNS.Base.DNSError:
        answers=[]
    if len(answers):
        return answers
    else:
        print 'aaa'
        remainder=qstring.split(".",1)
        print remainder
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
    nslist=findnameservers(qstring)
    if nslist==None:
        raise RuntimeError,'找不到服务器'
    if verbose:
        print "服务器:",",".join(nslist)
    return getrecordsfromnameserver(qstring,qtype, nslist)
if  __name__=='__main__':
    query=raw_input('输入网站:')
    DNS.DiscoverNameServers()
    answers=nslookup(query,DNS.Type.ANY)
    if not len(answers):
        print "未找到！"
    for i in answers:
        print "%-5s %s"%(i['typename'],i['data'])