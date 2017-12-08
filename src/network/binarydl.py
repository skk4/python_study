'''
Created on 2017.7.25

@author: Administrator
'''
from ftplib import FTP
import time
ftp = FTP('ftp.ibiblio.org')
ftp.login()
ftp.cwd('/pub/linux')
fd = open('INDEX.whole.gz', 'wb')
print 'wating......'
time.sleep(5)
ftp.retrbinary('RETR INDEX.whole.gz', fd.write)
fd.close()
ftp.quit()   