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

def calcSubListSum(my_list, start, end, step):

    num_list = []
    now_num = start
    while now_num < end:
        num_list.append(now_num)
        now_num += step
    num_list.append(end)

    sum_list = []
    for x in range(len(num_list)):
        sum_list.append(0)

    # 统计范围是[a, b)
    for x in my_list:
        for i in range(1, len(num_list)):
            # print x, num_list[i-1], num_list[i]
            if x >= num_list[i] and i == len(num_list)-1:
                sum_list[len(sum_list)-1] += 1
                break
            if x >= num_list[i-1] and x < num_list[i]:
                sum_list[i-1] += 1
                break

    result_list = []
    for i in range(len(sum_list)):
        result_list += [(i+1)] * sum_list[i]

    return result_list


if __name__ == '__main__':
    # l1 = []
    # l2 = None
    # l3 = [1]

    # print isNotEmptyList(l1)
    # print isNotEmptyList(l2)
    # print isNotEmptyList(l3)
    calcSubListSum([0,1,2,3,4,5,6,7,8,9,10,11,31,33,42,54,99,100,111], 0, 100, 10)