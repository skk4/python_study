'''
Created on 2017.7.24

@author: Administrator
'''
import xml.dom.minidom
#import xml.dom.minidom.Node
root = xml.dom.minidom.parse('sample.xml')
nodes = root.documentElement
print nodes.nodeName
for node in nodes.childNodes:
    if node.nodeType == node.ELEMENT_NODE:
        print node.nodeName
        if node.hasChildNodes:
            for childnode in node.childNodes:
                if childnode.nodeType == node.ELEMENT_NODE:
                    print childnode.nodeName
                    
                    for grandson in childnode.childNodes:
                        if grandson.nodeType == node.ELEMENT_NODE:
                            print grandson.nodeName
            
        

            