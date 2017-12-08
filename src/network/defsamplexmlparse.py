# -*- coding:utf-8 -*-
'''
Created on 2017.7.24

@author: Administrator
'''
import xml.dom.minidom
def scanNodeName(node):
    if node.childNodes:
        print 'Having childNodes, start parsing xml'
        for child in node.childNodes:
            if child.nodeType == node.ELEMENT_NODE:
                
                print child.nodeName
                node = child
                scanNodeName(node)#递归调用
                
                          
    else:
        print 'parsing over'  
        
        

root = xml.dom.minidom.parse('sample.xml')
doc = root.documentElement
scanNodeName(doc)       