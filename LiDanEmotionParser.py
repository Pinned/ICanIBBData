#!/usr/bin/python
#coding: utf-8
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from snownlp import SnowNLP

def emotionParser(*names):
    conn = conn = sqlite3.connect("deal_data.db")
    conn.text_factory = str
    cursor = conn.cursor()
    likeStr = ""
    for i in range(0, len(names)):
        likeStr = likeStr +  "like \"%" + names[i] + "%\" "
        if i + 1 < len(names):
            likeStr = likeStr + " or "
    print likeStr
    cursor.execute("select content from realData where content " + likeStr)
    values = cursor.fetchall()
    sentimentslist = []
    for item in values:
        # print SnowNLP(item[0].decode("utf-8")).words
        sentimentslist.append(SnowNLP(item[0].decode("utf-8")).sentiments)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor="#4F8CD6")  
    plt.xlabel("Sentiments Probability")                                       
    plt.ylabel("Quantity")                                                     
    plt.title("Analysis of Sentiments for Lidan")                                        
    plt.show()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    emotionParser("李诞")