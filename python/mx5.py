#!/usr/bin/env python
# -*- coding=utf-8 -*-
import urllib, urllib2,re,time
from HTMLParser import HTMLParser
_AMOUNT_ = re.compile(r'"articleAmount":"(\d+)"')
class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__bRecord = False
    def handle_starttag(self, tag, attrs): 
        if tag == 'script':
            self.__bRecord = True
    def handle_endtag(self, tag):
        pass
    def handle_startendtag(self, tag, attrs):
        pass
    def handle_data(self, data):
        if self.__bRecord:
            str = data.strip()
            if str.startswith('var GoodsArticleAmount'):
                #print str
                retlist = _AMOUNT_.findall(str)
                total = 0
                for value in retlist:
                    v = int(value[0])
                    total += v
                if total!=0 :
                    print '”–ªı¿≤°£°£'+'\a\a\a\a'
                    print time.strftime('%Y-%m-%d %X', time.localtime( time.time()))

            self.__bRecord = False

    def handle_comment(self, data):
        pass
    def handle_entityref(self, name):
        pass
    def handle_charref(self, name):
        pass


if __name__ == '__main__':
    print 'xiaomi 4note!'

    htmlparser = MyHtmlParser();
  #  time.sleep(3)

    for i in range(1000000):
            html = urllib.urlopen('http://www.10010.com/goodsdetail/111505266841.html')
            htmlparser = MyHtmlParser();
            time.sleep(3)
            htmlparser.feed(html.read().decode('UTF-8'))