# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel(r'D:\danxia_house\xm.xls',  sheetname=0)
df_xm = pd.DataFrame(df)
print df_xm
#print df

regoin = list(set(df_xm[u'小区'].values))
print '小区：\n', regoin

for each_regoin in regoin:
    print '小区:' , each_regoin
regoin_number = len(regoin)
print '小区总数：%d' % regoin_number    
x = df[df[u'小区']==u'鑫塔水尚'][u'单价']
print '鑫塔水尚单价:', x
x_min = x.min()
x_max = x.max()
x_mean = x.mean()
print x_min
print x_max
print x_mean
