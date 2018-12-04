#!/usr/bin/python
# coding: utf-8
import random
import json
import io
import datetime,time
import sqlite3
import sys

def updateWeek():
    conn = sqlite3.connect('deal_data.db')
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("select * from realData")
    values = cursor.fetchall()
    cursor.close()
    for item in values:
        realTime = time.localtime(float(item[3]))
        realTime = time.strftime("%A",realTime)
        sql = "UPDATE `realData` SET `week`=\"" + realTime + "\" WHERE `id`=\"" + item[0] + "\""
        cc = conn.cursor()
        cc.execute(sql)
        cc.close()

    conn.commit()
    conn.close()
    time.localtime()


## 转换数据
if __name__ == '__main__':
	updateWeek()
	