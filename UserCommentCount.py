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
	movieIdData = data.groupby(['movieId'])
	commentDataCount = movieIdData["movieId"].agg([ "count"])
	commentDataCount.reset_index(inplace=True)
	print commentDataCount
	movies = {
		"1629260900":u"第22期",
		"1629256800":u"第21期",
		"1596058300":u"第20期",
		"1596046700":u"第19期",
		"1560634500":u"第18期",
		"1560624600":u"第17期",
		"1530507600":u"第16期",
		"1530502000":u"第15期",
		"1500872700":u"第14期",
		"1500744900": u"第13期",
		"1467027700":u"第12期",
		"1467020800":u"第11期",
		"1447221500":u"第10期",
		"1443620200":u"第9期",
		"1421444400":u"第8期",
		"1415151600":u"第7期",
		"1398481500":u"第6期",
		"1395871500":u"第5期",
		"1376903200":u"第4期",
		"1373596700":u"第3期",
		"1355605500":u"第2期",
		"1352316900":u"第1期"
	}
	attr = [movies[commentDataCount["movieId"][i]] for i in range(0, commentDataCount.shape[0])]
	v1 = [commentDataCount["count"][i] for i in range(0, commentDataCount.shape[0])]
	bar = Bar("评论数量")
	bar.add("数量",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
			xaxis_interval=0,is_splitline_show=True,is_label_show=True)
	bar.render("html/comment_count.html")	
	conn.commit()
	conn.close()