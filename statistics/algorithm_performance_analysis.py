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
from calc.lcs_simillar import LCSSimilar
from calc.levenshtein_similar import LevenshteinSimilar

local_dom_session = LocalDomSession()

analysis_attributes = ['name', 'address']
MAX_COUNT = 10000

def get_all_algorithm_score(one_relation, poi, one_source, one_attribute):
    eleme_id = one_relation.eleme_poi_id
    other_id = one_relation.other_poi_id
    other_id_name = '%s_id' % one_source['pinyin']
    eleme_attribute_name = '%s_%s' % ('eleme', one_attribute)
    other_attribute_name = '%s_%s' % (one_source['pinyin'], one_attribute)
    
    other_poi = None
    if one_source['source'] == MagicNums.MEITUAN_SOURCE:
        other_poi = local_dom_session.query(DomMeituanRestairamtInfo)\
            .filter(DomMeituanRestairamtInfo.meituan_id == other_id)\
            .first()
    if one_source['source'] == MagicNums.DIANPING_SOURCE:
        other_poi = local_dom_session.query(DomDianpingRestairamtInfo)\
            .filter(DomDianpingRestairamtInfo.dianping_id == other_id)\
            .first()
    if one_source['source'] == MagicNums.BAIDU_SOURCE:
        other_poi = local_dom_session.query(DomBaiduRestairamtInfo)\
            .filter(DomBaiduRestairamtInfo.baidu_id == other_id)\
            .first()


    eleme_poi = local_dom_session.query(DomElemeRestaurantInfo)\
        .filter(DomElemeRestaurantInfo.eleme_id == eleme_id)\
        .first()

    str1 = getattr(other_poi, other_attribute_name)
    str2 = getattr(eleme_poi, eleme_attribute_name)
    str1 = StringUtils.deleteBrackets(str1)
    str2 = StringUtils.deleteBrackets(str2)

    # print eleme_id, other_id, one_source['name'], one_attribute, str1, str2

    cs = CosineSimilar(str1, str2)
    js = JaroWinklerSimilar(str1, str2)
    lcs = LCSSimilar(str1, str2)
    ls = LevenshteinSimilar(str1, str2)

    # cs_score, js_score, lcs_score, ls_score
    cs_score = cs.calc_similar()
    js_score = js.jarowinkler_similar()
    lcs_score = lcs.lcs_similar()
    ls_score = ls.levenshtein_similar()

    # print eleme_id, other_id, one_source['name'], one_attribute, cs_score, js_score, lcs_score, ls_score

    return cs_score, js_score, lcs_score, ls_score


def get_no_similar_score(eleme_poi, poi, one_source, one_attribute):
    relation_other_poi_id = local_dom_session.query(DomRestaurantRelation.other_poi_id)\
        .filter(DomRestaurantRelation.eleme_poi_id == eleme_poi.eleme_id)\
        .filter(DomRestaurantRelation.source == one_source['source'])\
        .first()

    other_poi = None
    meituan_random_id = NumUtils.getRandomId(1, 353799)
    dianping_random_id = NumUtils.getRandomId(1, 405496)
    baidu_random_id = NumUtils.getRandomId(167114, 436753)

    if relation_other_poi_id is None:
        if one_source['source'] == MagicNums.MEITUAN_SOURCE:
            other_poi = local_dom_session.query(DomMeituanRestairamtInfo)\
                .filter(DomMeituanRestairamtInfo.id == meituan_random_id)\
                .first()

        if one_source['source'] == MagicNums.DIANPING_SOURCE:
            other_poi = local_dom_session.query(DomDianpingRestairamtInfo)\
                .filter(DomDianpingRestairamtInfo.id == dianping_random_id)\
                .first()

        if one_source['source'] == MagicNums.BAIDU_SOURCE:
            other_poi = local_dom_session.query(DomBaiduRestairamtInfo)\
                .filter(DomBaiduRestairamtInfo.id == baidu_random_id)\
                .first()

    else:
        if one_source['source'] == MagicNums.MEITUAN_SOURCE:
            other_poi = local_dom_session.query(DomMeituanRestairamtInfo)\
                .filter(DomMeituanRestairamtInfo.meituan_id == relation_other_poi_id)\
                .first()
            relation_other_id = other_poi.id
            while True:
                meituan_random_id = NumUtils.getRandomId(1, 353799)
                if meituan_random_id != relation_other_id:
                    other_poi = local_dom_session.query(DomMeituanRestairamtInfo)\
                        .filter(DomMeituanRestairamtInfo.id == meituan_random_id)\
                        .first()
                break

        if one_source['source'] == MagicNums.DIANPING_SOURCE:
            other_poi = local_dom_session.query(DomDianpingRestairamtInfo)\
                .filter(DomDianpingRestairamtInfo.dianping_id == relation_other_poi_id)\
                .first()
            relation_other_id = other_poi.id
            while True:
                dianping_random_id = NumUtils.getRandomId(1, 405496)
                if dianping_random_id != relation_other_id:
                    other_poi = local_dom_session.query(DomDianpingRestairamtInfo)\
                        .filter(DomDianpingRestairamtInfo.id == dianping_random_id)\
                        .first()
                break
        if one_source['source'] == MagicNums.BAIDU_SOURCE:
            other_poi = local_dom_session.query(DomBaiduRestairamtInfo)\
                .filter(DomBaiduRestairamtInfo.baidu_id == relation_other_poi_id)\
                .first()
            relation_other_id = other_poi.id
            while True:
                baidu_random_id = NumUtils.getRandomId(167114, 436753)
                if baidu_random_id != relation_other_id:
                    other_poi = local_dom_session.query(DomBaiduRestairamtInfo)\
                        .filter(DomBaiduRestairamtInfo.id == baidu_random_id)\
                        .first()
                break

    eleme_poi_id = eleme_poi.eleme_id
    other_poi_id_name = '%s_id' % one_source['pinyin']
    other_poi_id = getattr(other_poi, other_poi_id_name)
    eleme_poi_attribute_name = '%s_%s' % ('eleme', one_attribute)
    other_poi_attribute_name = '%s_%s' % (one_source['pinyin'], one_attribute)
    str1 = getattr(eleme_poi, eleme_poi_attribute_name)
    str2 = getattr(other_poi, other_poi_attribute_name)

    str1 = StringUtils.deleteBrackets(str1)
    str2 = StringUtils.deleteBrackets(str2)
    
    # print eleme_poi_id, other_poi_id, one_source['name'], one_attribute, str1, str2
    
    cs = CosineSimilar(str1, str2)
    js = JaroWinklerSimilar(str1, str2)
    lcs = LCSSimilar(str1, str2)
    ls = LevenshteinSimilar(str1, str2)

    # cs_score, js_score, lcs_score, ls_score
    cs_score = cs.calc_similar()
    js_score = js.jarowinkler_similar()
    lcs_score = lcs.lcs_similar()
    ls_score = ls.levenshtein_similar()

    # print eleme_id, other_id, one_source['name'], one_attribute, cs_score, js_score, lcs_score, ls_score

    return cs_score, js_score, lcs_score, ls_score


def calc_one_attribute(poi, one_attribute, one_source):
    print "开始分析[%s - %s : %s]" % ('eleme', one_source['name'], one_attribute)

    attribute_name = '%s_%s' % (one_source['pinyin'], one_attribute)

    if attribute_name not in [x for x in dir(poi)]:
        raise Exception('%s 不存在 %s 属性' % (type(poi), attribute_name))

    cs_score_list = []
    js_score_list = []
    lcs_score_list = []
    ls_score_list = []

    cs_no_score_list = []
    js_no_score_list = []
    lcs_no_score_list = []
    ls_no_score_list = []

    limit = 100
    last_id = 0
    count = 0
    max_count = MAX_COUNT
    done = False
    while not done:

        relations = local_dom_session.query(DomRestaurantRelation)\
            .filter(DomRestaurantRelation.id > last_id)\
            .filter(DomRestaurantRelation.source == one_source['source'])\
            .order_by(DomRestaurantRelation.id.asc())\
            .limit(limit).all()

        if ListUtils.isEmptyList(relations):
            break

        last_id = relations[len(relations)-1].id

        for one_relation in relations:
            count += 1
            # print "已经分析[%s - %s : %s] %s 条" % ('eleme', one_source['name'], one_attribute, count)
            if count > max_count:
                done = True
                break;

            cs_score, js_score, lcs_score, ls_score = get_all_algorithm_score(one_relation, poi, one_source, one_attribute)
            
            cs_score_list.append(cs_score)
            js_score_list.append(js_score)
            lcs_score_list.append(lcs_score)
            ls_score_list.append(ls_score)

    limit = 100
    last_id = 0
    other_last_id = 0
    count = 0
    max_count = MAX_COUNT
    done = False
    while not done:
        eleme_pois = local_dom_session.query(DomElemeRestaurantInfo)\
            .filter(DomElemeRestaurantInfo.id > last_id)\
            .order_by(DomElemeRestaurantInfo.id.asc())\
            .limit(limit).all()

        if ListUtils.isEmptyList(eleme_pois):
            break

        last_id = eleme_pois[len(eleme_pois)-1].id

        for eleme_poi in eleme_pois:
            count += 1
            if count > max_count:
                done = True
                break;

            cs_no_score, js_no_score, lcs_no_score, ls_no_score = get_no_similar_score(eleme_poi, poi, one_source, one_attribute)

            cs_no_score_list.append(cs_no_score)
            js_no_score_list.append(js_no_score)
            lcs_no_score_list.append(lcs_no_score)
            ls_no_score_list.append(ls_no_score)


    print ListUtils.calc_avg(cs_score_list)-ListUtils.calc_avg(cs_no_score_list), ListUtils.calc_avg(js_score_list)-ListUtils.calc_avg(js_no_score_list), ListUtils.calc_avg(lcs_score_list)-ListUtils.calc_avg(lcs_no_score_list), ListUtils.calc_avg(ls_score_list)-ListUtils.calc_avg(ls_no_score_list)


def calc_attribute_score(poi, one_source):
    for one_attribute in  analysis_attributes:
        calc_one_attribute(poi, one_attribute, one_source)


def calc_avg_score(one_source):
    poi = None
    if one_source['source'] == MagicNums.MEITUAN_SOURCE:
        poi = DomMeituanRestairamtInfo()
    elif one_source['source'] == MagicNums.DIANPING_SOURCE:
        poi = DomDianpingRestairamtInfo()
    elif one_source['source'] == MagicNums.BAIDU_SOURCE:
        poi = DomBaiduRestairamtInfo()
    else:
        raise Exception('无效source:%s' % one_source)

    calc_attribute_score(poi, one_source)


def main():
    all_sources = MagicNums.ALL_SOURCES
    for one_source in all_sources:
        if all_sources[one_source]['source'] == MagicNums.ELEME_SOURCE:
            continue

        calc_avg_score(all_sources[one_source])

if __name__ == '__main__':
    main()