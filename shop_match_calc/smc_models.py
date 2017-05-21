#! -*- coding:utf8 -*-

import sys

sys.path.append('..')
reload(sys)
sys.setdefaultencoding('utf-8')

from smc_main_calc import calc_shop_similar_score
from smc_config import ELEME_SOURCE, BAIDU_SOURCE, MEITUAN_SOURCE, DIANPING_SOURCE

class Shop(object):
    ELEME_SOURCE = ELEME_SOURCE
    MEITUAN_SOURCE = MEITUAN_SOURCE
    DIANPING_SOURCE = DIANPING_SOURCE
    BAIDU_SOURCE = BAIDU_SOURCE

    sources = ['eleme', 'meituan', 'dianping', 'baidu']


    def __init__(self, name, address, phones, latitude, longitude, source):
        self.name = name
        self.address = address
        self.phones = phones
        self.latitude = latitude
        self.longitude = longitude
        self.source = source


    def __str__(self):
        return 'name[%s], address[%s], phones[%s], latitude[%s], longitude[%s], source[%s]' % (self.name, self.address, self.phones, self.latitude, self.longitude, self.sources[self.source])


    def match_shop(self, other_shop):
        if self.source == self.ELEME_SOURCE and other_shop.source == self.ELEME_SOURCE or self.source != self.ELEME_SOURCE and other_shop.source != self.ELEME_SOURCE:
            raise Exception ('能且只能进行 饿了么店铺 和 竞对店铺 进行匹配')
        
        eleme_poi_shop = None
        other_poi_shop = None
        other_poi_source = None
        if self.source == self.ELEME_SOURCE:
            eleme_poi_shop = self
            other_poi_shop = other_shop
            other_poi_source = other_poi_shop.source
        elif other_shop.source == self.ELEME_SOURCE:
            eleme_poi_shop = other_shop
            other_poi_shop = self
            other_poi_source = other_poi_shop.source
        else:
            raise Exception ('能且只能进行 饿了么店铺 和 竞对店铺 进行匹配')

        return calc_shop_similar_score(eleme_poi_shop, other_poi_shop, other_poi_source) # 计算两个店铺的匹配度

if __name__ == '__main__':
    shop1 = Shop(u'丽姐烤肉饭', u'东北大学北门', '18704036473', 31.0231990814000, 121.48, Shop.ELEME_SOURCE)
    shop2 = Shop(u'小超小炒', u'沈阳工业大学北门', '18804036473', 31.0231990814000, 121.4364013670000, Shop.MEITUAN_SOURCE)
    print shop1.match_shop(shop2)