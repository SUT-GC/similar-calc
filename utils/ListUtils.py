#! -*-coding:utf8-*-

def isEmptyList(my_list, empty_size=0):
    if my_list is None or len(my_list) <= empty_size:
        return True
    return False

def isNotEmptyList(my_list, empty_size=0):
    return not isEmptyList(my_list, empty_size=0)

def calc_avg(my_list):
    my_sum = 0.0
    for x in my_list:
        my_sum += x

    return my_sum * 1.0 / len(my_list)

if __name__ == '__main__':
    l1 = []
    l2 = None
    l3 = [1]

    print isNotEmptyList(l1)
    print isNotEmptyList(l2)
    print isNotEmptyList(l3)