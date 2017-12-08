# -*- coding:utf-8 -*-
import logging
import sqlite3
import sys
import threading
import time
#日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-10s) %(message)s',
)
#sqlite3数据库
db_filename=r'E:\\sqlite3_databse\\todo.db'
'''
DEFERRED：延迟锁：这种模式是sqlite3的默认模式，也就是只在发生改变的时候才会锁上被更新的记录。
'''
isolation_level='DEFERRED'
def writer():
    my_name=threading.currentThread().name
    with sqlite3.connect(db_filename,isolation_level=isolation_level) as conn:
        cursor=conn.cursor()
        cursor.execute('update task set priority=priority+1')
        logging.debug('waiting to synchronize')
        ready.wait()# synchronize threads
        time.sleep(1)
        conn.commit()
        logging.debug('CHANGES COMMITTED')
    return
def reader():
    my_name=threading.currentThread().name
    with sqlite3.connect(db_filename,isolation_level=isolation_level) as conn:
        cursor=conn.cursor()
        logging.debug('waiting to synchronize')
        ready.wait() #synchronize threads
        cursor.execute('select * from task')
        logging.debug('SELECT EXECUTED')
        results=cursor.fetchall()
        logging.debug('result fetched')
    return

if __name__=='__main__':
    ready=threading.Event()
    threads=[
        threading.Thread(name='Reader 1',target=reader),
        threading.Thread(name='Reader 2',target=reader),
        threading.Thread(name='Writer 1',target=writer),
        threading.Thread(name='Writer 2',target=writer),
    ]
    [t.start() for t in threads]
    time.sleep(1)
    logging.debug('setting ready')
    ready.set()
    [t.join() for t in threads ]