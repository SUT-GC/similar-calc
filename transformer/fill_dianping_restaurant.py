#! -*-coding:utf8-*-

"""

填充10W条数据到 dom_dianping_restaurant 表中

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

print "开始填充点评店铺信息"

while True:
    if close:
        break

    dianping_pois = dom_test_session.query(DomExtDianpingRestaurant).filter(DomExtDianpingRestaurant.id > last_id).order_by(DomExtDianpingRestaurant.id.asc()).limit(LIMIt).all()

    if dianping_pois is None or len(dianping_pois) <= 0:
        break

    last_id = dianping_pois[len(dianping_pois)-1].id

    for dianping_poi in dianping_pois:
        if NumUtils.isNotRandomId(dianping_poi.id, FILTER_ID_LAST_NUM):
            continue

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

        print count 

        count += 1

        local_dom_session.add(dianping)

        if count > DEFAULT_NUM:
            close = True
            break

        if count % 100 == 0:
            local_dom_session.commit()
            print "已经填充 %s 条记录" % count

local_dom_session.commit()
print "填充完毕，共填充 %s 条记录" % count



