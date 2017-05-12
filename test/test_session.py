#! -*-coding:utf8-*-

import sys

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

dom_test_session = DomTestSession()
local_dom_session = LocalDomSession()

dom_pois = dom_test_session.query(DomPoi).filter(DomPoi.ers_poi_id > 0).limit(10)

for dom_poi in dom_pois:
    print dom_poi.shop_name, dom_poi.id
    eleme_restaurant = DomElemeRestaurantInfo()
    eleme_restaurant.eleme_name = dom_poi.shop_name
    eleme_restaurant.eleme_id = dom_poi.ers_poi_id
    local_dom_session.add(eleme_restaurant)

local_dom_session.commit()