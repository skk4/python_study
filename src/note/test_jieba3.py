# -*- coding:utf-8 -*-
import jieba
import jieba.analyse as ay
'''
setence ="我来到北京清华大学"

setence1 ="我是一只小小鸟"
#
seg_list = jieba.cut(setence, cut_all = True )
print "Full Mode:", ' '.join(seg_list)

seg_list = jieba.cut(setence, cut_all = False )
print "Default Mode:", ' '.join(seg_list)


seg_list = jieba.cut_for_search(setence)
print "Search Mode:", ' '.join(seg_list)




for i in list(seg_list):
    print i.encode('utf-8')
   

'''   

#jieba.load_userdict('dict_sans.txt') 

with open("sans.txt", "r") as f:
    setence = f.read()
    print setence
 
#搜索关键字  ,显示热度高的关键字 
word_dict = {}
for x, y in ay.extract_tags(setence, 200, withWeight=True) :
    word_dict[x] =  int(y*1000)     
    
