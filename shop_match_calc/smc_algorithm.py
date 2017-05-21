#! -*- coding:utf8 -*-

import numpy as np
import sys
import Levenshtein
import jieba
import math
from math import (
    radians, 
    cos, 
    sin, 
    asin, 
    sqrt  
)

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

from utils import (
    StringUtils,
)

class JaroWinklerSimilar(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def jarowinkler_similar(self):
        if StringUtils.isEmptyString(self.str1) or StringUtils.isEmptyString(self.str2):
            return 0.0
        return Levenshtein.jaro_winkler(self.str1, self.str2)


class CosineSimilar(object):

    def __init__(self, str1, str2):
        self.str1 = str1.lower()
        self.str2 = str2.lower()


    def calc_similar(self):
        if StringUtils.isEmptyString(self.str1) or StringUtils.isEmptyString(self.str2):
            return 0.0
        str1_list, str2_list = self.__fenci()
        str1_vector, str2_vector = self.__cipin(str1_list, str2_list)

        return self.__cosine_similar(str1_vector, str2_vector)


    def __fenci(self):
        str1_list = [x for x in jieba.cut(self.str1, cut_all=False)]
        str2_list = [x for x in jieba.cut(self.str2, cut_all=False)]

        return str1_list, str2_list


    def __cipin(self, str1_list, str2_list):
        ci_set = []
        str1_vector = []
        str2_vector = []

        for ci in str1_list:
            if ci not in ci_set:
                ci_set.append(ci)
        for ci in str2_list:
            if ci not in ci_set:
                ci_set.append(ci)

        return self.__calc_cipin(ci_set, str1_list), self.__calc_cipin(ci_set, str2_list)


    def __calc_cipin(self, ci_set, str_list):
        ci_vector = []
        for ci in ci_set:
            ci_count = 0
            for one_str in str_list:
                if ci == one_str:
                    ci_count += 1
            ci_vector.append(ci_count)

        return ci_vector


    def __cosine_similar(self, str1_vector, str2_vector):
        fenzi = 0.0
        for i in range(len(str1_vector)):
            fenzi += str1_vector[i] * str2_vector[i]
        fenmu = math.sqrt(sum([x*x for x in str1_vector])) * math.sqrt(sum([x*x for x in str2_vector]))
        return fenzi / fenmu


class PhoneSimilar(object):
    sub_symbol = [',', '-', '/', '\\', ' ', '，', '／', '、', '.', '。', '|', '_', '——']
    replace_symbol = ','

    def __init__(self, phone1, phone2):
        self.phone1 = phone1
        self.phone2 = phone2

    
    def calc_similar(self):
        phone1_list = self.__sub_phone(self.phone1)
        phone2_list = self.__sub_phone(self.phone2)

        return self.__calc_list_similar(phone1_list, phone2_list)


    def __calc_list_similar(self, phone1_list, phone2_list):
        for x in phone1_list:
            for y in phone2_list:
                if x == y or x in y or y in x:
                    return 1.0

        return 0.0


    def __sub_phone(self, phone):
        for symbol in self.sub_symbol:
            phone = phone.replace(symbol, self.replace_symbol)

        # 去掉非法字符和区号
        return [x for x in phone.split(',') if x.strip() != '' and len(x.strip()) > 6]



class SphericalDistance(object):
    def __init__(self, lon1, lat1, lon2, lat2):
        self.lon1 = lon1
        self.lat1 = lat1
        self.lon2 = lon2
        self.lat2 = lat2

    def calc_distance(self):
        # 将十进制度数转化为弧度  
        lon1, lat1, lon2, lat2 = map(radians, [self.lon1, self.lat1, self.lon2, self.lat2])  
        # haversine公式  
        dlon = lon2 - lon1   
        dlat = lat2 - lat1   
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
        c = 2 * asin(sqrt(a))   
        r = 6371 # 地球平均半径，单位为公里  

        return c * r * 1000


if __name__ == '__main__':
    str1 = u'清真兰州拉面馆'
    str2 = u'兰州拉面'

    jw = JaroWinklerSimilar(str1, str2)
    print jw.jarowinkler_similar()

    str1 = u"我喜欢看电视，不喜欢看电影。"
    str2 = u"我不喜欢看电视，也不喜欢看电影。"

    cs = CosineSimilar(str1, str2)
    print cs.calc_similar()

    phone1 = '18804036473 04217751442'
    phone2 = '7751442'

    ps = PhoneSimilar(phone1, phone2)
    print ps.calc_similar()

    lon1 = 123.2500200000
    lat1 = 41.7370000000
    lon2 = 123.2535982132
    lat2 = 41.7393130288

    sd = SphericalDistance(lon1, lat1, lon2, lat2)
    print sd.calc_distance()
