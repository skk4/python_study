# -*- coding:utf-8 -*-
import re
import os
from xlwt.Workbook import Workbook
# -*- coding:utf-8 -*-
import threading
import time
import urllib2
import Queue
import re
import os
import sqlite3
#创建数据库
def get_conn(path):
    conn = sqlite3.connect(path)
    return conn

def get_cursor(conn):
    cu= conn.cursor()
    return cu


def colse_conn(conn):
    conn.close()

def create_table(db_name, command):
    db_table = 'E:\\sqlite3_databse\\'+ db_name
    conn = get_conn(db_table)
    print 'opened database successfully'
    cu = get_cursor(conn)
    print 'get cursor'
    cu.execute(command)
    print '%s database created successfully' % db_name
    cu.close()
    print '%s closed' %db_name
    
#插入数据   
def insert_sql(data_list): 
    
    conn = get_conn(r'E:\\sqlite3_databse\\danxia_house.db')
    cu = conn.cursor()
    #command=r"insert into danxia_xm values(?,)",t_t
    for data in data_list:        
        cu.execute(r'''insert OR IGNORE into danxia_xm (HOUSE_HREF, HOUSING_ESTATE ,TOTAL_PRICE, 
        UNIT_PRICE, HOUSE_TYPE, HOUSE_AREAS, HOUSE_DIRECTION, HOUSE_FLOORS,
        HOUSE_REGOIN, HOUSE_YEARS, HOUSE_LOOK, HOUSE_OTHER) 
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''' ,data)
    conn.commit()
    conn.close()

 
#读取页面房源数据
def house_info(file, p):
     
    if os.path.isfile(file):    
        with open(file, 'r') as f:
            html = f.read()  
            #print 'html------', html    
            pattern = re.compile(p, re.DOTALL)
            infos = pattern.findall(html)   
        return infos   
    else:
        pattern = re.compile(p, re.DOTALL)
        infos = pattern.findall(file)        
        return infos
       
#解析保存房源
def save_download_house_info(city, dist_dict):
    book = Workbook()
    for dist in dist_dict:
    
        sheet = book.add_sheet(dist)
        excel_file = 'd://danxia_house//'+ city +'.xls'
        sheet.write(0, 0, '小区'.decode('utf-8'))
        sheet.write(0, 1, '总价'.decode('utf-8'))
        sheet.write(0, 2, '单价'.decode('utf-8'))
        sheet.write(0, 3, '户型'.decode('utf-8'))
        sheet.write(0, 4, '面积'.decode('utf-8'))
        sheet.write(0, 5, '朝向'.decode('utf-8'))
        sheet.write(0, 6, '楼层'.decode('utf-8'))
        sheet.write(0, 7, '位置'.decode('utf-8'))
        sheet.write(0, 8, '年限'.decode('utf-8'))
        sheet.write(0, 9, '看房次数'.decode('utf-8'))
        sheet.write(0, 10, '其他'.decode('utf-8'))
        i = 1
        for page_num in range(1, int(dist_dict[dist])+1):
            file = 'd://danxia_'+city+'//'+city+'_'+dist+'_'+str(page_num)+'.html'
            #print file
            if os.path.exists(file):
                #房子house_herf
                re_house_herf = r'<a.*?class="img".*?href="(.*?)".*?target="_blank">'
                #小区正则规则
                re_house_regoin = r'<p.*?class="moudle">.*?<a.*?target="_blank">(.*?)</a>'
               
                #房型信息正则规则
                re_module = r'<p.*?class="moudle">.*?<a.*?</a>(.*?)</p>'
                re_sub_module = r'<span>(.*?)</span>'
               
                #房屋总价正则规则
                re_total_price= r'<div.*?class="percent">.*?<b>(.*?)</b>'
               
                #房屋单价正则规则
                re_per_price = r'<div.*?class="percent">.*?<span>(.*?)</span>'
               
                #看房次数正则规则
                re_look = r'<p.*?class="text">.*?<span>(.*?)</span>'
               
                #房屋区域正则规则
                re_zone = r'<p.*?class="moudle">.*?</p>.*?<p.*?class="msg">.*?<a.*?target="_blank">(.*?)</a>'
               
                #房屋楼层、年限
                re_msg = r'<p.*?class="moudle">.*?</p>.*?<p.*?class="msg">.*?<a.*?</a>(.*?)</p>'
                re_sub_msg = r'<span>(.*?)</span>'
                re_fix = r'<p.*?class="moudle">.*?</p>.*?<p.*?class="msg">.*?<p.*?class=".*?">(.*?)</p>'
                re_sub_fix = r'<i.*?class=".*?">(.*?)</i>'
                #房子house_href连接
                house_index_ids = house_info(file, re_house_herf)                  
                #当前页面房屋所在小区列表
                house_regoin = house_info(file, re_house_regoin)
                #print '-----', house_regoin
                #当前页户型、面积、朝向信息列表
                house_module = house_info(file, re_module)
               
                #当前页面房屋总价列表
                house_totalprice = house_info(file, re_total_price)
               
                #当前页房屋单价列表
                house_perprice = house_info(file, re_per_price)
               
                #当前页房屋看房次数列表
                house_look = house_info(file, re_look)
               
                #当前页房屋所在区域列表
                house_zone = house_info(file, re_zone)
               
                #当前页房屋楼层、年限类别
                house_msg = house_info(file, re_msg)
               
                #当前页房屋其他信息（有否钥匙等）
                house_fix = house_info(file, re_fix)
               
                #当前页面房屋数
                house_length = len(house_regoin)
                print 'per page house nums: %s' % house_length
                for seq in range(house_length): 
                    house_href = 'http://danxia.com'+ house_index_ids[seq]                                 
                    house_sub_module = house_info(house_module[seq], re_sub_module)
                    house_sub_module_length = len(house_sub_module)
                    if len(house_sub_module) == 3:
                        #户型
                        house_hx = house_sub_module[0]
                        #面积
                        house_area = house_sub_module[1].strip('平米')
                        #朝向
                        house_faceto = house_sub_module[2]
                       
                    #若没有朝向信息，则输入为空   
                    if len(house_sub_module) == 2:
                        house_hx = house_sub_module[0]
                        house_area = house_sub_module[1].strip('平米')
                        house_faceto = ' '
                   
                    #拆分成楼层、年限信息三个列表
                    house_sub_msg = house_info(house_msg[seq], re_sub_msg)
                    house_sub_msg_length = len(house_sub_msg)
                    if house_sub_msg_length == 2:
                        #楼层
                        house_floor = house_sub_msg[0]
                        #年限
                        house_year = house_sub_msg[1]
                       
                    if  house_sub_msg_length == 1:
                        #楼层
                        house_floor = house_sub_msg[0]
                        #年限
                        house_year = ' '
                          
                   
                    house_others = ''
                    house_sub_fix = house_info(house_fix[seq], re_sub_fix)
                    for each_house_sub_fix in house_sub_fix:
                        house_others = house_others + each_house_sub_fix + ','
                    house_others
                   
                    #house_z = house_zone[seq]
                    #print type(house_z.strip('二手房').decode('utf-8'))
                            
                    print '房源链接： %s, 小区：%s, 总价：%s, 单价：%s, 户型：%s, 面积：%s, 朝向：%s,  楼层：%s, 区域：%s, 年限：%s, 看房次数：%s, 其他：%s' \
                    % (house_href, house_regoin[seq], house_totalprice[seq], house_perprice[seq].strip('元/㎡'), house_hx, house_area,  house_faceto,
                        house_floor, house_zone[seq][:-9], house_year.strip('年建'), house_look[seq], house_others)
                   
                               
                               
                    '''                   
                    sheet.write(i, 0 ,house_regoin[seq].decode('utf-8'))
                    sheet.write(i, 1 ,house_totalprice[seq].decode('utf-8'))
                    sheet.write(i, 2 ,house_perprice[seq].strip('元/㎡').decode('utf-8'))
                    sheet.write(i, 3 ,house_hx.decode('utf-8'))
                    sheet.write(i, 4 ,house_area.decode('utf-8'))
                    sheet.write(i, 5 ,house_faceto.decode('utf-8'))
                    sheet.write(i, 6 ,house_floor.decode('utf-8'))
                    sheet.write(i, 7 ,house_zone[seq][:-9].decode('utf-8'))
                    sheet.write(i, 8 ,house_year.strip('年建').decode('utf-8'))
                    sheet.write(i, 9 ,house_look[seq].decode('utf-8'))
                    sheet.write(i, 10 ,house_others.decode('utf-8'))
                    i=i+1
                    
                    
                '''   
                print 'page %s-------' % page_num
                #my_logger(page_num)
   
    book.save(excel_file)
    print 'save'
    
    
class MyScrapWorker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
       
    def run(self):
        while True:
            item = self.queue.get()
            if item is None:
                break
            url= item
            save_download_house_info(url)
            self.queue.task_done()
                
if __name__ == '__main__':
    #城市
    city_xm = 'xm'
    #区及各区房源页数数据字典
    dist_dict_xm ={'BC01':'162', 'BC02':'101', 'BC03':'30',
                   'BC04':'54', 'BC05':'29', 'BC06':'33', 'BC07':'39'}
    dist_dict_xm1 ={'BC01':'1', 'BC02':'0', 'BC03':'0',
               'BC04':'0', 'BC05':'0', 'BC06':'0', 'BC07':'0'}
    #保存数据到excel表
    #save_excel(city_xm, dist_dict_xm)
    
           


if __name__ == "__main__":
    db_name = 'danxia_house.db'
    Command = '''CREATE TABLE IF NOT EXISTS danxia_xm
            (HOUSE_HREF CHAR(128) PRIMARY KEY  NOT NULL,
            HOUSING_ESTATE CHAR(128) NOT NULL,
            TOTAL_PRICE INT ,
            UNIT_PRICE INT ,
            HOUSE_TYPE TEXT,
            HOUSE_AREAS TEXT ,
            HOUSE_DIRECTION TEXT,
            HOUSE_FLOORS TEXT,
            HOUSE_REGOIN TEXT,
            HOUSE_YEARS TEXT,
            HOUSE_LOOK TEXT,
            HOUSE_OTHER TEXT)'''
    create_table(db_name,Command)
    queue = Queue.Queue()
    
    for x in range(3):      
        worker = MyScrapWorker(queue)
        worker.daemon = True
        worker.start()   
    for i in range(1, 21):
       
        url = 'http://danxia.com/house/all/BC01/PG' + str(i)
        queue.put(url)
    queue.join()     