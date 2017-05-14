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

dom_test_session = DomTestSession()
local_dom_session = LocalDomSession()


def fill_one_baidu_restaurant(eleme_id, baidu_poi):
    if baidu_poi is None:
        return

    if eleme_id is None or eleme_id <= 0:
        return

    has_relation = local_dom_session.query(DomRestaurantRelation).filter(DomRestaurantRelation.eleme_poi_id == eleme_id).filter(DomRestaurantRelation.other_poi_id == baidu_poi.shop_id).filter(DomRestaurantRelation.source == MagicNums.BAIDU_SOURCE).all()
    if has_relation is not None and len(has_relation) > 0:
        print "已经存在关联关系[eleme_id:%s, baidu_id:%s]" % (eleme_id, baidu_poi.shop_id)
        return

    baidus = local_dom_session.query(DomBaiduRestairamtInfo).filter(DomBaiduRestairamtInfo.baidu_id == baidu_poi.shop_id).all()
    
    if baidus is None or len(baidus) <= 0:
        baidu = DomBaiduRestairamtInfo()
        baidu.baidu_id = baidu_poi.shop_id
        baidu.baidu_name = baidu_poi.shop_name
        baidu.baidu_branch_name = baidu_poi.fendian_name
        baidu.baidu_address = baidu_poi.address
        baidu.baidu_phone = baidu_poi.shop_phone
        baidu.baidu_latitude = baidu_poi.eleme_lat
        baidu.baidu_longitude = baidu_poi.eleme_lng
        baidu.baidu_logo_hash = baidu_poi.logo
        baidu.baidu_is_value = 1
        baidu.created_at = datetime.datetime.now()
        baidu.updated_at = datetime.datetime.now()
        local_dom_session.add(baidu)

    relation = DomRestaurantRelation()
    relation.eleme_poi_id = eleme_id
    relation.other_poi_id = baidu_poi.shop_id
    relation.source = MagicNums.BAIDU_SOURCE
    relation.is_valid = 1
    relation.created_at = datetime.datetime.now()
    relation.updated_at = datetime.datetime.now()
    local_dom_session.add(relation)

    print "填充[饿了么:%s - 百度:%s]" % (eleme_id, baidu_poi.shop_id)

    local_dom_session.commit()


def fill_one_meituan_restaurant(eleme_id, meituan_poi):
    if meituan_poi is None:
        return

    if eleme_id is None or eleme_id <= 0:
        return

    has_relation = local_dom_session.query(DomRestaurantRelation).filter(DomRestaurantRelation.eleme_poi_id == eleme_id).filter(DomRestaurantRelation.other_poi_id == str(meituan_poi.shop_id)).filter(DomRestaurantRelation.source == MagicNums.MEITUAN_SOURCE).all()
    if has_relation is not None and len(has_relation) > 0:
        print "已经存在关联关系[eleme_id:%s, meituan_id:%s]" % (eleme_id, meituan_poi.shop_id)
        return

    meituans = local_dom_session.query(DomMeituanRestairamtInfo).filter(DomMeituanRestairamtInfo.meituan_id == str(meituan_poi.shop_id)).all()
    
    if meituans is None or len(meituans) <= 0:
        meituan = DomMeituanRestairamtInfo()
        meituan.meituan_id = meituan_poi.shop_id
        meituan.meituan_name = meituan_poi.shop_name
        meituan.meituan_branch_name = meituan_poi.fendian_name
        meituan.meituan_address = meituan_poi.address
        meituan.meituan_phone = meituan_poi.call_center
        meituan.meituan_latitude = meituan_poi.eleme_lat
        meituan.meituan_longitude = meituan_poi.eleme_lng
        meituan.meituan_logo_hash = meituan_poi.pic_url
        meituan.meituan_is_value = 1
        meituan.created_at = datetime.datetime.now()
        meituan.updated_at = datetime.datetime.now()
        local_dom_session.add(meituan)

    relation = DomRestaurantRelation()
    relation.eleme_poi_id = eleme_id
    relation.other_poi_id = meituan_poi.shop_id
    relation.source = MagicNums.MEITUAN_SOURCE
    relation.is_valid = 1
    relation.created_at = datetime.datetime.now()
    relation.updated_at = datetime.datetime.now()
    local_dom_session.add(relation)

    print "填充[饿了么:%s - 美团:%s]" % (eleme_id, meituan_poi.shop_id)

    local_dom_session.commit()


def fill_one_dianping_restaurant(eleme_id, dianping_poi):
    if dianping_poi is None:
        return

    if eleme_id is None or eleme_id <= 0:
        return

    has_relation = local_dom_session.query(DomRestaurantRelation).filter(DomRestaurantRelation.eleme_poi_id == eleme_id).filter(DomRestaurantRelation.other_poi_id == str(dianping_poi.restaurant_id)).filter(DomRestaurantRelation.source == MagicNums.DIANPING_SOURCE).all()
    if has_relation is not None and len(has_relation) > 0:
        print "已经存在关联关系[eleme_id:%s, dianping_id:%s]" % (eleme_id, dianping_poi.restaurant_id)
        return

    dianpings = local_dom_session.query(DomDianpingRestairamtInfo).filter(DomDianpingRestairamtInfo.dianping_id == str(dianping_poi.restaurant_id)).all()

    if dianpings is None or len(dianpings) <= 0:
        dianping = DomDianpingRestairamtInfo()
        dianping.dianping_id = dianping_poi.restaurant_id
        dianping.dianping_name = dianping_poi.restaurant_name
        dianping.dianping_branch_name = dianping_poi.fendian_name
        dianping.dianping_address = dianping_poi.address
        dianping.dianping_phone = dianping_poi.telphone
        dianping.dianping_latitude = dianping_poi.lat
        dianping.dianping_longitude = dianping_poi.lng
        dianping.dianping_logo_hash = dianping_poi.logurl
        dianping.dianping_is_value = 1
        dianping.created_at = datetime.datetime.now()
        dianping.updated_at = datetime.datetime.now()
        local_dom_session.add(dianping)

    relation = DomRestaurantRelation()
    relation.eleme_poi_id = eleme_id
    relation.other_poi_id = dianping_poi.restaurant_id
    relation.source = MagicNums.DIANPING_SOURCE
    relation.is_valid = 1
    relation.created_at = datetime.datetime.now()
    relation.updated_at = datetime.datetime.now()
    local_dom_session.add(relation)

    print "填充[饿了么:%s - 点评:%s]" % (eleme_id, dianping_poi.restaurant_id)

    local_dom_session.commit()


def main():
    limit = 100
    last_id = 0
    count = 0
    print "开始填充关联表数据 [%s]" % datetime.datetime.now()

    while True:
        eleme_restaurants = local_dom_session.query(DomElemeRestaurantInfo).filter(DomElemeRestaurantInfo.id > last_id).order_by(DomElemeRestaurantInfo.id.asc()).limit(limit).all()

        if eleme_restaurants is None or len(eleme_restaurants) <= 0:
            break

        last_id = eleme_restaurants[len(eleme_restaurants) - 1].id

        for eleme_restaurant in eleme_restaurants:
            ers_id = eleme_restaurant.eleme_id
            dom_poi = dom_test_session.query(DomPoi).filter(DomPoi.ers_poi_id == ers_id).first()
            if StringUtils.isNotEmptyString(dom_poi.baidu_poi_id):
                baidu_poi = dom_test_session.query(DomExtBaiduRestaurant).filter(DomExtBaiduRestaurant.shop_id == dom_poi.baidu_poi_id).first()
                if baidu_poi is not None:
                    fill_one_baidu_restaurant(ers_id, baidu_poi)
            if StringUtils.isNotEmptyString(dom_poi.meituan_poi_id):
                meituan_poi = dom_test_session.query(DomExtMeituanRestaurant).filter(DomExtMeituanRestaurant.shop_id == dom_poi.meituan_poi_id).first()
                if meituan_poi is not None:
                    fill_one_meituan_restaurant(ers_id, meituan_poi)
            if StringUtils.isNotEmptyString(dom_poi.dianping_poi_id):
                dianping_poi = dom_test_session.query(DomExtDianpingRestaurant).filter(DomExtDianpingRestaurant.restaurant_id == dom_poi.dianping_poi_id).first()
                if dianping_poi is not None:
                    fill_one_dianping_restaurant(ers_id, dianping_poi)

            count += 1

        if count % 100 == 0:
            print "已经处理 %s 条数据" % count

    print "已经处理完所有[%s]条数据" % count

if __name__ == '__main__':
    main()

