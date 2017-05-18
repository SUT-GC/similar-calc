#! -*- coding:utf8 -*-

import numpy as np
import sys
import Levenshtein

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


if __name__ == '__main__':
    str1 = u'清真兰州拉面馆'
    str2 = u'兰州拉面'

    jw = JaroWinklerSimilar(str1, str2)
    print jw.jarowinkler_similar()
