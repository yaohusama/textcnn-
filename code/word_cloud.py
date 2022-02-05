from tfidf_textrank import get_data
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import pickle
'''绘制词云图，使用tfidf_textrank.py生成的keywords'''
bar_width = 0.5
data= ''
max_words=100
#可以修改为sentence_neg.txt，以观察所有样本的关键词
f=open('data/sentence.txt','r',encoding="utf-8")
for i in f:
    data+=f.read()
keywords=get_data(data,max_words)
print(str(len(keywords))+"条")
print(keywords)
pickle.dump(keywords,open("data/keyword.pkl","wb"))
image= Image.open('data/background.png')
graph = np.array(image)
wc = WordCloud(font_path='simfang.ttf',background_color='White',max_words=max_words,mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)#设置背景图像
plt.imshow(wc)  #画图
plt.imshow(wc.recolor(color_func=image_color))  #根据背景图片着色
plt.axis("off") #不显示坐标轴
plt.show()
wc.to_file('data/output.png')
