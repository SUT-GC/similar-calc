#! -*- coding:utf8 -*-

import sys

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")

class PhoneSimilar(object):
    sub_symbol = [',', '-', '/', '\\', ' ', '，', '／', '、', '.', '。', '|', '_', '——']
    replace_symbol = ','

    def __init__(self, phone1, phone2):
        self.phone1 = phone1
        self.phone2 = phone2

    
    def calc_similar(self):
        phone1_list = self.__sub_phone(self.phone1)
        phone2_list = self.__sub_phone(self.phone2)

        return self.__calc_list_similar(phone1_list, phone2_list)


    def __calc_list_similar(self, phone1_list, phone2_list):
        for x in phone1_list:
            for y in phone2_list:
                if x == y or x in y or y in x:
                    return 1.0

        return 0.0


    def __sub_phone(self, phone):
        for symbol in self.sub_symbol:
            phone = phone.replace(symbol, self.replace_symbol)

        # 去掉非法字符和区号
        return [x for x in phone.split(',') if x.strip() != '' and len(x.strip()) > 6]


if __name__ == '__main__':
    phone1 = '18804036473 04217751442'
    phone2 = '7751442'
    ps = PhoneSimilar(phone1, phone2)
    print ps.calc_similar()
