# -*- coding:utf-8 -*-
import re
import os
from xlwt.Workbook import Workbook
import logging
def my_logger(log_obj):
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='d://lianjia_house//save_excel.log',
                    filemode='w')
    
    #################################################################################################
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    #################################################################################################
    
    logging.debug('This is debug message : %s' %log_obj)
    logging.info('This is info message :%s' %log_obj)
    logging.warning('This is warning message :%s' %log_obj)
 

#读取页面房源数据
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
        

#解析保存房源
def save_excel(city, dist_dict):
    book = Workbook()
    for dist in dist_dict:
        sheet = book.add_sheet(dist)
        excel_file = 'd://lianjia_house//'+ city +'.xls'
        sheet.write(0, 0, '小区'.decode('utf-8'))
        sheet.write(0, 1, '总价'.decode('utf-8'))
        sheet.write(0, 2, '单价'.decode('utf-8'))
        sheet.write(0, 3, '户型'.decode('utf-8'))
        sheet.write(0, 4, '面积'.decode('utf-8'))
        sheet.write(0, 5, '装修'.decode('utf-8'))
        sheet.write(0, 6, '楼层'.decode('utf-8'))
        sheet.write(0, 7, '位置'.decode('utf-8'))
        sheet.write(0, 8, '关注人数'.decode('utf-8'))
        sheet.write(0, 9, '看房次数'.decode('utf-8'))
        sheet.write(0, 10, '发布时间'.decode('utf-8'))
        sheet.write(0, 11, '税费'.decode('utf-8'))
        
        i = 1
        for page_num in range(1, int(dist_dict[dist])+1):
            file = 'd://lianjia_'+city+'//'+city+'_'+dist+'_'+str(page_num)+'.html'
            if os.path.exists(file):
                re_house_regoin = r'"region">(.*?)</a>'
                re_house_detail = r'"region">.*?</a>(.*?)</div>'
                re_house_totalprice = r'totalPrice">.*?<span>(.*?)</span>'
                re_house_perprice = r'data-price="(.*?)">'
                re_house_poistion = r'class="positionInfo">.*?<a.*?target="_blank">(.*?)</a>'
                re_house_floor = r'class="positionIcon"></span>(.*?)<a'
                re_house_publish = r'class="starIcon"></span>(.*?)</div>'
                re_house_tag = r'<li.*?class="tag".*?>(.*?)</div>'
                re_sub_house_tag = r'<span.*?class=.*?">(.*?)</span>'
                house_regoin = house_info(file, re_house_regoin)
                house_detail = house_info(file, re_house_detail)
                house_total_price = house_info(file, re_house_totalprice)
                house_per_price = house_info(file, re_house_perprice)
                house_position = house_info(file, re_house_poistion)
                house_floor = house_info(file, re_house_floor)
                house_publish = house_info(file, re_house_publish)
                house_tag = house_info(file, re_house_tag)
                
                #print house_regoin[1]
                house_sum = len(house_regoin)
                print 'per page house nums: %s' % house_sum
        
                for seq in range(0, house_sum):
                    house_focus = house_publish[seq].split('/')[0].strip().strip('人关注')
                    house_look = house_publish[seq].split('/')[1].strip().strip('共').strip('次带看')
                    house_push_time = house_publish[seq].split('/')[2].strip()
                    house_layout = house_detail[seq].split('|')[1].strip()
                    house_area = house_detail[seq].split('|')[2].strip().strip('平米')
                    house_fixed = ''
                    for each_house_fixed in house_detail[seq].split('|')[3:]:
            
                        house_fixed = house_fixed + '' + each_house_fixed 
                    
                    
                    house_tax = ''
                    if house_tag[seq]== '':
                        house_tax = house_tag[seq]
            
                    else:           
                        house_tax_sub = house_info(house_tag[seq], re_sub_house_tag)
                        for each_house_tax in house_tax_sub:
                            house_tax = house_tax  +  each_house_tax + ' '  
                    
                    
                          
                    print '小区:%s 总价:%s 单价:%s 户型:%s 面积: %s 装修: %s 楼层:%s 位置:%s 关注人数: %s 看房次数:%s 发布时间: %s 税费: %s'  \
                    %(house_regoin[seq], house_total_price[seq], house_per_price[seq], 
                      house_layout, house_area, house_fixed, house_floor[seq], house_position[seq], 
                      house_focus, house_look, house_push_time, house_tax)    
                    sheet.write(i, 0 ,house_regoin[seq].decode('utf-8'))
                    sheet.write(i, 1 ,house_total_price[seq].decode('utf-8'))
                    sheet.write(i, 2 ,house_per_price[seq].decode('utf-8'))
                    sheet.write(i, 3 ,house_layout.decode('utf-8'))
                    sheet.write(i, 4 ,house_area.decode('utf-8'))
                    sheet.write(i, 5 ,house_fixed.decode('utf-8'))
                    sheet.write(i, 6 ,house_floor[seq].decode('utf-8'))
                    sheet.write(i, 7 ,house_position[seq].decode('utf-8'))
                    sheet.write(i, 8 ,house_focus.decode('utf-8'))
                    sheet.write(i, 9 ,house_look.decode('utf-8'))
                    sheet.write(i, 10 ,house_push_time.decode('utf-8'))
                    sheet.write(i, 11 ,house_tax.decode('utf-8'))
                    i=i+1
                print 'page %s-------' % page_num
                #my_logger(page_num)
    
    book.save(excel_file)
    print 'save'
    #my_logger(excel_file)


if __name__ == '__main__':
    #城市
    city_wh = 'wh'
    city_xm = 'xm'
    #区及各区房源页数数据字典
    dist_dict_wh = {'jiangan':'78', 'jianghan':'67', 'qiaokou':'33', 
                 'dongxihu':'43', 'wuchang':'65', 'qingshan':'3', 
                 'hongshan':'81', 'hanyang':'45', 'donghugaoxin':'64', 
                 'jiangxia':'3'}
    
    dist_dict_xm ={'siming':'74', 'huli':'60', 'haicang':'37',
                   'jimei':'36', 'xiangan':'3', 'tongan':'2'}
    #保存数据到excel表
    save_excel(city_xm, dist_dict_xm)