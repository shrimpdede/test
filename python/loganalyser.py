#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

#[2016/05/06 07:34:16:609] SIU - SP - NORMAL - CNHSIU4PNCDrvUsb::SetGuideLight() - m_byGuidLightData[6] ==> 40, byData ==>  0

FORMAT_COMPILE = re.compile('\[(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}:\d{3})\] (\w+) - (\w+) - (\w+) - (.+) - (.+)')
ElementTypes = ('Time','Catagory', 'Layer', 'Level', 'Method', 'Content')
class Record(object):
    def __init__(self, OriginStr):
        self.OriginStr = OriginStr
        result = FORMAT_COMPILE.match(OriginStr)
        self.__dataMap={}
        if result != None:
            self.isNone = False
            rg=result.groups()
            for i in range(len(ElementTypes)):
                self.__dataMap[ElementTypes[i]] = rg[i] 
        else:
            self.isNone = True
    def __getattr__(self, name):
        if self.__dataMap.has_key(name):
            return self.__dataMap[name]
        return None
    def __str__(self):
        return self.OriginStr
    __repr__ = __str__
class LogFilter(object):
    def __init__(self):
        self.__filterMap={}
    '''
    filtertype includes ['equal','like','between']
    '''
    
    def addFilter(self, filtertype, key, *arge):
        if key not in ElementTypes:
            print 'key[%s] is not in ElementTypes' % key
            return False
        l = list(arge)
        l.insert(0,filtertype)
        self.__filterMap[key] = l
    def testRecord(self, record):
        if record.isNone:
            return False
        result = True
        for key,value in self.__filterMap.iteritems():
            result = result and self.testValue(getattr(record,key,""),*value)
            if not result:
                break
        return result
    def testValue(self, value, *arge):
        if arge[0]=='equal':
            return value == arge[1]
            pass
        if arge[0]=='like':
            ret= value.upper().find(arge[1].upper())
            return ret!=-1
        if arge[0]=='between':
            return value>=arge[1] and value<=arge[2]
        return False
    def __str__(self):
        return str(self.__filterMap)
    __repr__ = __str__
class LogFile(object):
    def __init__(self, filename):
        self.filename = filename
    def OutputLogAfterFilter(self, logfilter):
        fin = open(self.filename, 'r')
        fout = open('Output_'+self.filename, 'w')
        for line in fin:
            r = Record(line)
            if logfilter.testRecord(r):
                fout.write(str(r))
                fout.flush()
        fout.close()
        fin.close()
    
if __name__ == '__main__':
    f = LogFilter()
    f.addFilter('between','Time', '2016/05/05 00:10:30:898', '2016/05/05 00:12:30:898')
    lf = LogFile('test.txt')
    lf.OutputLogAfterFilter(f)