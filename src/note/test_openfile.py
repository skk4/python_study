# -*- coding:gbk -*-
f = open("d:\\record.txt", 'r')
boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] !='======':
        role, line_spoken = each_line.split('：', 1)
        if role == '小甲鱼':
            boy.append(line_spoken)
            #file_name_boy = 'boy' + str(count) +'.txt'
            #f_boy =open('d:\\%s' %file_name_boy, 'w')
            #f_boy.writelines(boy)
            #f_boy.close()
            
        if role == '小客服':
            girl.append(line_spoken)
            #file_name_girl = 'girl' + str(count) +'.txt'
            #f_girl =open('d:\\%s' %file_name_girl, 'w')
            #f_girl.writelines(girl)
            #f_girl.close()
    elif each_line[:6] =='======' :
        print girl
        print boy
        print each_line
                
print girl
print boy
            
            
        