#! -*-coding:utf8-*-

import sys

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

from dao.models import (
    DomElemeRestaurantInfo,
    DomMeituanRestairamtInfo,
    DomDianpingRestairamtInfo,
    DomBaiduRestairamtInfo,

    LocalDomSession,
)

from utils import (
    MagicNums,
    ListUtils,
    StringUtils,
)

not_attrs = ['created_at', 'updated_at', 'id', 'metadata']
count_str = 'count'

local_dom_session = LocalDomSession()

def clac_coverage(poi, attrs):

    poi_class = type(poi)
    limit = 1000
    last_id = 0
    clac_count = 0
    
    while True:
        all_pois = local_dom_session.query(poi_class).filter(poi_class.id > last_id).order_by(poi_class.id.asc()).limit(limit).all()
        if ListUtils.isEmptyList(all_pois):
            break

        last_id = all_pois[len(all_pois)-1].id

        for one_poi in all_pois:
            for attr in attrs:
                if hasattr(one_poi, attr) and StringUtils.isNotEmptyAndZeroString(getattr(one_poi, attr)):
                    attrs[attr] += 1
            attrs[count_str] = attrs[count_str] + 1
            clac_count += 1

        if clac_count % 100 == 0:
            print "已经处理[%s]条[%s]数据" % (clac_count, poi_class)


    if attrs[count_str] != clac_count:
        raise Exception("统计数据数量有误 count_str[%s], clac_count[%s]" % (count_str, clac_count))
    print "已经处理所有[%s]数据共[%s]条" % (poi_class, clac_count)

    return attrs        

def get_coverage(source):
    poi = None

    if source == MagicNums.BAIDU_SOURCE:
        poi = DomBaiduRestairamtInfo()
    elif source == MagicNums.MEITUAN_SOURCE:
        poi = DomMeituanRestairamtInfo()
    elif source == MagicNums.DIANPING_SOURCE:
        poi = DomDianpingRestairamtInfo()
    elif source == MagicNums.ELEME_SOURCE:
        poi = DomElemeRestaurantInfo()
    else:
        raise Exception('无效数据源 source[%s]' % source)

    attrs = {x:0 for x in dir(poi) if not x.startswith('_') and x not in not_attrs}
    attrs[count_str] = 0
    
    attrs = clac_coverage(poi, attrs)

    for x in attrs.keys():
        if x != count_str:
            attrs[x] = attrs[x]*1.0/attrs[count_str]

    return attrs

def test():
    poi = DomElemeRestaurantInfo()
    poi_class = type(poi)
    one = local_dom_session.query(poi_class).filter(poi_class.id > 0).first()
    print one.id

if __name__ == '__main__':

    eleme_attrs = get_coverage(MagicNums.ELEME_SOURCE)
    baidu_attrs = get_coverage(MagicNums.BAIDU_SOURCE)
    meituan_attrs = get_coverage(MagicNums.MEITUAN_SOURCE)
    dianping_attrs = get_coverage(MagicNums.DIANPING_SOURCE)

    print eleme_attrs
    print baidu_attrs
    print meituan_attrs
    print dianping_attrs
