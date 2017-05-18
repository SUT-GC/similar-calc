#! -*- coding:utf8 -*-

import numpy as np
import sys

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

from utils import (
    StringUtils,
)

class LCSSimilar(object):
    def __init__(self, str1, str2):
        self.str1 = str1.lower()
        self.str2 = str2.lower()

    def lcs_similar(self):
        if StringUtils.isEmptyString(self.str1) or StringUtils.isEmptyString(self.str2):
            return 0.0
            
        collective_str = self.__calc_lcs()

        return self.__calc_score(collective_str)

    def __calc_lcs(self):
        a = self.str1
        b = self.str2

        m, n = len(a), len(b)

        # 为便于计算，为 D 多增加一行一列
        # 其中第一行和第一列中的元素保持为空字符串
        D = np.zeros((m+1, n+1), dtype=object)
        D[:] = ''                   # 初始化为空字符串

        for idx_a, ch_a in enumerate(a, 1):
            for idx_b, ch_b in enumerate(b, 1):
                # 若 D 不增加一行一列，下标 idx_a-1/idx_b-1 要判断是否非负
                if ch_a == ch_b:
                    D[idx_a, idx_b] = D[idx_a-1, idx_b-1] + ch_a
                else:
                    lcs_one = D[idx_a, idx_b-1]
                    lcs_two = D[idx_a-1, idx_b]
                    if len(lcs_one) > len(lcs_two):
                        D[idx_a, idx_b] = lcs_one
                    else:
                        D[idx_a, idx_b] = lcs_two

        return D[m, n]


    def __calc_score(self, collective_str):
        return 2.0 * len(collective_str) / (len(self.str1) + len(self.str2))

if __name__ == '__main__':
    str1 = u'你好'
    str2 = u'你好啊'

    lcs = LCSSimilar(str1, str2)
    print lcs.lcs_similar()
