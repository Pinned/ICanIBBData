#!/usr/bin/env python
#!-*-coding:utf-8 -*-
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
	data = pd.read_sql("select content from realData where content like '%李诞%' or content like '%李蛋%' or content like '%蛋蛋%'", conn)
	comment = jieba.cut(str(data["content"]), cut_all=False)
	wl_space_split = " ".join(comment)
	backgroudImage = np.array(Image.open(r"/Users/zhaocheng/Downloads/qipashuo.jpg"))
	stopword = STOPWORDS.copy()
	stopword.add(u"李诞")
	stopword.add(u"李蛋")
	stopword.add(u"蛋蛋")
	stopword.add(u"教授")
	stopword.add(u"高晓松")
	stopword.add(u"这个")
	stopword.add(u"就是")
	stopword.add(u"真的")
	stopword.add(u"说话")
	stopword.add(u"节目")
	wc = WordCloud(width=1920, height=1080, background_color='white',
				   mask=backgroudImage,
				   font_path="/Users/zhaocheng/Documents/Deng.ttf",
				   stopwords=stopword, max_font_size=400,
				   random_state=50)
	wc.generate_from_text(wl_space_split)
	plt.imshow(wc)
	plt.axis("off")
	wc.to_file('lidan_word_cloud1.png')