# -*- coding:utf-8 -*-
import easygui as g
import sys
def openfile(path):
    f = open(path, 'r')
    text = f.read().decode('gbk')
    print text
    f.close()
    return text

def savefile(path, text):
    f = open(path, 'w')
    f.write(text.encode('gbk'))
    f.close()


dir_path = g.fileopenbox('请选择文件', title='显示文件内容')
text = openfile(dir_path)
gtext = g.textbox(msg=u'文件[%s]内容如下：'%dir_path, title=u'显示文件内容', 
          text=text, codebox=0)

if text != gtext and gtext != None:
    gbutton = g.buttonbox(msg='检查到文件发生改变,请选择以下操作', title='警告', 
                choices=['覆盖保存', '放弃保存', '另存为...'])
    
    if gbutton== '覆盖保存':
        savefile(dir_path, gtext)
       
    elif gbutton == '另存为...':
        gfilesave = g.filesavebox(msg='请输入保存文件名', title='文件另存为', default='*.txt')
        savefile(gfilesave, gtext)
                      
    else:
        sys.exit(0)                    
else:
    sys.exit(0)

