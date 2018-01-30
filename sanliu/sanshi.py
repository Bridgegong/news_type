# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 10:52
# @Author  : Bridge
# @Email   : 13722450120@163.com
# @File    : sanshi.py
# @Software: PyCharm
import sys
sys.path.append(r'D:\ZHiYin')
sys.path.append(r'D:\python3.6\Lib\site-packages')
import requests
from news_type.sanliu import sql
from bs4 import BeautifulSoup
import time
import json


class SanSHiLiu():
    def __init__(self):
        self.save = sql.RuKu()

    def get_url(self, url):
        try:
            r = requests.get(url)
            json_str = json.loads(r.text)
            for i in json_str['data']['items']:
                self.save.saves(i['news_url'],i['published_at'],i['title'],i['description'])
        except Exception as e:
            f = open('errors.txt', 'a', encoding='utf-8')
            f.write('%s\n' % e)
            f.close()

    def get_con(self):
        pass

    def get_requests(self, url):
        rep = requests.get('%s' % url)
        rep.encoding = rep.apparent_encoding
        bea = BeautifulSoup(rep.text, 'lxml')
        return bea

    def main(self):
        for i in range(76101,100659):
            print(i)
            url = 'http://36kr.com/api/newsflash?b_id=%d' % i
            self.get_url(url)

if __name__ == '__main__':
    san = SanSHiLiu().main()