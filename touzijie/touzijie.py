# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 13:25
# @Author  : Bridge
# @Email   : 13722450120@163.com
# @File    : touzijie.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
from news_type.touzijie import sql
import time

class TouZiJie():
    def __init__(self):
        self.header = {'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
        self.save = sql.RuKu()
    def get_url(self, url):
        try:
            r = self.get_requests(url)
            title_url = r.find('ul', id="newslist-all").find_all('li')
            for i in title_url:
                title_urls = (i.find('a')['href'])
                self.get_content(title_urls)
        except Exception as e:
            print(e)
            pass

    def get_content(self, title_urls):
        print(title_urls)
        if self.save.select(title_urls) == 0:
            url = self.get_requests(title_urls)
            try:
                title = url.find('h1', id="newstitle").text
                date_time = url.find('span','date').text
                con = url.find('div', id="news-content")
                time.sleep(1)
                self.save.saves(title_urls, title, date_time, con.text)
            except Exception as e:
                pass

    def get_requests(self, url):
        rep = requests.get('%s' % url)
        rep.encoding = rep.apparent_encoding
        bea = BeautifulSoup(rep.text, 'lxml')
        return bea

    def main(self):
        for i in range(1,6):
            url = 'http://pe.pedaily.cn/%s/'%i
            self.get_url(url)

if __name__ == '__main__':
    while True:
        tzj = TouZiJie().main()
        print('《融资事件》正在休息，请稍等…………')
        time.sleep(21600)