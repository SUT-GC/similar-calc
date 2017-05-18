#! -*- coding:utf8 -*-

import jieba
import math

import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

from utils import (
    StringUtils,
)

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


if __name__ == '__main__':
    str1 = u"我喜欢看电视，不喜欢看电影。"
    str2 = u"我不喜欢看电视，也不喜欢看电影。"
    cs = CosineSimilar(str1, str2)
    
    print cs.calc_similar()
