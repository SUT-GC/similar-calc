#! -*-coding:utf8-*-

import sys
import re

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

"""
字符串处理工具
"""

def isEmptyString(my_string):
    if my_string is None or my_string.strip() == '' or len(my_string) <= 0:
        return True
    return False

def isNotEmptyString(my_string):
    return not isEmptyString(my_string)

def isEmptyAndZeroString(my_string):
    if type(my_string) is str or type(my_string) is unicode:
        if isNotEmptyString(my_string) and my_string.strip() != '0' and my_string.strip() != '0.0':
            return False
    else:
        try:
            my_string = float(my_string)
            
            if my_string > 0.0:
                return False
        except Exception as e:
            raise Exception("无法转换成float且不是str类型, message: %s", e)
    
    

    return True

def isNotEmptyAndZeroString(my_string):
    return not isEmptyAndZeroString(my_string)    


def deleteBrackets(my_str):
    if isEmptyString(my_str):
        return ''

    start_index = -1
    start_index1 = my_str.find(u'(')
    start_index2 = my_str.find(u'（')

    if start_index1 < 0:
        start_index = start_index2
    if start_index2 < 0:
        start_index = start_index1
    if start_index1 >= 0 and start_index2 >= 0:
        start_index = min(start_index1, start_index2)

    end_index = -1
    end_index1 = my_str.rfind(u')')
    end_index2 = my_str.rfind(u'）')

    if end_index1 < 0:
        end_index = end_index2
    if end_index2 < 0:
        end_index = end_index1
    if end_index1 >= 0 and end_index2 >= 0:
        end_index = max(end_index1, end_index2)

    if start_index >=0 and end_index >=0:
        sub_str = my_str[start_index : end_index+1]
        my_str = my_str.replace(sub_str, '')

    return my_str


if __name__ == '__main__':
    # str1 = " 2 "
    # print isEmptyString(str1)
    # str2 = " 0 "
    # print str2.strip() == "0.0"
    # print isNotEmptyAndZeroString(str2)
    # str3 = 0
    # print isNotEmptyAndZeroString(str3)
    str1 = u'小超小炒肉(沈阳工业大学店)'

    print deleteBrackets(str1)