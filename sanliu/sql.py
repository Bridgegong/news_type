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

    def select(self, link):
        self.cur = self.conn.cursor()  # connection.cursor()：返回一个游标对象，该对象可以用于查询并从数据库中获取结果。
        a = "select count(1) from news_types where Url='%s'" %(link)
        self.cur.execute(a)
        row = self.cur.fetchall()  # 将查询结果返回成一个元组（列表）
        print(row[0][0])
        return row[0][0]

    def saves(self, urls,date_times, name,  contents):
        print(urls)
        print(date_times)
        print(name)
        print(contents)
        sql = "insert into news_types(Url,DateTime,Title,Content,Types,Forms) VALUES ('%s','%s','%s','%s','%s','%s')" % (urls, date_times, name, contents, '融资事件', '36氪')
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)

    # def Laiyuan(self,area,laiyuan):
    #     # area = str(area)
    #     # laiyuan = str(laiyuan)
    #     if area == laiyuan:
    #         return '现有建设用地'
    #     elif laiyuan ==0:
    #         return '新增建设用地'
    #     else:
    #         return '新增建设用地(来自存量库)'

    def md5(self,strs):
        m = hashlib.md5()
        m.update(strs.encode("utf8"))
        return m.hexdigest()

# create table ChinaLand(ID int not null,AdminRegion varchar(255),ElectronicId varchar(255),ProjectName varchar(255),ProjectSeat varchar(255),Acreage varchar(255),LandSources varchar(255),LandUse varchar(255),LandSupply varchar(255),LandUsageTerm varchar(255),ClassificationIndustry varchar(255),LandLevel varchar(255),TransactionPrice varchar(255),InstallmentPlan varchar(255),LandUser varchar(255),AgreedLimits varchar(255),AgreedLimit varchar(255),AgreedTime varchar(255),ScheduledStartTime varchar(255),ScheduledCompletionTime varchar(255),ActualStartTime varchar(255),ActualCompletionTime varchar(255),Approvers varchar(255),DateOfContract varchar(255),CURRENT_TIME timestamp not null default current_timestamp,PRIMARY KEY (ID))




