#-*-coding=utf-8-*-
'''
Created on 2016��10��28��

@author: Administrator
'''


import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.yoya.com")

print html