# #! -*-coding:utf8 -*-
# import numpy as np
# import matplotlib.mlab as mlab
# import matplotlib.pyplot as plt

# np.random.seed(0)

# # example data
# mu = 100  # 均值
# sigma = 15  # 标准差
# x = mu + sigma * np.random.randn(437)

# print np.random.randn(437)

# num_bins = 50

# fig, ax = plt.subplots()

# # the histogram of the data
# n, bins, patches = ax.hist(x, num_bins, normed=True)
# print "=============="
# print n,"------", bins, '-------', patches
# print "=============="
# print bins
# # add a 'best fit' line
# y = mlab.normpdf(bins, mu, sigma)
# ax.plot(bins, y, '-')
# ax.set_xlabel('Smarts')
# ax.set_ylabel('Probability density')
# ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# # Tweak spacing to prevent clipping of ylabel
# fig.tight_layout()
# plt.show()

#-*- coding: utf-8 -*-
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
t = arange(-4*pi, 4*pi, 0.01)
y = sin(t)/t
plt.plot(t, y)
plt.title(u'钟形函数')
plt.xlabel(u'时间')
plt.ylabel(u'幅度')
plt.show()