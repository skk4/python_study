# -*- coding:gbk -* -
def savefile(count, filename, role):
    file_name = '%s' %filename +str(count) +'.txt'
    f = open('d:\\%s' %file_name, 'w')
    f.writelines(role)
    f.close()
    

f = open("d:\\record.txt", 'r')
boy = []
girl = []
file_list = []
count = 1
for each_line in f:
    if each_line[:6]!='======' :
        role, line_spoken = each_line.split("��", 1)
        if role == 'С����':
            boy.append(line_spoken)
        if role == 'С�ͷ�':
            girl.append(line_spoken)
        
    else:
        '''
        file_name_boy = 'boy' + str(count) + '.txt'
        file_name_girl = 'girl' + str(count) + '.txt'

        file_boy = open("d:\\%s" %file_name_boy, 'w')
        file_girl = open("d:\\%s" %file_name_girl, 'w')
        file_boy.writelines(boy)
        file_girl.writelines(girl)
        file_boy.close()
        file_girl.close()
        '''
        savefile(count, 'boy', boy)
        savefile(count, 'girl', girl)
        count=count +1
        #���֮ǰ��һ�ε�file_list����գ���Ȼfile_list���ݻ��ǵ�1��+��2�� 
        boy = []
        girl = []
    savefile(count, 'boy', boy)
    savefile(count, 'girl', girl)   
        
    '''
    file_name_boy = 'boy' + str(count) + '.txt'
    file_name_girl = 'girl' + str(count) + '.txt'

    file_boy = open("d:\\%s" %file_name_boy, 'w')
    file_girl = open("d:\\%s" %file_name_girl, 'w')
    file_boy.writelines(boy)
    file_girl.writelines(girl)
    file_boy.close()
    file_girl.close()
    '''
        