#! -*-coding:utf8-*-

"""

填充10W条数据到 dom_meituan_restaurant 表中

随机抽选id尾数位2的店铺数据

"""

import sys
import datetime

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

from dao.models import (
    DomTestSession,
    LocalDomSession,

    DomElemeRestaurantInfo,
    DomBaiduRestairamtInfo,
    DomMeituanRestairamtInfo,
    DomDianpingRestairamtInfo,
    DomRestaurantRelation,
    
    DomPoi,
    DomExtBaiduRestaurant,
    DomExtMeituanRestaurant,
    DomExtDianpingRestaurant,
)

from utils import (
    NumUtils    
)

dom_test_session = DomTestSession()
local_dom_session = LocalDomSession()

DEFAULT_NUM = 100000
LIMIt = 10000
FILTER_ID_LAST_NUM = [9]
last_id = 0

count = 0
close = False

print "开始填充美团店铺信息"

while True:
    if close:
        break

    meituan_pois = dom_test_session.query(DomExtMeituanRestaurant).filter(DomExtMeituanRestaurant.id > last_id).order_by(DomExtMeituanRestaurant.id.asc()).limit(LIMIt).all()

    if meituan_pois is None or len(meituan_pois) <= 0:
        break

    last_id = meituan_pois[len(meituan_pois)-1].id

    for meituan_poi in meituan_pois:
        if NumUtils.isNotRandomId(meituan_poi.id, FILTER_ID_LAST_NUM):
            continue

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

        print count 

        count += 1

        local_dom_session.add(meituan)

        if count > DEFAULT_NUM:
            close = True
            break

        if count % 100 == 0:
            local_dom_session.commit()
            print "已经填充 %s 条记录" % count

local_dom_session.commit()
print "填充完毕，共填充 %s 条记录" % count



