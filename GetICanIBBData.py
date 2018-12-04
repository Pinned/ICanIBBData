#!/usr/bin/python
# coding: utf-8
import requests
import random
import json
import io
import datetime,time
import sqlite3
import sys


def saveMoveInfoToFile(movieId, movieName, lastId):
    url = "http://sns-comment.iqiyi.com/v3/comment/get_comments.action?"
    params = {
        "types":"time",
        "business_type":"17",
        "agent_type":"119",
        "agent_version":"9.9.0",
        "authcookie":"847FnsUHQ7HBoXOUiSm2WfUyjup8YW8UL2sEonbGKoSm2cBSJpSokg6lm2DYVm1Cim15Cov22"
    }
    if lastId != "":
        params["last_id"] =  lastId
    for item in params:
        url = url + item + "=" + params[item] + "&"
    url = url + "content_id=" + movieId
    try:
        responseTxt = getMoveinfo(url)
        returnLastId = parseData(movieId, movieName, responseTxt)
        if returnLastId == "-1":
            print "==============="
            print movieName
            print url
            print "==============="
            time.sleep(1)
            print("isEnd")
        else: 
            time.sleep(0.5)
            saveMoveInfoToFile(movieId, movieName, returnLastId)
    except Exception as e:
        print("exception:" + e.message)
        time.sleep(0.5)
        saveMoveInfoToFile(movieId, movieName, lastId)
    
def parseData(movieId, movieName, htmlContent):
    data = json.loads(htmlContent)['data']['comments']
    lastId = "-1"
    if json.dumps(data) == "[]":
        return lastId
    lastId = "-1"
    for item in data:
        originalData = json.dumps(item)
        saveOriginalDataToDatabase(item["id"], movieId, movieName, originalData)
        lastId = item['id']
    return lastId
        
def saveOriginalDataToDatabase(msgId, movieId, movieName, originalData):
    conn = sqlite3.connect('i_can_i_bb.db')
    conn.text_factory = str
    cursor = conn.cursor()
    ins="insert into originalData values (?,?,?,?)"
    v = (movieId+ "_" + msgId, movieId, originalData, movieName)
    cursor.execute(ins, v)
    cursor.close()
    conn.commit()
    conn.close()
    
def getMoveinfo(url):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Accept": "application/json",
        "Referer": "http://m.iqiyi.com/v_19rqriflzg.html",
        "Origin": "http://m.iqiyi.com",
        "Host": "sns-comment.iqiyi.com",
        "Connection": "keep-alive",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6",
        "Accept-Encoding": "gzip, deflate"
    }
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


## 获取原始数据
if __name__ == '__main__':
    print("start main")
    movies = {
        "1629260900":u"第22期 马薇薇飙泪“致离别”",
        "1629256800":u"第21期 周冬雨爆料马思纯家很有钱 陈铭1v1开杠首次落败",
        "1596058300":u"第20期 高晓松年轻时像吴亦凡？马薇薇黄执中开杠抱头痛哭",
        "1596046700":u"第19期 李诞首度下场开杠蔡康永 邱晨自带PPT辩论遭吐槽",
        "1560634500":u"第18期 马东高晓松开杠互拆套路 李诞“黑粉上位”成主持",
        "1560624600":u"第17期 蔡康永薛兆丰参战针锋相对 陈铭詹青云学霸大乱斗",
        "1530507600":u"第16期 董岩磊回忆被骂上热搜",
        "1530502000":u"第15期 李诞池子爆笑互怼",
        "1500872700":u"第14期 陈铭放大招引邱晨驳斥",
        "1500744900": u"第13期 如晶结辩听哭梁洛施",
        "1467027700":u"第12期 蔡康永薛兆丰挖坑互怼",
        "1467020800":u"第11期 陈铭灵魂拷问催泪全场",
        "1447221500":u"第10期 颜如晶首曝暗恋情史",
        "1443620200":u"第9期 吴谨言尔晴附体掌掴肖骁",
        "1421444400":u"第8期 肖骁催泪发言感染全场",
        "1415151600":u"第7期 毛不易为马东包扎遭吐槽",
        "1398481500":u"第6期 肖骁马薇薇上演教练对决",
        "1395871500":u"第5期 陈铭花希极限攻防战",
        "1376903200":u"第4期 臧鸿飞首曝离婚净身出户",
        "1373596700":u"第3期 如晶走心讲述听哭高晓松",
        "1355605500":u"第2期 新奇葩剑走偏锋压制如晶",
        "1352316900":u"第1期 李诞下跪求蔡康永原谅"
    }
    for item in movies:
        saveMoveInfoToFile(item, movies[item] ,"")