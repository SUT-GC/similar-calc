#! -*-coding:utf8-*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

ELEME_SOURCE = 0
MEITUAN_SOURCE = 1
DIANPING_SOURCE = 2
BAIDU_SOURCE = 3

ALL_SOURCES = {
    'eleme':{
        'pinyin':'eleme',
        'name':u"饿了么",
        'source':ELEME_SOURCE,
    },
    'meituan':{
        'pinyin':'meituan',
        'name':u"美团外卖",
        'source':MEITUAN_SOURCE,
    },
    'dianping':{
        'pinyin':'dianping',
        'name':u"点评外卖",
        'source':DIANPING_SOURCE,
    },
    'baidu':{
        'pinyin':'baidu',
        'name':u"百度外卖",
        'source':BAIDU_SOURCE,
    }
}

ELEME_ID_START = 176118
ELEME_ID_END = 476120
MEITUAN_ID_START = 1
MEITUAN_ID_END = 353799
DIANPING_ID_START = 1
DIANPING_ID_END = 405496
BAIDU_ID_START = 167114
BAIDU_ID_END = 436753


if __name__ == '__main__':
    for x in ALL_SOURCES:
        print ALL_SOURCES[x]