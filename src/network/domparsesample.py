'''
Created on 2017.7.24

@author: Administrator
'''
from xml.dom import minidom, Node
import re
import textwrap


class SampleScanner:
    def __init__(self, doc):
        for child in doc.childNodes:
            if child.nodeType == Node.ELEMENT_NODE and child.tagName == 'book':
                self.handleBook(child)
    def gettext(self, nodelist):
        '''give a list of one or more nodes, recurively finds all text nodes
        in that list (or children of nodes in that list), concatenates them
        ,removes duplicate spaces, and returns the result'''
        retlist = []
        for node in nodelist:
            if node.nodeType == node.ELEMENT_NODE:
                retlist.append(node.wholeText)
            elif node.hasChildNodes:
                retlist.append(self.gettext(node.childNodes))
        return re.sub('\s+',' ',''.join(retlist)) 
           
    def handleBook(self, node):
        '''Process the book tag. Look for little, author, then chapters.'''
        for child in node.childNodes:
            if child.nodeType != node.ELEMENT_NODE:
                continue
            if child.nodeName == 'title':
                print "Book title is:", self.gettext(child.childNodes)
        
            
doc = minidom.parse('sample.xml')
SampleScanner(doc)