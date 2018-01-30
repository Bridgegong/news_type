# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 18:33
# @Author  : Bridge
# @Email   : 13722450120@163.com
# @File    : wangyicaijing.py
# @Software: PyCharm
import re, requests, time
from bs4 import BeautifulSoup
from news_type.wangyicaijing import sql
import json
class XinLang():
    def __init__(self):
        self.header = {'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
        self.save = sql.RuKu()

    def get_url(self, url):
        r = requests.get(url).text[14:-1]
        try:
            json_str = json.loads(r)
            for i in json_str:
                self.get_content(i['docurl'],i['title'])
        except Exception as e:
            print(e)
            pass
    def get_content(self, urls, title):
        if self.save.select(urls) == 0:
            bea = self.get_requests(urls)
            date_times = bea.find('div', 'post_time_source').text.split('来源:')[0].replace('\n','').replace('                ','')
            froms = bea.find('div', 'post_time_source').text.split('来源:')[1].replace('\n','')
            contents = bea.find('div', id="endText").text.replace('\n','').replace('                    ', '').replace("""(function(c){var x,d,g,s='script',w=window,n=c.name||'PLISTA';try{x=w.frameElement;w=x?w.top:w;}catch(e){}if(x){d=w.document.createElement('div');d.setAttribute(c.dataMode,'plista_widget_'+c.widgets[0].name||c.widgets[0]);x.parentNode.insertBefore(d,x);}if(!w[n]){w[n]=c;g=w.document.getElementsByTagName(s)[0];s=w.document.createElement(s);s.async=true;s.type='text/javascript';s.src=(w.location.protocol==='https:'?'https:':'http:')+'//static'+(c.origin?'-'+c.origin:'')+'.plista.com/async'+(c.name?'/'+c.name:'')+'.js';g.parentNode.insertBefore(s,g);}    }({     "publickey": "5cd03db33cec612ec6ac1a79",     "name": "PLISTA_OUTSTREAM",     "origin": "cn",     "dataMode": "data-display",     "noCache": true,     "widgets": [      "outstream"     ]    }));""",'').replace('''var newsFontSize = wwwstore.getItem("fontSize");          if (newsFontSize!=null && newsFontSize!=""){            $(".news_txt").addClass(newsFontSize).attr("data-size",newsFontSize);            $("#"+newsFontSize).addClass("on").siblings().removeClass("on");          }          var play = function(divId, url , defImg, w, h){            jwplayer(divId).setup({              flashplayer: "//file.thepaper.cn/www/v3/js/jwplayer.flash.swf",              file: url,              image: defImg,              width: w,              height: h            });          }          var playUrl = '',wrapperId='player_wrapper',$wrapper = $('#'+wrapperId);          if(playUrl){play(wrapperId,playUrl,'',$wrapper.width(),$wrapper.height())}''','').replace('''(function() {  var s = "_" + Math.random().toString(36).slice(2);  document.write('</p><p>');  (window.slotbydup=window.slotbydup || []).push({    id: '2475336',    container: s,    size: '300,250',    display: 'inlay-fix'  });})();''','')
            self.save.saves(urls, title, date_times, froms, contents)

    def get_requests(self, url):
        rep = requests.get('%s' % url)
        rep.encoding = rep.apparent_encoding
        bea = BeautifulSoup(rep.text, 'lxml')
        return bea

    def main(self):
        # for i in range(5, 200):
        #     url = 'http://money.163.com/special/002557NJ/chanjing_data_chanjing_0%d.js?callback=data_callback'%i
        url = 'http://money.163.com/special/002557NJ/chanjing_data_chanjing.js?callback=data_callback'
        self.get_url(url)

if __name__ == '__main__':
    while True:
        xl = XinLang().main()
        print('《政企合作》正在休息，请稍等…………')
        time.sleep(21600)


