# -*- coding:utf-8 -*-
import jieba
import jieba.analyse as ay
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#结巴中文分词，三种模式
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
#读取文本
with open("sans.txt", "r") as f:
    setence = f.read()
    #print setence
 
#搜索关键字  ,显示热度高的关键字 及对应热度值，最好得到字典
word_dict = {}
for x, y in ay.extract_tags(setence, 200, withWeight=True) :
    word_dict[x] =  int(y*10000)
         
#设置中文字体
fontname = r'C:\\Windows\\Fonts\\msyh.ttf'
#back_ground = imread('hhb.jpg')
#设置自定义背景图
back_ground = np.array(Image.open('alice_color.png'))
#生成自定义背景图颜色
image_colors = ImageColorGenerator(back_ground)
#生成云标签
wc = WordCloud(background_color="white", font_path=fontname, mask=back_ground,stopwords=STOPWORDS.add("said"),
random_state=42, scale= 2)
wc.generate_from_frequencies(word_dict)
plt.imshow(wc)
#去除坐标
plt.axis('off')
#保存图片
wc.to_file('wordcloud1.png')

plt.figure()# 创建的2张图
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
wc.to_file('wordcloud2.png')

#plt.figure()
#plt.imshow(back_ground,cmap='gray')
#plt.axis('off')

plt.show()
        