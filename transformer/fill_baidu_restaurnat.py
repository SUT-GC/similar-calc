#! -*-coding:utf8-*-

"""

填充10W条数据到 dom_baidu_restaurant 表中

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

print "开始填充百度店铺信息"

while True:
    if close:
        break

    baidu_pois = dom_test_session.query(DomExtBaiduRestaurant).filter(DomExtBaiduRestaurant.id > last_id).order_by(DomExtBaiduRestaurant.id.asc()).limit(LIMIt).all()

    if baidu_pois is None or len(baidu_pois) <= 0:
        break

    last_id = baidu_pois[len(baidu_pois)-1].id

    for baidu_poi in baidu_pois:
        if NumUtils.isNotRandomId(baidu_poi.id, FILTER_ID_LAST_NUM):
            continue

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

        print count 

        count += 1

        local_dom_session.add(baidu)

        if count > DEFAULT_NUM:
            close = True
            break

        if count % 100 == 0:
            local_dom_session.commit()
            print "已经填充 %s 条记录" % count

local_dom_session.commit()
print "填充完毕，共填充 %s 条记录" % count



