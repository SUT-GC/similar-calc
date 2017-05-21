#! -*- coding:utf8 -*-

import sys

sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')

ELEME_SOURCE = 0
MEITUAN_SOURCE = 1
DIANPING_SOURCE = 2
BAIDU_SOURCE = 3

ALL_SOURCES = [
    {
        'pinyin':'eleme',
        'name':u"饿了么",
        'source':ELEME_SOURCE,
    },
    {
        'pinyin':'meituan',
        'name':u"美团外卖",
        'source':MEITUAN_SOURCE,
    },
    {
        'pinyin':'dianping',
        'name':u"点评外卖",
        'source':DIANPING_SOURCE,
    },
    {
        'pinyin':'baidu',
        'name':u"百度外卖",
        'source':BAIDU_SOURCE,
    }
]

# 电话匹配分数阀值 score >= phone_threshold 确认匹配，否则继续进行别属性匹配
phone_threshold = 1.0 

# 店铺各种属性的权重
name_weight = 0.5
address_weight = 0.3
distance_weight = 0.2

# 店铺的名称，地址在匹配分数段上对应的得分
eleme_baidu_name = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.5,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.5,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_baidu_address = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.9,
    },
    {
        'min_score':0.4,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.3,
        'min_include':False,
        'max_score':0.4,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.3,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_meituan_name = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.5,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.5,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_meituan_address = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.9,
    },
    {
        'min_score':0.4,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.3,
        'min_include':False,
        'max_score':0.4,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.3,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_dianping_name = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.5,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.5,
        'max_include':True,
        'return_score':0.0,
    },
]

eleme_dianping_address = [
    {
        'min_score':0.8,
        'min_include':False,
        'max_score':1.0,
        'max_include':True,
        'return_score':1.0,
    },
    {
        'min_score':0.6,
        'min_include':False,
        'max_score':0.8,
        'max_include':True,
        'return_score':0.9,
    },
    {
        'min_score':0.4,
        'min_include':False,
        'max_score':0.6,
        'max_include':True,
        'return_score':0.8,
    },
    {
        'min_score':0.3,
        'min_include':False,
        'max_score':0.4,
        'max_include':True,
        'return_score':0.6,
    },
    {
        'min_score':0.0,
        'min_include':True,
        'max_score':0.3,
        'max_include':True,
        'return_score':0.0,
    },
]


# 店铺 经纬度距离 和对应的得分
eleme_meituan_distance = [
    {
        'max_distance':100,
        'max_include':True,
        'return_max_score':0.9,
        'min_distance':0,
        'min_include':True,
        'return_min_score':1.0,
    },
    {
        'max_distance':200,
        'max_include':True,
        'return_max_score':0.8,
        'min_distance':100,
        'min_include':False,
        'return_min_score':0.9,
    },
    {
        'max_distance':300,
        'max_include':True,
        'return_max_score':0.6,
        'min_distance':200,
        'min_include':False,
        'return_min_score':0.8,
    },
    {
        'max_distance':400,
        'max_include':True,
        'return_max_score':0.5,
        'min_distance':300,
        'min_include':False,
        'return_min_score':0.6,
    },
    {
        'max_distance':1000,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':400,
        'min_include':False,
        'return_min_score':0.5,
    },
    {
        'max_distance':sys.maxint,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':1000,
        'min_include':False,
        'return_min_score':0.0,
    },
]

eleme_dianping_distance = [
    {
        'max_distance':100,
        'max_include':True,
        'return_max_score':0.9,
        'min_distance':0,
        'min_include':True,
        'return_min_score':1.0,
    },
    {
        'max_distance':200,
        'max_include':True,
        'return_max_score':0.8,
        'min_distance':100,
        'min_include':False,
        'return_min_score':0.9,
    },
    {
        'max_distance':300,
        'max_include':True,
        'return_max_score':0.6,
        'min_distance':200,
        'min_include':False,
        'return_min_score':0.8,
    },
    {
        'max_distance':400,
        'max_include':True,
        'return_max_score':0.5,
        'min_distance':300,
        'min_include':False,
        'return_min_score':0.6,
    },
    {
        'max_distance':1000,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':400,
        'min_include':False,
        'return_min_score':0.5,
    },
    {
        'max_distance':sys.maxint,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':1000,
        'min_include':False,
        'return_min_score':0.0,
    },
]

eleme_baidu_distance = [
    {
        'max_distance':200,
        'max_include':True,
        'return_max_score':0.3,
        'min_distance':0,
        'min_include':True,
        'return_min_score':0.5,
    },
    {
        'max_distance':300,
        'max_include':True,
        'return_max_score':0.7,
        'min_distance':200,
        'min_include':False,
        'return_min_score':0.9,
    },
    {
        'max_distance':400,
        'max_include':True,
        'return_max_score':0.9,
        'min_distance':300,
        'min_include':True,
        'return_min_score':1.0,
    },
    {
        'max_distance':500,
        'max_include':True,
        'return_max_score':0.5,
        'min_distance':400,
        'min_include':False,
        'return_min_score':0.7,
    },
    {
        'max_distance':1000,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':500,
        'min_include':False,
        'return_min_score':0.5,
    },
    {
        'max_distance':sys.maxint,
        'max_include':True,
        'return_max_score':0.0,
        'min_distance':1000,
        'min_include':False,
        'return_min_score':0.0,
    },
]
