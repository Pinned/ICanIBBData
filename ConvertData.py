#!/usr/bin/python
# coding: utf-8
import random
import json
import io
import datetime,time
import sqlite3
import sys

def saveRealItem(id, originalData):
	user = json.loads(originalData)
	conn = sqlite3.connect('deal_data.db')
	conn.text_factory = str
	cursor = conn.cursor()
	ins="insert into realData values (?,?,?,?,?,?,?,?)"
	content = ""
	if user.has_key("content"):
		content = user["content"]
	v = (id, content, user["userInfo"]["gender"], user["addTime"], user["userInfo"]["uname"], user["userInfo"]["uid"], user["id"], user["userInfo"]["uidType"])
	cursor.execute(ins, v)
	cursor.close()
	conn.commit()
	conn.close()

## 转换数据
if __name__ == '__main__':
	conn = sqlite3.connect('i_can_i_bb.db')
	conn.text_factory = str
	cursor = conn.cursor()
	cursor.execute("select * from originalData")
	values = cursor.fetchall()
	for item in values:
		saveRealItem(item[0], item[2])
	cursor.close()
	conn.commit()
	conn.close()
	