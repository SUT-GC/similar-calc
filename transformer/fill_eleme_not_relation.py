#! -*- coding:utf8 -*-

import sys
import datetime

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

from dao.models import (
    DomTestSession,
    LocalDomSession,

    DomElemeRestaurantInfo,
    DomMeituanRestairamtInfo,
    DomBaiduRestairamtInfo,
    DomDianpingRestairamtInfo,
    DomRestaurantRelation,
    DomRestaurantNotRelation,
    
    DomPoi,
    DomExtDianpingRestaurant,
    DomExtBaiduRestaurant,
    DomExtMeituanRestaurant,
)

from utils import (
    NumUtils,
    StringUtils,
    ListUtils,
    MagicNums,
)

local_dom_session = LocalDomSession()


def get_meituan_id(other_poi_id):
    return local_dom_session.query(DomMeituanRestairamtInfo.id).filter(DomMeituanRestairamtInfo.meituan_id == other_poi_id).first()


def get_dianping_id(other_poi_id):
    return local_dom_session.query(DomDianpingRestairamtInfo.id).filter(DomDianpingRestairamtInfo.dianping_id == other_poi_id).first()


def get_baidu_id(other_poi_id):
    return local_dom_session.query(DomBaiduRestairamtInfo.id).filter(DomBaiduRestairamtInfo.baidu_id == other_poi_id).first()


def fill_one_data(eleme_poi_id, not_other_poi_id, source):
    drnr = DomRestaurantNotRelation()
    drnr.eleme_poi_id = eleme_poi_id
    drnr.other_poi_id = not_other_poi_id
    drnr.source = source
    drnr.is_valid = 1
    drnr.created_at = datetime.datetime.now()
    drnr.deleted_at = datetime.datetime.now()

    local_dom_session.add(drnr)
    local_dom_session.commit()


def fill_data(one_source, poi):
    print '开始填充 %s' % one_source['name']
    limit = 1000
    last_id = 0
    done = False
    count = 0
    poi_class = type(poi)
    source = one_source['source']
    other_poi_id_name = '%s_id' % one_source['pinyin']
    get_id_fun = 'get_%s_id' % one_source['pinyin']
    start_id = getattr(MagicNums,'%s_ID_START' % one_source['pinyin'].upper())
    end_id = getattr(MagicNums,'%s_ID_END' % one_source['pinyin'].upper())

    while not done:
        all_relations = local_dom_session.query(DomRestaurantRelation)\
            .filter(DomRestaurantRelation.id > last_id)\
            .filter(DomRestaurantRelation.source == source)\
            .order_by(DomRestaurantRelation.id.asc())\
            .limit(limit).all()

        if ListUtils.isEmptyList(all_relations):
            done = True
            break

        last_id = all_relations[len(all_relations)-1].id

        for one_relation in all_relations:
            eleme_poi_id = one_relation.eleme_poi_id
            other_poi_id = one_relation.other_poi_id
            source = one_relation.source
            other_id = eval(get_id_fun)(other_poi_id)
            not_relation_id = NumUtils.getRandomDischargeId(start_id, end_id, other_id)
            not_other_poi = local_dom_session.query(poi_class).get(not_relation_id)
            not_other_poi_id = getattr(not_other_poi, other_poi_id_name)

            fill_one_data(eleme_poi_id, not_other_poi_id, source)
            count += 1

            if count % 100 == 0:
                print '已经处理了 %s 数据' % count

    print '已经处理完所有数据 %s' % count


def dispose(one_source):
    poi = None
    if one_source['source'] == MagicNums.MEITUAN_SOURCE:
        poi = DomMeituanRestairamtInfo()
    elif one_source['source'] == MagicNums.DIANPING_SOURCE:
        poi = DomDianpingRestairamtInfo()
    elif one_source['source'] == MagicNums.BAIDU_SOURCE:
        poi = DomBaiduRestairamtInfo()
    else:
        raise Exception (u'无效SOURCE[%s]' % one_source)
    fill_data(one_source, poi)


def main():
    all_sources = MagicNums.ALL_SOURCES
    for source_key in all_sources:
        if all_sources[source_key]['source'] == MagicNums.ELEME_SOURCE:
            continue
        dispose(all_sources[source_key])


if __name__ == '__main__':
    main()



