# -*- coding:utf-8 -*-

import pymssql
import sys
#连接mssql
conn = pymssql.connect(host='192.168.22.174', user='sa', password='sasa', database='study_test')

print 'connect successful'
cur = conn.cursor()
query = 'SELECT TOP 100 id ,name FROM dbo.user_name'
cur.execute(query)
#获取所有数据
rows = cur.fetchall()
print ' '
print '-----结果返回中------- '
print ' '
for (id,name) in rows:
    print  'id:',  id 
    print  'name:', name
    print ' '
    print '-----以上是所有结果!------- '
    #关闭连接，释放资源

cur.close()
conn.close()
    
