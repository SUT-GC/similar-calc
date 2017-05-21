#! -*-coding:utf8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

np.random.seed(0)

# example data
mu = 100  # 均值
sigma = 15  # 标准差
x = mu + sigma * np.random.randn(437)

datas = (x[0:len(x)/2], x[len(x)/2+1:len(x)])
print datas

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(datas, num_bins, normed=True)
# add a 'best fit' line
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()

