# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
#导入图表库以进行图表绘制
import matplotlib.pyplot as plt
loandata=pd.DataFrame(pd.read_excel('loan_data.xls'))
#设置日期字段issue_d为loandata数据表索引字段
loandata = loandata.set_index('issue_d')
#按月对贷款金额loan_amnt求均值，以0填充空值
loan_plot=loandata['loan_amnt'].resample('M').fillna(0)
#图表字体为华文细黑，字号为15
plt.rc('font', family='STXihei', size=15)
#创建一个一维数组赋值给a
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#创建折线图，数据源为按月贷款均值，标记点，标记线样式，线条宽度，标记点颜色和透明度
plt.plot(loan_plot,'g^',loan_plot,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
#添加x轴标签
plt.xlabel('月份')
#添加y周标签
plt.ylabel('贷款金额')
#添加图表标题
plt.title('分月贷款金额分布')
#添加图表网格线，设置网格线颜色，线形，宽度和透明度
plt.grid( color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
#设置数据分类名称
plt.xticks(a, ('1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月') )
#输出图表
plt.show()
