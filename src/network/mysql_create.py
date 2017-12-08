# -*- coding:utf-8 -*-
'''
Created on 2017年7月28日

@author: Administrator
'''
import MySQLdb
print "Connecting to mysql"
conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'root')
print "Connection successful."
#创建xiesj数据库database
cur = conn.cursor()
cur.execute('create database xiesj')
print 'create database xiesj successed '
cur.close()
#创建user表table
cur = conn.cursor()
cur.execute('use xiesj')    
cur.execute('create table user (id varchar(20) primary key, name varchar(20))')
print 'create table user successed'
cur.close()
#user表table插入id、name字段数据
cur = conn.cursor()
cur.execute('use xiesj')
cur.execute('insert into user (id, name) values (%s, %s)', ('1', 'mike'))
print 'insert user(id, name) successed'
conn.commit()
cur.close()
#查询id用户
cur = conn.cursor()
cur.execute('use xiesj')
cur.execute('select * from user where id = %s', ('1',))
print cur.fetchall()
print 'select user_id successed'
#drop数据库xiesj
cur = conn.cursor()
cur.execute('drop database xiesj')
print 'drop database xiesj successed'
cur.close()   
conn.close()

