# -*- coding:utf-8 -*-
import easygui as g
import random
secret = random.randint(1, 10)
print secret
count = 0
while 1:   
    guess = g.integerbox('请输入数字：', title='猜数字', default='', lowerbound=1, upperbound=10)
    #guess = input('请输入数字：')
    if guess == secret:
        g.msgbox('恭喜，你猜对了！')
        #print '恭喜，你猜对了！'
        break        
    else:
        count = count + 1
        g.msgbox('很遗憾，你第%d没猜中' %count)
        #print '很遗憾，你第%d没猜中' %count
        if count >= 3:
            g.msgbox('超过%d次，退出游戏'%count)
            #print '超过%d次，退出游戏'%count
            break    
    
    