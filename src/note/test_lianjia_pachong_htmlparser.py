from HTMLParser import HTMLParser
import time
import re

class Translator(HTMLParser):
    def __init__(self):
        self.trans_result = ','
        self.read_result = 0
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        '''
        if tag == 'a':
            #print 'attrs............',attrs
            for x, y in attrs:
                #print x, y
                if y == 'region':           
                    self.read_result = 1
        '''    
        if tag == 'a':
            for x, y in attrs:
                #print x, y
                if y == '_blank': 
                    #print 'x====', x          
                    self.read_result = 1
                 
        '''    
        if tag == 'div':
            for x, y in attrs:
                #print x, y
                if y == 'totalPrice' or y == 'unitPrice' or y == 'houseInfo': 
                    #print 'x====', x          
                    self.read_result = 1
        ''' 
        '''           
        if tag == 'span':
            for x, y in attrs:
                if y == 'taxfree':
                    self.read_result = 1
        '''                                 
                
    def handle_data(self, data):
        if self.read_result:
            print 'data', data
            self.trans_result = data + self.trans_result  
             
        
        
    def handle_endtag(self, tag):
        if tag == 'a':
            self.read_result = 0
            
        if tag == 'div':
            self.read_result =0 
            
        if tag == 'span':
            self.read_result = 0      
                        
            
            
    def gettrans_rusult(self):
        return self.trans_result     
    
    
tp = Translator() 
with open('D://lianjia_xm/xm_huli_1.html', 'r') as f:
    html = f.read().decode('utf-8')
    tp.feed(html)
    print 'tp--',tp.gettrans_rusult()  
