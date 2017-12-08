#-*- coding:gbk -*-
def file_seek(filename, rowrange):
    f = open(filename, 'r')
    i = 0
    rowrange_list = rowrange.split(':')
    if rowrange_list[0]== '':
        rowend = int(rowrange_list[1])
        for each_line in f:
            i = i + 1
            if i<= rowend:
                print each_line
        
    elif rowrange_list[1] == '' :
        rowstart = int(rowrange_list[0])
        for each_line in f:
            i = i + 1
            if i>= rowstart:
                print each_line 
                
    elif rowrange_list[1] != '' and rowrange_list[0] != '' :
        rowstart = int(rowrange_list[0])
        rowend = int(rowrange_list[1])
        for each_line in f:
            i = i + 1
            if rowstart<=i<= rowend:
                print each_line
                
    else:
        for each_line in f:
            print each_line
                     
                      
    
    f.close()   
    
    
file_seek('some.txt', ':')