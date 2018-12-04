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
	genderData = data.groupby(['gender'])
	rateDataCount = genderData["id"].agg([ "count"])
	rateDataCount.reset_index(inplace=True)
	print rateDataCount
	attr = ["女", "男"]
	v1 = [rateDataCount["count"][i] for i in range(0, rateDataCount.shape[0])]
	pie = Pie("性别比例")
	pie.add("", attr, v1, is_label_show=True)
	pie.render("html/gender.html")
	conn.commit()
	conn.close()