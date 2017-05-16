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
    MatplotlibUtils,
)

local_dom_session = LocalDomSession()

analysis_attributes = ['name', 'address']
imagefile_path = '../files/images'

def calc_avg(length_list):
    length_sum = 0.0
    for x in length_list:
        length_sum += x

    return length_sum * 1.0 / len(length_list)

def draw_one_attribute(poi, one_attribute, one_source):
    print "开始绘制[%s - %s]的分析图" % (one_source['name'], one_attribute)

    attribute_name = '%s_%s' % (one_source['pinyin'], one_attribute)

    if attribute_name not in [x for x in dir(poi)]:
        raise Exception('%s 不存在 %s 属性' % (type(poi), attribute_name))

    attribute_length_list = []

    limit = 10000
    last_id = 0
    poi_class = type(poi)
    while True:
        all_pois = local_dom_session.query(poi_class).filter(poi_class.id > last_id).order_by(poi_class.id.asc()).limit(limit).all()
        if ListUtils.isEmptyList(all_pois):
            break

        last_id = all_pois[len(all_pois)-1].id

        for one_poi in all_pois:
            attribute = getattr(one_poi, attribute_name)
            attribute_length_list.append(len(attribute)) 

    # 画图
    # MatplotlibUtils.draw_histogram(attribute_length_list, '%s length' % one_attribute , 'proportion', '%s shop %s attribute length distribution' % (one_source['pinyin'], one_attribute), '%s/%s-%s-length' % (imagefile_path, one_source['pinyin'], one_attribute))

    # 计算平均值
    length_avg = calc_avg(attribute_length_list)
    print '%s - %s 的平均值: %s' % (one_source['name'], one_attribute, length_avg)

def draw_attributes_image(poi, one_source):
    for one_attribute in  analysis_attributes:
        draw_one_attribute(poi, one_attribute, one_source)


def draw_hist(one_source):
    poi = None
    if one_source['source'] == MagicNums.ELEME_SOURCE:
        poi = DomElemeRestaurantInfo()
    elif one_source['source'] == MagicNums.MEITUAN_SOURCE:
        poi = DomMeituanRestairamtInfo()
    elif one_source['source'] == MagicNums.DIANPING_SOURCE:
        poi = DomDianpingRestairamtInfo()
    elif one_source['source'] == MagicNums.BAIDU_SOURCE:
        poi = DomBaiduRestairamtInfo()
    else:
        raise Exception('无效source:%s' % one_source)

    draw_attributes_image(poi, one_source)


def main():
    all_sources = MagicNums.ALL_SOURCES
    for one_source in all_sources:
        draw_hist(all_sources[one_source])

if __name__ == '__main__':
    main()