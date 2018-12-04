#!/usr/bin/python
# coding: utf-8
import sqlite3, time, datetime

def createOriginalDatabase():
    conn = sqlite3.connect('i_can_i_bb.db')
    conn.text_factory = str
    cursor = conn.cursor()
    # 需要解析的数据表
    # cursor.execute(
        # 'create table comments(id varchar, movieId varchar, name varchar(40), comment TEXT, gender varchar, addTime varchar(20))')
    # 原始数据表
    cursor.execute('create table originalData(id varchar, movieId varchar, originalInfo TEXT, movieName TEXT)')
    cursor.close()
    conn.commit()
    conn.close()

def createDealDatabase():
    conn = sqlite3.connect('deal_data.db')
    conn.text_factory = str
    cursor = conn.cursor()
    createTable = """CREATE TABLE `realData` (
	`id`	varchar,
	`content`	TEXT,
	`gender`	varchar,
	`addDate`	TEXT,
	`uname`	TEXT,
	`uid`	TEXT,
	`msgId`	TEXT,
	`uidType`	TEXT
);"""
    # 需要解析的数据表
    cursor.execute(createTable)
    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # 只能创建一次
    createOriginalDatabase()
    createDealDatabase()


