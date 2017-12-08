# -*- coding: utf-8 -*-
import jieba
import codecs
import jieba.posseg as pseg
novel_role = [u'白浅' ,u'白止', u'白真', u'白奕' ,u'白玄', u'离镜 ',u'令羽' ,
              u'玄女 ',u'少辛' ,u'夜华' ,u'墨渊',u'折颜' ,u'素锦' ,u'凤九', 
              u'桑籍', u'糯米', u'元贞' ,u'天君 ',u'团子', u'帝君' ,u'阿离' ,
              u'西海 ', u'素素', u'姑姑', u'司音']
lineNames = []
node_dict = {} 
relationships ={}
jieba.load_userdict("dict_sans.txt")
with codecs.open('sans.txt', 'r') as f:
    #print f.readlines()
    i = 0
    for line in f.readlines():
        
        #print line
        i = i+1

        psg = pseg.cut(line)#对小说每一行进行分词
        lineNames.append([])
        #print lineNames
        for w in  psg:
            #print w, w.flag, w.word
            if w.flag != 'nr' or len(w.word)<2 or len(w.word)>= 3:
                #print w, w.flag, w.word
                continue
            
            #print w.flag, w.word
            
            if w.word in novel_role: 
                #print lineNames
                #print w.flag, w.words
                #同个角色名多个称呼归类到一个名字   
                if w.word == u'素素' or w.word == u'姑姑' or w.word == u'司音':
                    lineNames[-1].append(u'白浅')
                    
                elif w.word == u'糯米' or w.word == u'团子' :
                    lineNames[-1].append(u'阿离')       
                else:
                    lineNames[-1].append(w.word)#添加角色到对应行列表内
                node_dict.setdefault(w.word, 0)#初始化角色字典
                relationships.setdefault(w.word, {})#初始化角色关系字典
                #print relationships
                #同个角色名多个称呼归类到一个名字                
                if w.word == u'姑姑' or w.word == u'素素' or w.word == u'司音':
                    node_dict[u'白浅'] = node_dict[u'白浅'] + 1
                    
                elif w.word == u'糯米' or w.word == u'团子':
                    node_dict[u'阿离'] = node_dict[u'阿离']  + 1  
                else:
                    node_dict[w.word] = node_dict[w.word] + 1#字典内统计角色出现次数，没出现1次+1
      
        #print '第%s行' %i 
print '总共%s行' %i   
#print lineNames
node_dict.pop(u'姑姑')#剔除同名角色字段
node_dict.pop(u'素素') 
node_dict.pop(u'司音')
node_dict.pop(u'糯米')
node_dict.pop(u'阿离')
node_dict.pop(u'团子')
with codecs.open('sans_node_list.txt', 'w', 'utf-8') as f:             
    for x in node_dict:
        f.write(x + ' ' + str(node_dict[x])+ '\r\n')#保存角色文件



for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
                     
            relationships[name1].setdefault(name2, 1) 
            relationships[name1][name2] =  relationships[name1][name2] + 1

    
with codecs.open('sans_edge_list.txt', 'w', 'utf-8') as f:                    
    for x in relationships:
        for y in relationships[x]:
            if relationships[x][y]>3:
                f.write( x + ' '+ y + ' '+ str(relationships[x][y]) + '\r\n') # 保存角色关系文件             