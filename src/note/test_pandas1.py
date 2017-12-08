# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#整形索引
s = pd.Series([1, 3, 5,np.nan, 6, np.nan, 8])

my_date = pd.date_range('20170101', periods=6)
for each_date in my_date :
    each_date
    
    
rd = np.random.randn(6, 4) 
rd
df = pd.DataFrame(rd, index=my_date, columns=list('ABCD'))
#print df
df.head(2)
df_dict = pd.DataFrame({'A':1,
                        'B':pd.Timestamp('20130102'),
                        'C':pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D':np.array([3]*4, dtype='int32'),
                        'E':pd.Categorical(['test', 'train', 'test', 'train']),
                        'F':'foo'
                                      })   

print s
print s.dropna()
print s.fillna(0)
print s.fillna({0:111})