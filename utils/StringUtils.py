#! -*-coding:utf8-*-

"""
字符串处理工具
"""

def isEmptyString(my_string):
    if my_string is None or my_string.strip() == '' or len(my_string) <= 0:
        return True
    return False

def isNotEmptyString(my_string):
    return not isEmptyString(my_string)

if __name__ == '__main__':
    str1 = " 2 "
    print isEmptyString(str1)