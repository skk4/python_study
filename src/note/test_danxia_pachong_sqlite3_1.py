# -*- coding:utf-8 -*-
import threading
import time
import datetime
import urllib2
import Queue
import re
import os
import sqlite3
import logging
import logging.handlers
import random
#封装日志类
class Logger():
    def __init__(self, logName, logLevel, logger):

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logName)
        fh.setLevel(logLevel)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logLevel)

        # 定义handler的输出格式    
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s \
        -[%(filename)s:%(lineno)d]')
        fh.setFormatter(log_format)
        ch.setFormatter(log_format)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


   
    def getlog(self):
        return self.logger

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
    #mylogger = Logger(logName=r'D:\\python_save_path\\insert_sql.txt', logLevel='INFO', logger='insert_data_log').getlog()
    global mylogger_danxia
    db_table = 'E:\\sqlite3_databse\\'+ db_name
    conn = get_conn(db_table)
    cu = conn.cursor()
    #command=r"insert into danxia_xm values(?,)",t_t
    for data in data_list:        
        cu.execute(r'''insert OR IGNORE into danxia_xm (HOUSE_HREF, HOUSING_ESTATE ,TOTAL_PRICE, 
        UNIT_PRICE, HOUSE_TYPE, HOUSE_AREAS, HOUSE_DIRECTION, HOUSE_FLOORS,
        HOUSE_REGOIN, HOUSE_YEARS, HOUSE_LOOK, HOUSE_OTHER) 
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''' ,data)
        mylogger_danxia.info(data)
    conn.commit()
    
    conn.close()

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]

     
#下载房源页解析并插入sqlite3数据库，边下载边插入
def save_download_house_info(url):
    #mylogger = Logger(logName=r'D:\\python_save_path\\downloaded_url.txt', logLevel='INFO', logger='downloaded_url_log').getlog()
    global mylogger_danxia 
    time.sleep(1)
    try:
        rq = urllib2.Request(url, headers=hds[random.randint(0,len(hds)-1)])
        fd = urllib2.urlopen(rq, timeout=10)
        html = fd.read().decode('utf-8')
        mylogger_danxia.info(url)
          
    except (urllib2.HTTPError, urllib2.URLError), e:
        print e
        return
    except Exception,e:
        print e
        return   
    #解析房源href
    re_house_herf = r'<a.*?class="img".*?href="(.*?)".*?target="_blank">'
    house_herf = re.compile(re_house_herf, re.DOTALL).findall(html)
    #解析房源小区
    re_housing_estate = r'<p.*?class="moudle">.*?<a.*?target="_blank">(.*?)</a>'
    housing_estate =re.compile(re_housing_estate, re.DOTALL).findall(html)
    #解析房源总价
    re_total_price= r'<div.*?class="percent">.*?<b>(.*?)</b>'
    total_price = re.compile(re_total_price, re.DOTALL).findall(html)
    #解析房源单价
    re_unit_price = r'<div.*?class="percent">.*?<span>(.*?)</span>'
    unit_price = re.compile(re_unit_price, re.DOTALL).findall(html)
    #解析户型、面积、朝向
    re_layout = r'<p.*?class="moudle">.*?<a.*?</a>(.*?)</p>'
    re_sub_layout =r'<span>(.*?)</span>'
    #第一次解析
    house_layout = re.compile(re_layout, re.DOTALL).findall(html)
    #解析楼层、年限
    re_msg = r'<p.*?class="moudle">.*?</p>.*?<p.*?class="msg">.*?<a.*?</a>(.*?)</p>'
    re_sub_msg = r'<span>(.*?)</span>'
    house_msg = re.compile(re_msg, re.DOTALL).findall(html)
    #看房次数
    re_look = r'<p.*?class="text">.*?<span>(.*?)</span>'
    house_look = re.compile(re_look, re.DOTALL).findall(html)
    #房子区域
    re_region = r'<p.*?class="moudle">.*?</p>.*?<p.*?class="msg">.*?<a.*?target="_blank">(.*?)</a>'
    house_region = re.compile(re_region, re.DOTALL).findall(html)
    #其他信息
    re_fix = r'<p.*?class="moudle">.*?</p>.*?<p.*?class="msg">.*?<p.*?class=".*?">(.*?)</p>'
    re_sub_fix = r'<i.*?class=".*?">(.*?)</i>'
    house_fix = re.compile(re_fix, re.DOTALL).findall(html)
    
    

                    
    #插入sqlite3数据库
    data_list = []
    house_href_length = len(house_herf)
    for seq in range(house_href_length):  
        print '*****house_href:*****', house_herf[seq]
        print '*****housing_estate:*****', housing_estate[seq]
        print '*****total_price:*****', total_price[seq]
        print '*****unit_price:*****', unit_price[seq].strip(u'元/㎡') 
        
        #分解出户型、面积、朝向
        house_sub_layout = re.compile(re_sub_layout, re.DOTALL).findall(house_layout[seq])
        if len(house_sub_layout) == 3:
            #解析户型
            house_type = house_sub_layout[0]
            #解析面积
            house_areas = house_sub_layout[1].strip(u'平米')
            #解析朝向
            house_direction = house_sub_layout[2]
            
        if len(house_sub_layout) == 2:
            #解析户型
            house_type = house_sub_layout[0]
            #解析面积
            house_areas = house_sub_layout[1].strip(u'平米')
            #解析朝向
            house_direction = ' '
               
        print '*****house_type:*****', house_type
        print '*****house_areas:*****', house_areas
        print '*****house_direction:*****', house_direction
        
        
        #分解楼层、年限
        house_sub_msg = re.compile(re_sub_msg, re.DOTALL).findall(house_msg[seq])
        if len(house_sub_msg) == 2:
            #解析楼层
            house_floors = house_sub_msg[0]
            #解析年限
            house_years = house_sub_msg[1]
            
        if len(house_sub_msg) == 1:
            #解析楼层
            house_floors = house_sub_msg[0]
            #解析年限
            house_years =' ' 
        print '*****house_floors:*****', house_floors
        print '*****house_years:*****', house_years.strip(u'年建')
        print '*****house_region:*****', house_region[seq]  
        print '*****house_look:*****', house_look[seq] 
        #分解其他
        house_others = ''
        house_sub_fix = re.compile(re_sub_fix, re.DOTALL).findall(house_fix[seq])
        for each_house_sub_fix in house_sub_fix:
                        house_others = house_others + each_house_sub_fix + ','
              
        print '*****house_others:*****', house_others  
         
        data =  (house_herf[seq], housing_estate[seq], total_price[seq],
               unit_price[seq].strip(u'元/㎡'), house_type, house_areas,
                house_direction, house_floors, house_years.strip(u'年建'),
                house_region[seq], house_look[seq], house_others)
        
        data_list.append(data)
    insert_sql(data_list)
 
       
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

if __name__ == "__main__":
    mylogger_danxia = Logger(logName=r'D:\\python_save_path\\downloaded_url.txt', logLevel='INFO', logger='danxia_xm_log').getlog()

    i = datetime.datetime.now()
    date_time = str(i.year)+str(i.month)+ str(i.day)+str(i.hour)+str(i.minute)+str(i.second)
    
    db_name = 'danxia_house'+'_'+ date_time+'.db'
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
    for i in range(1, 3):
       
        url = 'http://danxia.com/house/all/BC01/PG' + str(i)
        queue.put(url)
    queue.join()
    print 'end' 
    
