#! -*-coding:utf8-*-

import random

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


def getRandomId(start_id, end_id):
    return random.randint(start_id, end_id)


def getRandomDischargeId(start_id, end_id, dischargeId, max_times=100):
    count = 0
    random_id = getRandomId(start_id, end_id)
    while True:
        if dischargeId == random_id:
            random_id = getRandomId(start_id, end_id)
            count += 1
            if count > 100:
                raise Exception(u'已经重试%s次' % max_times)
        else:
            return random_id


if __name__ == '__main__':
    # print isRandomId(24,[1,2,4,7,9])
    # print getRandomId(10,20)

    print getRandomDischargeId(10, 11, 10)
