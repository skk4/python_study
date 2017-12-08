# -*- coding:utf-8 -*-
from HTMLParser import HTMLParser
class Translator(HTMLParser):
    def __init__(self):
        self.trans_result = ''
        self.read_result = 0
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            #print 'attrs............',attrs
            for x, y in attrs:
                #print x, y
                if y == 'tgt':           
                    self.read_result = 1
            
            
    def handle_data(self, data):
        if self.read_result:
            self.trans_result = data + self.trans_result
             
        
        
    def handle_endtag(self, tag):
        if tag == 'p':
            self.read_result = 0           
            
            
    def gettrans_rusult(self):
        return self.trans_result        
fd = open('aa.html')
tp = Translator()
for each in fd.readlines():
    
    tp.feed(each + '------------\n')
print tp.gettrans_rusult()