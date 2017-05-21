#! -*- coding:utf8 -*-

import sys

sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')

from smc_algorithm import JaroWinklerSimilar, CosineSimilar, PhoneSimilar, SphericalDistance
from smc_config import ALL_SOURCES

from smc_config import (
    # 电话阀值
    phone_threshold,
    # 属性权重
    name_weight,
    address_weight,
    distance_weight,
    # 名称匹配得分配置
    eleme_baidu_name,
    eleme_dianping_name,
    eleme_meituan_name,
    # 地址匹配得分配置
    eleme_baidu_address,
    eleme_dianping_address,
    eleme_meituan_address,
    # 经纬度距离
    eleme_baidu_distance,
    eleme_dianping_distance,
    eleme_meituan_distance,
)

def calc_shop_similar_score(eleme_shop, other_shop, other_source):
    ps = PhoneSimilar(eleme_shop.phones, other_shop.phones)
    phone_score = ps.calc_similar() # 使用 电话匹配度 算法

    if phone_score >= phone_threshold:
        return phone_score
    else:
        name_score = calc_shop_name_similar(eleme_shop.name, other_shop.name, other_source)
        address_score = calc_shop_address_similar(eleme_shop.address, other_shop.address, other_source)
        distance_score = calc_shop_distance_similar(eleme_shop.latitude, eleme_shop.longitude, other_shop.latitude, other_shop.longitude, other_source)
        print 'name[%s], address[%s]. distance[%s]' % (name_score, address_score, distance_score)

        return name_score*name_weight + address_score*address_weight + distance_score*distance_weight


def calc_shop_name_similar(eleme_name, other_name, other_source):
    jw = JaroWinklerSimilar(eleme_name, other_name)
    similar_score = jw.jarowinkler_similar() # 使用 JaroWinkler 相似度算法

    one_source = ALL_SOURCES[other_source]
    
    return get_smc_name_score(similar_score, one_source) # 获取经过阀值重新计算之后的名称分数


def calc_shop_address_similar(eleme_address, other_address, other_source):
    cs = CosineSimilar(eleme_address, other_address)
    similar_score = cs.calc_similar() # 使用 CosineSimilar 相似度算法

    one_source = ALL_SOURCES[other_source]

    return get_smc_address_score(similar_score, one_source) # 获取经过阀值重新计算之后的地址分数


def calc_shop_distance_similar(eleme_lat, eleme_lnt, other_lat, other_lnt, other_source):
    sd = SphericalDistance(eleme_lnt, eleme_lat, other_lnt, other_lat)
    distance = sd.calc_distance() # 计算 两点球面距离

    one_source = ALL_SOURCES[other_source]

    return get_smc_distance_score(distance, one_source) # 获取经过阀值重新计算之后的距离分数


def get_smc_name_score(similar_score, one_source):
    score_step =  eval('eleme_%s_name' % one_source['pinyin'])
    for one_step in score_step:
        condition = '%s %s %s and %s %s %s' % (one_step['max_score'], '>=' if one_step['max_include'] else '>', similar_score, one_step['min_score'], '<=' if one_step['min_include'] else '<', similar_score)
        if eval(condition):
            return one_step['return_score']


def get_smc_address_score(similar_score, one_source):
    score_step =  eval('eleme_%s_address' % one_source['pinyin'])
    for one_step in score_step:
        condition = '%s %s %s and %s %s %s' % (one_step['max_score'], '>=' if one_step['max_include'] else '>', similar_score, one_step['min_score'], '<=' if one_step['min_include'] else '<', similar_score)
        if eval(condition):
            return one_step['return_score']


def get_smc_distance_score(distance, one_source):
    distance_step = eval('eleme_%s_distance' % one_source['pinyin'])
    for one_step in distance_step:
        condition = '%s %s %s and %s %s %s' % (one_step['max_distance'], '>=' if one_step['max_include'] else '>', distance, one_step['min_distance'], '<=' if one_step['min_include'] else '<', distance)
        if eval(condition):
            step_distance = one_step['max_distance'] - one_step['min_distance']
            step_score = one_step['return_min_score'] - one_step['return_max_score']
            distance_ratio = (distance - one_step['max_distance']) * 1.0 / step_distance
            return one_step['return_min_score'] - distance_ratio * step_score 


