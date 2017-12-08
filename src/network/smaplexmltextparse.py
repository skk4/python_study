#-*- coding:utf-8 -*-
'''
Created on 2017.7.24

@author: Administrator
'''
import xml.dom.minidom
doc = xml.dom.minidom.parse('sample.xml')
node = doc.documentElement

print node.nodeName
childlist = []
for child in node.childNodes:
    
    if child.nodeType == node.ELEMENT_NODE:
        print 'child.childNodes:',child.childNodes
        
    '''    
    re= childlist    
    if child.nodeName == 'chapter':
        number = child.getAttribute('number')
        print 'number:', number
            
    if child.nodeName == 'title':
        print 'title ,childnodes:', child.childNodes
        for child in child.childNodes:
            print 'child :',child.data
        
        #title = child.childNodes[0].data
        #print "title:", title    
print re 
'''           
'''
titlelist = node.getElementsByTagName('title')
print titlelist
print titlelist[0]
print titlelist[0].childNodes
print titlelist[0].childNodes[0].nodeType
print titlelist[0].childNodes[0].data
'''
