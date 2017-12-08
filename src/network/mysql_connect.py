'''
Created on 2017.7.25

@author: Administrator
'''
import MySQLdb
print "Connecting to yoya_smedia"
conn = MySQLdb.connect(db = 'yoya_smedia', host = 'localhost', user = 'xiesj', passwd = 'xiesj')
print "Connection successful."
cur = conn.cursor()
cur.execute('SELECT * FROM s_user;')
for data in cur.fetchall():
    print data
cur.close()    
conn.close()