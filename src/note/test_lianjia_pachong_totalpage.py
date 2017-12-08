# -*- coding:utf-8 -*-
import re
import os

#读取各区房源页数
def total_page(city, dist):
    file = 'd://lianjia_'+city+'//'+city+'_'+dist+'_'+'1.html'
    if os.path.exists(file):
        with open(file, 'r') as f:
            html = f.read()
            #print html
            p = r'{"totalPage":(.+?),"curPage"'
            pat = re.compile(p)
            
            pages =  pat.findall(html)[0]
 
        return pages
'''
city = 'xm'
dist = 'siming'
dist_dict = {}
dist_dict[dist] = total_page(city, dist)
print dist_dict
'''
dist_dict = {}
city = 'wh'
dists = ('jiangan', 'jianghan', 'qiaokou', 'dongxihu', 'wuchang', 'qingshan',
            'hongshan', 'hanyang', 'donghugaoxin', 'jiangxia')
    
for dist in dists:
    dist_dict[dist] = total_page(city, dist)
print dist_dict    
    