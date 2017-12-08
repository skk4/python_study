# -*- coding:utf-8 -*-
import time
import threading
import sqlite3
def nomal_producer(conn):
    '''    @summary: producer defination    '''    
    counter = 0    
    conn.isolation_level = None    
    conn.row_factory = sqlite3.Row    
    while True:        
    # insert to db        
        cur = conn.cursor()        
        cur.execute('INSERT INTO datas(content, flag) VALUES (?, ?);', ('content %s' %counter, False))       
        counter = counter + 1       
        # conn.commit()            
        time.sleep(0.1)
        
def nomal_consumer(conn):    
    '''    @summary: consumer defination    '''    
    conn.isolation_level = None    
    conn.row_factory = sqlite3.Row    
    while True:       
    # select data        
        cur = conn.cursor()       
        cur.execute('SELECT * FROM datas ORDER BY id LIMIT 10;')        
        records = cur.fetchall()        
        if len(records) > 0:            
            print 'begin to delete: '            
            print records            
            # delete records            
            for r in records:                
                conn.execute('DELETE FROM datas WHERE id = ?;', (r['id'], ))        
                time.sleep(0.5)
                
if __name__ == '__main__':    
# init db    
    conn = sqlite3.connect('./db.sqlite', check_same_thread = False)    
    # conn = sqlite3.connect('./db.sqlite')    
    # init thread    
    producer = threading.Thread(target = nomal_producer, args = (conn,))    
    consumer = threading.Thread(target = nomal_consumer, args = (conn,))    
    # start threads   
    producer.start()    
    consumer.start()