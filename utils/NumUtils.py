#! -*-coding:utf8-*-

def isRandomId(id, lastNum=None):
    if lastNum is None:
        if (id % 10 == 2) or (id % 10 == 7):
            return True
    else:
        if type(lastNum) is not list:
            raise Exception("第二个参数必须是list")
        for num in lastNum:
            if id % 10 == num:
                return True
    
    return False

def isNotRandomId(id, lastNum=None):
    return not isRandomId(id, lastNum)

if __name__ == '__main__':
    print isRandomId(24,[1,2,4,7,9])