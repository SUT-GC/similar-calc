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
        'name':"饿了么",
        'source':ELEME_SOURCE,
    },
    'meituan':{
        'pinyin':'meituan',
        'name':"美团外卖",
        'source':MEITUAN_SOURCE,
    },
    'dianping':{
        'pinyin':'dianping',
        'name':"点评外卖",
        'source':DIANPING_SOURCE,
    },
    'baidu':{
        'pinyin':'baidu',
        'name':"百度外卖",
        'source':BAIDU_SOURCE,
    }
}


if __name__ == '__main__':
    for x in ALL_SOURCES:
        print ALL_SOURCES[x]