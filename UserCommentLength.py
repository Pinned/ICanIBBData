#!/usr/bin/python
#coding: utf-8
from wordcloud import WordCloud,STOPWORDS
import pandas as pd 
import jieba
import matplotlib.pyplot as plt 
#import seaborn as sns
from pyecharts import Geo,Style,Line,Bar,Overlap,Map, Pie
import io
import sqlite3


if __name__ == '__main__':
	conn = sqlite3.connect('deal_data.db')
	conn.text_factory = str
	data = pd.read_sql("select * from realData", conn)
	lengthData = data.groupby(['length'])
	lengthDataCount = lengthData["movieId"].agg([ "count"])
	lengthDataCount.reset_index(inplace=True)
	print lengthDataCount

	attr = ["20字以内", "20~50字", "50~100字", "100字以上"]
	v1 = [lengthDataCount["count"][i] for i in range(0, lengthDataCount.shape[0])]
	bar = Line("评论字数")
	bar.add("数量",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
			xaxis_interval=0,is_splitline_show=True,is_label_show=True)
	bar.render("html/comment_word_count.html")
	
	conn.commit()
	conn.close()