# -*- coding:utf-8 -*-
from wordcloud import WordCloud
import codecs
import matplotlib.pyplot as plt
#from scipy.misc import imread
from PIL import Image
import numpy as np

from wordcloud import ImageColorGenerator, STOPWORDS
#设置中文兼容 fontname
fontname = r'C:\\Windows\\Fonts\\msyh.ttf'
word_dict ={}
#读取文件用codecs 加'utf-8'
with codecs.open('sans_node_list.txt', 'r', 'utf-8') as f:
    for each_line in f:
        word_dict.setdefault(each_line.split()[0], 0)
        word_dict[each_line.split()[0]] = int(each_line.split()[1])
        

#back_ground = imread('hhb.jpg')
back_ground = np.array(Image.open('alice_color.png'))
image_colors = ImageColorGenerator(back_ground)
#设置中文兼容 fontname
wc = WordCloud(background_color="white", font_path=fontname, mask=back_ground,stopwords=STOPWORDS.add("said"),
random_state=42)
wc.generate_from_frequencies(word_dict)
plt.imshow(wc)
plt.axis('off')

plt.figure()# 创建的2张图
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')

#plt.figure()
#plt.imshow(back_ground,cmap='gray')
#plt.axis('off')

plt.show()
        
