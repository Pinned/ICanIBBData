#!/usr/bin/python
# coding: utf-8
import random
import json
import io
import datetime,time
import sqlite3
import sys


def updateMovieId(): 
    conn = sqlite3.connect('deal_data.db')
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("select * from realData")
    values = cursor.fetchall()
    cursor.close()
    for item in values:
        sql = "UPDATE `realData` SET `movieId`=\""+item[0].split("_")[0]+ "\" WHERE `id`=\"" + item[0] + "\""
        print sql
        cc = conn.cursor()
        cc.execute(sql)
        cc.close()
    conn.commit()
    conn.close()

## 转换数据
if __name__ == '__main__':
	updateMovieId()
	