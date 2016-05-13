#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

#[2016/05/06 07:34:16:609] SIU - SP - NORMAL - CNHSIU4PNCDrvUsb::SetGuideLight() - m_byGuidLightData[6] ==> 40, byData ==>  0

FORMAT_COMPILE = re.compile('\[(\d{4})/(\d{2})/(\d{2}) (\d{2}):(\d{2}):(\d{2}):(\d{3})\] (\w+) - (\w+) - (\w+) - (.+) - (.+)')
ElementTypes = ('Time_year', 'Time_month', 'Time_day', 'Time_hour', 'Time_minute', 'Time_second',
    'Catagory', 'Layer', 'Level', 'Method', 'Content'
)
class Record(object):
    def __init__(self, OriginStr):
        result = FORMAT_COMPILE.match(OriginStr)
        self.__dataMap={}
        if result != None:
            rg=result.groups()
            for i in range(len(ElementTypes)):
                self.__dataMap[ElementTypes[i]] = rg[i]
            print self.__dataMap
    def setFilter(**kw):        
    def __getattr__(self, name):
        if self.__dataMap.has_key(name):
            return self.__dataMap[name]
        return None
if __name__ == '__main__':
    Record('[2016/05/06 07:34:16:609] SIU - SP - NORMAL - CNHSIU4PNCDrvUsb::SetGuideLight() - m_byGuidLightData[6] ==> 40, byData ==>  0')
    print ElementTypes
