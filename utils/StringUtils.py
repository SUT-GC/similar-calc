#! -*-coding:utf8-*-

"""
字符串处理工具
"""

def isEmptyString(my_string):
    my_string = str(my_string)
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

if __name__ == '__main__':
    str1 = " 2 "
    print isEmptyString(str1)
    str2 = " 0 "
    print str2.strip() == "0.0"
    print isNotEmptyAndZeroString(str2)
    str3 = 0
    print isNotEmptyAndZeroString(str3)