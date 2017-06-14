# conding=utf-8 -*-
import time
files=file("pome.txt","r")
strs= files.readlines()
try:
    for l in strs:
        print l
        time.sleep(1)
finally:
        files.close()
        print "Cleaning up ...closed the file"
         
            