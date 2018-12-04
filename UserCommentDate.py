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
	movieIdData = data.groupby(['week'])
	commentDataCount = movieIdData["week"].agg([ "count"])
	commentDataCount.reset_index(inplace=True)
	print commentDataCount
	weekInfo = {
		"Monday":u"周一",
		"Tuesday":u"周二",
		"Wednesday":u"周三",
		"Thursday":u"周四",
		"Friday":u"周五",
		"Saturday":u"周六",
		"Sunday":u"周日"
	}
	weeks = [
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday","Sunday"
	]
	attr = []
	v1 = []
	week_temp = [commentDataCount["week"][i] for i in range(0, commentDataCount.shape[0])]
	for item in weeks:
		attr.append(weekInfo[item])
		index = week_temp.index(item)
		v1.append(commentDataCount["count"][index])
	for aa in attr:
		print aa
#	
#	attr = [weekInfo[commentDataCount["week"][i]] for i in range(0, commentDataCount.shape[0])]
#	v1 = [commentDataCount["count"][i] for i in range(0, commentDataCount.shape[0])]
	bar = Line("天评论数量")
	bar.add("数量",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
			xaxis_interval=0,is_splitline_show=True,is_label_show=True)
	bar.render("html/comment_week_count.html")