#!/usr/bin/python
#coding: utf-8
from wordcloud import WordCloud,STOPWORDS
import pandas as pd 
from PIL import Image
import numpy as np
import jieba
import matplotlib.pyplot as plt 
#import seaborn as sns
from pyecharts import Geo,Style,Line,Bar,Overlap,Map
import io, sqlite3
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
	conn = sqlite3.connect('deal_data.db')
	conn.text_factory = str
	data = pd.read_sql("select * from realData", conn)
	jieba.add_word("马薇薇", freq = 20000, tag = None)
	comment = jieba.cut(str(data["content"]),cut_all=False)
	wl_space_split = " ".join(comment)
	backgroudImage = np.array(Image.open(r"/Users/zhaocheng/Downloads/qipashuo.jpg"))
	stopword = STOPWORDS.copy()
	stopword.add(u"奇葩")
	stopword.add(u"一部")
	stopword.add(u"第一")
	stopword.add(u"现在")
	stopword.add(u"只有")
	stopword.add(u"这个")
	stopword.add(u"选手")
	stopword.add(u"前排")
	stopword.add(u"一个")
	stopword.add(u"没有")
	stopword.add(u"什么")
	stopword.add(u"有点")
	stopword.add(u"感觉")
	stopword.add(u"无名之辈")
	stopword.add(u"就是")
	stopword.add(u"觉得")
#	.add('一部').add('一个').add('没有').add('什么').add('有点').add('感觉').add('无名之辈').add('就是').add('觉得')
	wc = WordCloud(width=1920,height=1080,background_color='white',
		mask=backgroudImage,
		font_path="/Users/zhaocheng/Documents/Deng.ttf",
		stopwords=stopword,max_font_size=400,
		random_state=50)
	wc.generate_from_text(wl_space_split)
	plt.imshow(wc)
	plt.axis("off")
	wc.to_file('html/unknow_word_cloud.png')
	
	
	conn.commit()
	conn.close()
	# recolor wordcloud and show
	# we could also give color_func=image_colors directly in the constructor
	# 我们还可以直接在构造函数中直接给颜色
	# 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
#	plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#	plt.axis("off")
#	plt.figure()
#	plt.imshow(backgroud_Image, cmap=plt.cm.gray, interpolation="bilinear")
#	plt.axis("off")
#	plt.show()
		
	#
#	wc.generate_from_text(wl_space_split)
#	plt.imshow(wc)
#	plt.axis('off')#不显示坐标轴  
#	plt.show()
#	wc.to_file(r'laji.jpg')