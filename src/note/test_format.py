# -*- coding:utf-8 -*-
#通过位置来填充字符串
print 'hello {0} i am {1}'.format('Kevin','Tom')
#返回结果：hello Kevin i am Tom

print 'hello {} i am {}'.format('Kevin','Tom')
#返回结果：hello Kevin i am Tom

print 'hello {0} i am {1} . myname is {0}'.format('Kevin','Tom')
#返回结果：hello Kevin i am Tom . myname is Kevin

#通过key来填充
print 'hello {name1}  i am {name2}'.format(name1='Kevin',name2='Tom')
#返回结果：hello Kevin i am Tom

#通过列表下标填充(位置，key)
names=['Kevin','Tom']
print 'hello {names[0]}  i am{names[1]}'.format(names=names)                
#返回结果：hello Kevin i am Tom

print 'hello {0[0]}  i am {0[1]}'.format(names)
#返回结果：hello Kevin i am Tom

#通过字典的key
names={'name':'Kevin','name2':'Tom'}
print 'hello {names[name]}  i am {names[name2]}'.format(names=names)
#返回结果：hello Kevin i am Tom

#通过对象的属性
class Names():
    name1='Kevin'
    name2='Tom'
print 'hello {names.name1}  iam {names.name2}'.format(names=Names)
#返回结果：hello Kevin i am Tom

#使用魔法参数
args=['lu']
kwargs = {'name1': 'Kevin', 'name2': 'Tom'}
print 'hello {name1} {} i am {name2}'.format(*args, **kwargs)  
# 返回结果：hello Kevin lu i am Tom

#转义{和}符号,跟%中%%转义%一样，formate中用两个大括号来转义
print '{{ {0} }}'.format('Kevin')
#返回结果：{ Kevin }

#format作为函数
f = 'hello {0} i am {1}'.format    
print f('Kevin','Tom')
#返回结果：hello Kevin i am Tom

#格式化datetime
import datetime
now = datetime.datetime.now()
print '{:%Y-%m-%d %X}'.format(now)

#内嵌用法
print 'hello {0:>{1}} '.format('Kevin',10)
#返回结果：hello      Kevin 

#叹号的用法，！后面可以加s r a 分别对应str() repr() ascii()
#差别就是repr带有引号，str()是面向用户的，目的是可读性，
#repr()是面向Python解析器的，返回值表示在python内部的含义
print "{!s}".format('2')  
print "{!r}".format('2')  
#返回结果：2
#返回结果：'2'
 
'''
格式转换
b、d、o、x分别是二进制、十进制、八进制、十六进制。

 

数字                               格式                    输出                                描述
3.1415926      {:.2f}     3.14         保留小数点后两位
3.1415926      {:+.2f}    3.14         带符号保留小数点后两位
-1             {:+.2f}    -1           带符号保留小数点后两位
2.71828        {:.0f}     3            不带小数
1000000        {:,}       1,000,000    以逗号分隔的数字格式
0.25           {:.2%}     25.00%       百分比格式
1000000000     {:.2e}     1.00E+09     指数记法
25             {0:b}      11001        转换成二进制
25             {0:d}      25           转换成十进制
25             {0:o}      31           转换成八进制
25             {0:x}      19           转换成十六进制



对齐与填充
数字             格式            输出         描述
5     {:0>2}    05    数字补零 (填充左边, 宽度为2)
5     {:x<4}    5xxx  数字补x (填充右边, 宽度为4)
10    {:x^4}    x10x  数字补x (填充右边, 宽度为4)
13    {:10}     13    右对齐 (默认, 宽度为10)
13    {:<10}    13    左对齐 (宽度为10)
13    {:^10}    13    中间对齐 (宽度为10)    
'''

width = 5
end =''
for num in range(5,6):
    for base in 'dXob':
        print '{0:{width}{base}}'.format(num, base=base, width=width)
    print end      