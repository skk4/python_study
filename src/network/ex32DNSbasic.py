# -*-coding:utf-8 -*-
'''
Created on 2017.7.19

@author: Administrator
'''
'''常见的dns资源记录类型：
A记录：域名到IP的映射
CNAME：通用规范名称，可以理解为域名到域名的映射
PTR记录：反解，IP到域名的映射
NS记录：  NS（Name Server）记录是域名服务器记录，用来指定该域名由哪个DNS服务器来进行解析,
如： ns1.domain.com、ns2.domain.com等
mx记录：MX记录 MX（Mail Exchanger）记录是邮件交换记录，它指向一个邮件服务器，用于电子邮件系统发邮件时根据收信人的地址后缀来定位邮件服务器。例如，当Internet上的某用户要发一封信给 user@mydomain.com 时，该用户的邮件系统通过DNS查找mydomain.com这个域名的MX记录，
如果MX记录存在， 用户计算机就将邮件发送到MX记录所指定的邮件服务器上。  '''
import sys, DNS
#script = sys.argv[0]
qurey = raw_input(">:")
DNS.DiscoverNameServers()
reqobj = DNS.Request()
answerobj = reqobj.req(name = qurey, qtype = DNS.Type.ANY)
print "answerobj.answers: " , answerobj.answers
print "len:", len(answerobj.answers)
if not len(answerobj.answers):
    print "Not Found"
    
for item in answerobj.answers:
    print "%-5s %s" %(item['typename'], item['data'])    