# -*- coding:utf-8 -*-
print "{!s}".format('2')  
print "{!r}".format('2')
#返回结果：2
#返回结果：'2'
print zip('<^>', ['letf', 'center', 'right'])
#[('<', 'letf'), ('^', 'center'), ('>', 'right')]
for align, text in zip('<^>', ['letf', 'center', 'right']):
    #print align, text
    #print '--------------------------------------------------'
    print '{0:{fill}{align}16}'.format(text, fill=align, align=align)
'''
返回结果
letf<<<<<<<<<<<<
^^^^^center^^^^^
>>>>>>>>>>>right 
'''
   
octets = [192, 168, 0, 1]  
print '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
#C0A80001
_ = 'C0A80001'
print int('C0A80001', 16)

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