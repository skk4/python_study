#-*- coding:utf-8 -*-
'''
求给你的年份是否是闰年
解题思路：
能被4整除，但不能被100整除 的数
'''
#_year = raw_input(">")
for _year in range(1900,2300):
    int_year = int(_year)
    if int_year%4 == 0 and int_year%100 !=0:
        print int_year
