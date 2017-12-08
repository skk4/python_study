import threading
import time
def worker():
    print "worker"
    time.sleep(2)
    return
for i in xrange(5):
    worker()
    #t = threading.Thread(target=worker)
    #t.start()