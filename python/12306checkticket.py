#!/usr/bin/env python
# -*- coding: utf-8 -*-

import HTMLParser,re,urllib,urllib2,json,ssl
import time
def checktickets(datas):
    if datas is None:
        return False
    totaltickets = 0
    for dataitem in datas:
        if dataitem['ze_num']!='нч'.decode('GBK') and dataitem['ze_num']!='--' :
            print 'There is %4s ticket(s) in Train number %5s --- start time %s' % (dataitem['ze_num'], dataitem['station_train_code'], dataitem['start_time'])
            totaltickets += int(dataitem['ze_num'])
    if totaltickets != 0:
        print 'totaltickets is %d' % totaltickets
        return True
    return False
            
if __name__ == '__main__':
    print 'Tickets check'
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s' % ('2016-02-04','BJP','DIP')
    print url
    for i in range(1000000):
        url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s' % ('2016-02-03','BJP','DIP')
        try:
            jsonstr = urllib2.urlopen(url)
            str = jsonstr.read().decode('UTF-8')
            data = json.loads(str)
            if data['data']!= None:
                ret = checktickets(data['data']['datas'])
                if ret:
                    print time.strftime('%Y-%m-%d %X', time.localtime( time.time()))
                    print '\a\a\a There\'re tickets in 2016-02-03'
                    time.sleep(3)
 
        except urllib2.HTTPError, e:
            print url
            print 'some HTTPError happened %s' % e.code
        except Exception, e:
            print  e
        url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s' % ('2016-02-04','BJP','DIP')
        try:
            jsonstr = urllib2.urlopen(url)
            str = jsonstr.read().decode('UTF-8')
            data = json.loads(str)
            if data['data']!= None:
                ret = checktickets(data['data']['datas'])
                if ret:
                    print time.strftime('%Y-%m-%d %X', time.localtime( time.time()))
                    print '\a\a\a There\'re tickets in 2016-02-04'
                    
        except urllib2.HTTPError, e:           
            print url
            print 'some urlerror happened %s' % e.code
        except  Exception, e:
            print  e
        time.sleep(3)    
