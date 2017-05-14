#! -*-coding:utf8-*-

"""

填充10W条数据到 dom_eleme_restaurant 表中

随机抽选id尾数位2/7的店铺数据

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

print "开始填充饿了么店铺信息"

while True:
    if close:
        break

    dom_pois = dom_test_session.query(DomPoi).filter(DomPoi.ers_poi_id > 0).filter(DomPoi.id > last_id).order_by(DomPoi.id.asc()).limit(LIMIt).all()

    if dom_pois is None or len(dom_pois) <= 0:
        break

    last_id = dom_pois[len(dom_pois)-1].id

    for dom_poi in dom_pois:
        if NumUtils.isNotRandomId(dom_poi.id, FILTER_ID_LAST_NUM):
            continue

        ers = DomElemeRestaurantInfo()
        ers.eleme_id = dom_poi.ers_poi_id
        ers.eleme_name = dom_poi.shop_name
        ers.eleme_branch_name = dom_poi.branch_shop_name
        ers.eleme_address = dom_poi.address
        ers.eleme_phone = dom_poi.phone
        ers.eleme_latitude = dom_poi.latitude
        ers.eleme_longitude = dom_poi.longitude
        ers.eleme_logo_hash = dom_poi.logo_pic
        ers.eleme_is_value = 1
        ers.created_at = datetime.datetime.now()
        ers.updated_at = datetime.datetime.now()

        print count 

        count += 1

        local_dom_session.add(ers)

        if count > DEFAULT_NUM:
            close = True
            break

        if count % 100 == 0:
            local_dom_session.commit()
            print "已经填充 %s 条记录" % count

local_dom_session.commit()
print "填充完毕，共填充 %s 条记录" % count



