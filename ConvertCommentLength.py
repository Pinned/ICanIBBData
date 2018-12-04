#!/usr/bin/python
# coding: utf-8
import sqlite3, time, datetime

def updateCommentLength():
    conn = sqlite3.connect('deal_data.db')
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute("select * from realData")
    values = cursor.fetchall()
    cursor.close()
    for item in values:
        content = item[1]
        length = 0
        if len(content) <= 20:
            length = 0
        elif len(content) > 20 and len(content) <= 50:
            length = 1
        elif len(content) > 50 and len(content) <= 100:
            length = 2
        else:
            length = 3
        sql = "UPDATE `realData` SET `length`=\"" + str(length) + "\" WHERE `id`=\"" + item[0] + "\""
        cc = conn.cursor()
        cc.execute(sql)
        cc.close()
    conn.commit()
    conn.close()
    time.localtime()

if __name__ == '__main__':
    updateCommentLength()


