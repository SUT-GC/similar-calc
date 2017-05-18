#! -*- coding:utf8 -*-
from math import radians, cos, sin, asin, sqrt  

class SphericalDistance(object):
    def __init__(self, lon1, lat1, lon2, lat2):
        self.lon1 = lon1
        self.lat1 = lat1
        self.lon2 = lon2
        self.lat2 = lat2

    def calc_distance(self):
        # 将十进制度数转化为弧度  
        lon1, lat1, lon2, lat2 = map(radians, [self.lon1, self.lat1, self.lon2, self.lat2])  
      
        # haversine公式  
        dlon = lon2 - lon1   
        dlat = lat2 - lat1   
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
        c = 2 * asin(sqrt(a))   
        r = 6371 # 地球平均半径，单位为公里  

        return c * r * 1000

if __name__ == '__main__':
    lon1 = 123.2500200000
    lat1 = 41.7370000000
    lon2 = 123.2535982132
    lat2 = 41.7393130288

    sd = SphericalDistance(lon1, lat1, lon2, lat2)
    print sd.calc_distance()