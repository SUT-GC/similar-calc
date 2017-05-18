#! -*- coding:utf8 -*-

import sys
import re

sys.path.append("..")

str1 = u'小超小炒肉（沈阳工业大学店)'

start_index = str1.find(u'沈')
end_index = str1.rfind(u'学')

print start_index, end_index

sub_str = str1[start_index : end_index+1]
print str1.replace(sub_str, '')