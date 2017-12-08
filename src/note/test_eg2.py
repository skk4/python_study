# -*- coding:utf-8 -*-
import easygui as g
while 1:
    guess = g.multenterbox(msg='【*真实姓名】为必填项\n【*手机号码】为必填项\n【*E-mail】为必填项', 
                       title='账号中心', fields=('*用户名:','*真实姓名', '固定电话', '*手机号码', 'QQ', '*E-mail'), 
                       values=())
    
    print guess[0].strip() or guess[1].strip() or guess[3] or guess[5]
    if guess[0].strip() and guess[1].strip() and guess[3] and guess[5] != '':
        print guess
        break

