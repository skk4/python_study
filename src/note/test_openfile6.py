# -*- coding:gbk -*-

def replace_file(file_name, old, new):
    f1 = open(file_name, 'r')
    count = 0
    content = []
    for each_line in f1:
        count = count + each_line.count(old)
        #print count
        each_line = each_line.replace(old, new)
        #each_line = each_line.replace('谢尚记', '小甲鱼')
        content.append(each_line)
    f1.close()  
    print '''文件%s中共有%d个【%s】
您确定要把所有的【%s】替换成【%s】吗？''' %(file_name, count, old, old, new)                            
    
    decide = raw_input("YES/NO:")
    
    if decide == 'YES':                         
        f2 = open(file_name, 'w')
        f2.writelines(content)
        f2.close()
 
 
file_name = raw_input("文件名：")
old = raw_input("需替换的文字：")
new = raw_input("替换成：")
     
replace_file(file_name, old, new)    