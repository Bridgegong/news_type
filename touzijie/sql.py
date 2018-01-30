# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 17:46
# @Author  : Bridge
# @Email   : 13722450120@163.com
# @File    : sql.py
# @Software: PyCharm
import pymysql
import hashlib
class RuKu():

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', db='zhiyin', user='root', passwd='123456', charset='utf8')
        self.cur = self.conn.cursor()
        if self.cur:
            print("连接成功")
        else:
            print("连接失败")

    def select(self, title_url):
        self.cur = self.conn.cursor()  # connection.cursor()：返回一个游标对象，该对象可以用于查询并从数据库中获取结果。
        a = "select count(1) from news_types where Url='%s'" %(title_url)
        self.cur.execute(a)
        row = self.cur.fetchall()  # 将查询结果返回成一个元组（列表）
        print(row[0][0])
        return row[0][0]

    def saves(self, urls, title, date_times, content):
        print(title)
        print(date_times)
        print(urls)
        print(content)
        sql = "insert into news_types(DateTime,Url,Title,Content,Types,Forms) VALUES ('%s','%s','%s','%s','%s','%s')" % (date_times,urls,title,content,'融资事件','投资界')
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)



