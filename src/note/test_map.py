# -*-coding:utf-8 -*-
numblist2 = [1, 3, 5, 7,'hello']
numblist1 = (1, 'I', 'love', 'you', 4, 8)
f = lambda x: x*2
print map(f, numblist2)
print map(f, numblist1)
#返回列表[2, 6, 10, 14, 'hellohello']
#返回列表[2, 'II', 'lovelove', 'youyou', 8, 16]