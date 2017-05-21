#! -*- coding:utf8 -*-

import sys

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

from dao.models import (
    DomElemeRestaurantInfo,
    DomMeituanRestairamtInfo,
    DomDianpingRestairamtInfo,
    DomBaiduRestairamtInfo,
    DomRestaurantRelation,
    DomRestaurantNotRelation,

    LocalDomSession,
)

from utils import (
    MagicNums,
    ListUtils,
    StringUtils,
    MatplotlibUtils,
    NumUtils,
)

from calc.cosine_similar import CosineSimilar
from calc.jarowinkler_similar import JaroWinklerSimilar

local_dom_session = LocalDomSession()

analysis_attributes = ['name', 'address']
MAX_COUNT = 20000

file_path = '../files/images'

def draw_hist(all_similar_score, one_source, one_attribute):
    similar_calc = 'default'
    if one_attribute == 'name':
        similar_calc = 'JaroWinklerSimilar'
    elif one_attribute == 'address':
        similar_calc = 'CosineSimilar'
    else:
        raise Exception('无效属性 %s' % one_attribute)

    title = '%s-%s:%s-[%s]' % ('eleme', one_source['pinyin'], one_attribute, similar_calc)
    xlabel = 'similar score'
    ylabel = 'percentage'
    file = '%s/%s' % (file_path, title)

    MatplotlibUtils.draw_multi_histogram(all_similar_score, xlabel, ylabel, title, write_file_path=file)


def get_meituan_poi(meituan_poi_id):
    return local_dom_session.query(DomMeituanRestairamtInfo).filter(DomMeituanRestairamtInfo.meituan_id == meituan_poi_id).first()


def get_dianping_poi(dianping_poi_id):
    return local_dom_session.query(DomDianpingRestairamtInfo).filter(DomDianpingRestairamtInfo.dianping_id == dianping_poi_id).first()


def get_baidu_poi(baidu_poi_id):
    return local_dom_session.query(DomBaiduRestairamtInfo).filter(DomBaiduRestairamtInfo.baidu_id == baidu_poi_id).first()


def draw_eleme_other_attribute(one_source, poi, one_attribute):
    print '开始处理 %s - %s: %s' % ('eleme', one_source['pinyin'], one_attribute)

    get_other_poi_func = 'get_%s_poi' % one_source['pinyin']
    eleme_attribute_name = '%s_%s' % ('eleme', one_attribute)
    other_attribute_name = '%s_%s' % (one_source['pinyin'], one_attribute)
    source = one_source['source']

    limit = 100
    last_id = 0
    count = 0
    done = False
    
    similar_sorce_list = []

    # 开始处理相似数据
    while not done:
        relations = local_dom_session.query(DomRestaurantRelation)\
            .filter(DomRestaurantRelation.id > last_id)\
            .filter(DomRestaurantRelation.source == source)\
            .order_by(DomRestaurantRelation.id.asc())\
            .limit(limit).all()

        if ListUtils.isEmptyList(relations):
            break

        last_id = relations[len(relations)-1].id

        for relation in relations:
            eleme_poi_id = relation.eleme_poi_id
            other_poi_id = relation.other_poi_id

            eleme_poi = local_dom_session.query(DomElemeRestaurantInfo)\
                .filter(DomElemeRestaurantInfo.eleme_id == eleme_poi_id)\
                .first()
            other_poi = eval(get_other_poi_func)(other_poi_id)

            eleme_attribute_value = getattr(eleme_poi, eleme_attribute_name)
            other_attribute_value = getattr(other_poi, other_attribute_name)
            similar_socre = 0.0
            if one_attribute == 'name':
                jw = JaroWinklerSimilar(eleme_attribute_value, other_attribute_value)
                similar_socre = jw.jarowinkler_similar()
            elif one_attribute == 'address':
                cs = CosineSimilar(eleme_attribute_value, other_attribute_value)
                similar_socre = cs.calc_similar()
            else:
                raise Exception ('错误属性 %s' % one_attribute)
            similar_sorce_list.append(similar_socre)

            count += 1
            if count > MAX_COUNT:
                done = True
                break


    # 开始处理不相似数据
    limit = 100
    last_id = 0
    count = 0
    done = False

    not_similar_score_list = []

    while not done:
        not_relations = local_dom_session.query(DomRestaurantNotRelation)\
            .filter(DomRestaurantNotRelation.source == source)\
            .filter(DomRestaurantNotRelation.id > last_id)\
            .order_by(DomRestaurantNotRelation.id.asc())\
            .limit(limit).all()

        if ListUtils.isEmptyList(not_relations):
            break

        last_id = not_relations[len(not_relations)-1].id

        for not_relation in not_relations:
            eleme_poi_id = not_relation.eleme_poi_id
            other_poi_id = not_relation.other_poi_id

            eleme_poi = local_dom_session.query(DomElemeRestaurantInfo)\
                .filter(DomElemeRestaurantInfo.eleme_id == eleme_poi_id)\
                .first()
            other_poi = eval(get_other_poi_func)(other_poi_id)

            eleme_attribute_value = getattr(eleme_poi, eleme_attribute_name)
            other_attribute_value = getattr(other_poi, other_attribute_name)
            similar_socre = 0.0
            if one_attribute == 'name':
                jw = JaroWinklerSimilar(eleme_attribute_value, other_attribute_value)
                similar_socre = jw.jarowinkler_similar()
            elif one_attribute == 'address':
                cs = CosineSimilar(eleme_attribute_value, other_attribute_value)
                similar_socre = cs.calc_similar()
            else:
                raise Exception ('错误属性 %s' % one_attribute)
            not_similar_score_list.append(similar_socre)

            count += 1
            if count > MAX_COUNT:
                done = True
                break

    all_similar_score = (similar_sorce_list, not_similar_score_list)
    draw_hist(all_similar_score, one_source, one_attribute)


def draw_eleme_other(one_source, poi):
    for one_attribute in analysis_attributes:
        draw_eleme_other_attribute(one_source, poi, one_attribute)


def draw_attribute_threshold(one_source):
    poi = None
    if one_source['source'] == MagicNums.MEITUAN_SOURCE:
        poi = DomMeituanRestairamtInfo()
    elif one_source['source'] == MagicNums.DIANPING_SOURCE:
        poi = DomDianpingRestairamtInfo()
    elif one_source['source'] == MagicNums.BAIDU_SOURCE:
        poi = DomBaiduRestairamtInfo()
    else:
        raise Exception('无效source[%s]' % one_source)

    draw_eleme_other(one_source, poi)


def main():
    all_sources = MagicNums.ALL_SOURCES
    for one_source_key in all_sources:
        if all_sources[one_source_key]['source'] == MagicNums.ELEME_SOURCE:
            continue

        draw_attribute_threshold(all_sources[one_source_key])


if __name__ == '__main__':
    main()