#-*-coding=utf-8-*-
'''
Created on 2016Äê10ÔÂ28ÈÕ

@author: Administrator
'''


import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.yoya.com")

print html