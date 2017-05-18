#! -*- coding:utf8 -*-

import numpy as np
import sys

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

from utils import (
    StringUtils,
)

class LevenshteinSimilar(object):
    def __init__(self, str1, str2):
        self.str1 = str1.lower()
        self.str2 = str2.lower()


    def levenshtein_similar(self):
        if StringUtils.isEmptyString(self.str1) or StringUtils.isEmptyString(self.str2):
            return 0.0
            
        step_count = self.__ls()

        return self.__calc_similar(step_count)


    def __ls(self):
        a = self.str1
        b = self.str2

        m, n = len(a), len(b)
        dis_matrix = np.zeros((m+1, n+1), dtype=int)

        # 初始化距离矩阵的第 0 行和第 0 列
        dis_matrix[0, :] = np.arange(n+1)
        dis_matrix[:, 0] = np.arange(m+1)

        # 开始计算
        for idx_a, ch_a in enumerate(a, 1):
            for idx_b, ch_b in enumerate(b, 1):
                cur_dis = None

                dis_left = dis_matrix[idx_a, idx_b-1]
                dis_upper = dis_matrix[idx_a-1, idx_b]
                dis_upper_left = dis_matrix[idx_a-1, idx_b-1]
                if ch_a == ch_b:
                    cur_dis = min(dis_left+1, dis_upper+1, dis_upper_left)
                else:
                    cur_dis = min(dis_left+1, dis_upper+1, dis_upper_left + 1)

                dis_matrix[idx_a, idx_b] = cur_dis

        return dis_matrix[m, n]


    def __calc_similar(self, step_count):
        return 1 - step_count * 1.0 / max(len(self.str1), len(self.str2))

if __name__ == '__main__':
    str1 = u'清真兰州拉面馆'
    str2 = u'兰州拉面'

    ls = LevenshteinSimilar(str1, str2)
    print ls.levenshtein_similar()
