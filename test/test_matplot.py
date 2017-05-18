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
import matplotlib.pyplot as plt
 
plt.clf()  # 清空画布
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel(u"横轴")
plt.ylabel(u"纵轴")
plt.title("pythoner.com")
plt.show()