# -*- coding: UTF-8 -*-
'''
Created on 2017.7.24

@author: Administrator
'''


from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
#获取根节点文档对象
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    
    print "Root element : %s" % collection.getAttribute("shelf")

# 在集合中获取所有tag='movie'电影列表list
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print "*****Movie*****"
    if movie.hasAttribute("title"):
        print "Title: %s" % movie.getAttribute("title")
        
    type = movie.getElementsByTagName('type')[0]
    print "type.childNodes======", type.childNodes
    print "Type: %s" % type.childNodes[0].data
    format = movie.getElementsByTagName('format')[0]
    print "Format: %s" % format.childNodes[0].data
    rating = movie.getElementsByTagName('rating')[0]
    print "Rating: %s" % rating.childNodes[0].data
    description = movie.getElementsByTagName('description')[0]
    print "Description: %s" % description.childNodes[0].data