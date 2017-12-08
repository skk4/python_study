# -*- coding:utf-8 -*-
import time as t
class MyTimer(object):

    def __add__(self, other):
        hint = ''
        for i in range(6):
            a = self.end[i] - self.begin[i]
            b = other.end[i] - other.begin[i]
            if a + b != 0:

                hint = hint + str(a + b) + self.unit[i]

        print hint


    def __init__(self):
        self.tcalc = ''
        self.unit = ['年', '月', '天', '小时', '分', '秒']
        self.end = []
        self.begin = []

    def __str__(self):
        if not len(self.begin):
            return '未开始计时'
            
        elif not len(self.end):
            return '需先暂停计时'
            
        else:        
            return self._calc()



    def start(self):
        
        if len(self.begin):
            print '已经开始计时,需先暂停计时'
            
        else:

            self.begin = t.localtime()




    def stop(self):
        
        if not len(self.begin):
            print '未开始计时'
            
        else:           
            self.end = t.localtime()
        


    def _calc(self):
        for i in range(6):
            self.tesp = self.end[i] - self.begin[i]
            if self.tesp != 0:
                self.tcalc = self.tcalc +str(self.tesp) + self.unit[i]
        self.begin = []
        self.end = []
        return self.tcalc



mytime = MyTimer()
mytime.start()
t.sleep(3)
mytime.stop()
mytime.stop()
print mytime
