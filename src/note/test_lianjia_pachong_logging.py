# -*-coding:utf-8 -*-
import re
import os
import logging
def house_info(file, p):
    
    if os.path.isfile(file): 
    
        with open(file, 'r') as f:
            html = f.read()
        
            pattern = re.compile(p)
            infos = pattern.findall(html)
    
        return infos
    
    else:
        pattern = re.compile(p)
        infos = pattern.findall(file)
         
        return infos
        

def house_info_parser(htm, p):
    pass
    

if __name__ == '__main__':
    city = 'xm'
    dist ='huli'
    file = 'd://lianjia_'+city+'//'+city+'_'+dist+'_'+'33.html'
    re_taxfree = r'<li.*?class="clear".*?class="taxfree">(.*?)</span>'
    re_five = r'<li.*?class="clear".*?class="five">(.*?)</span>'
    re_house_detail = r'class="tag">.*?"region">.*?</a>(.*?)</div>'
    re_data_index = r'<li.*?class="img.*?data-log_index="(.*?)".*?data-el'
    re_house_tag = r'<li.*?class="tag".*?>(.*?)</div>'
    re_sub_house_tag = r'<span.*?class=.*?">(.*?)</span>'
    #re_house_tag = r'li.*?<div.*?class="tag"(.*?).*?/div'
    house_taxfree = house_info(file, re_taxfree)
    house_five = house_info(file, re_five)
    house_index = house_info(file, re_data_index)
    house_tag = house_info(file, re_house_tag)
    for seq in range(0, len(house_tag)):
        house_tax = ''
        if house_tag[seq]== '':
            house_tax = house_tag[seq]
            
        else:   
            house_tax_sub = house_info(house_tag[seq], re_sub_house_tag)
            for each_house_tax in house_tax_sub:
                house_tax = house_tax  +  each_house_tax + ' '  
        print '税费:%s' % house_tax  
    '''
    for i in house_tag :
        sub_house_tag = house_info(i, re_sub_house_tag)
        for j in sub_house_tag :
            print j 
    '''         
    '''    
    for i in house_taxfree:
        print 'i:', i
        
    for j in house_five:
        print 'j:', j    
    '''
    '''
    for m in house_index:
        print m
    '''
    '''
    house_detail = house_info(file, re_house_detail)#['3人关注 /共0次带看 /6天以前发布']
    num = len(house_detail)
    for seq in range(0, num):
        house_layout = house_detail[seq].split('|')[1]
        house_area = house_detail[seq].split('|')[2]
        house_fixed = ''
        for each_house_fixed in house_detail[seq].split('|')[3:]:
            
            house_fixed = house_fixed + '' + each_house_fixed
        print '户型: %s 面积:%s 装修: %s' % (house_layout, house_area, house_fixed)
    '''    
    '''
    re_house_publish = r'class="starIcon"></span>(.*?)</div>'
    house_publish = house_info(file, re_house_publish)#['3人关注 /共0次带看 /6天以前发布']
    num = len(house_publish)
    for seq in range(0, num):
        house_focus = house_publish[seq].split('/')[0]
        house_look = house_publish[seq].split('/')[1]
        house_push_time = house_publish[seq].split('/')[2]
        print '关注人数: %s 看房次数:%s 发布时间: %s' % (house_focus, house_look, house_push_time)
        
    '''    