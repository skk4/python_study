# -*- coding:utf-8 -*-
import urllib2
from HTMLParser import HTMLParser
class Get_iplist(HTMLParser):
    def __init__(self):
        self.trans_result = ''
        self.read_result = 0
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            #print 'attrs............',attrs
            #for x, y in attrs:
                #print x, y
                #if x == 'class':           
                    #self.read_result = 1
            
            self.read_result = 1
    def handle_data(self, data):
        if self.read_result and not data.isspace():
            self.trans_result = data.strip() +'\n' + self.trans_result 
             
        
        
    def handle_endtag(self, tag):
        if tag == 'td':
            self.read_result = 0           
            
            
    def gettrans_rusult(self):
        return self.trans_result 

url = 'http://www.xicidaili.com/nn/1'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
rq = urllib2.Request(url, headers = headers)
fd = urllib2.urlopen(rq)
html = fd.read()
tp = Get_iplist()
tp.feed(html)
with open('iplist_source.txt', 'w') as f:
    f.write(tp.gettrans_rusult())
#print 'tp--',tp.gettrans_rusult()
fd.close()

with open('iplist_source.txt', 'r') as f:
    f_list = f.readlines()
    i = 5
    iplist = []
    while 1:
        if i < len(f_list):
            print f_list[i], f_list[i+1]
            iplist.append(f_list[i+1]+':'+f_list[i])
            i = i + 7      
            
        else:
            break    
        
print iplist  
for i in iplist:
    print i.strip('\n')  



    
    
