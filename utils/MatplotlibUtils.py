#! -*- coding:utf8 -*-

import sys

sys.path.append("..")
reload(sys)
sys.setdefaultencoding("utf-8")


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

my_fs = 15  # fontsize
my_figsize = (6, 6)


def draw_boxplot(data, xlabel, title, fontsize=my_fs, figsize=my_figsize, write_file_path=None):
    plt.figure(figsize=figsize)
    plt.boxplot(data)
    plt.xlabel(xlabel)
    plt.title(title, fontsize=fontsize)
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

    if write_file_path is None:
        plt.show()
    else:
        plt.savefig(write_file_path)

    print "绘制完成"

def draw_histogram(data, xlabel, ylabel, title, write_file_path=None):
    data_sum = 0.0
    for x in data:
        data_sum += x
    avg_data = data_sum / len(data)
    sigma_sum = 0.0
    set_list = []
    for x in data:
        sigma_sum += (x - avg_data)*(x - avg_data)
        if x not in set_list:
            set_list.append(x)

    sigma_data = sigma_sum / len(data)

    fig, ax = plt.subplots()
    # the histogram of the data
    n, bins, patches = ax.hist(data, normed=True)

    y = mlab.normpdf(bins, avg_data, sigma_data)
    ax.plot(bins, y, '-')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()

    if write_file_path is None:
        plt.show()
    else:
        plt.savefig(write_file_path)

    print "绘制完成"

if __name__ == '__main__':
    # draw_boxplot([1], 'name', 'my')
    draw_histogram([1,2,2,2,2,2,3,3,4,], u'x坐标', "ylabel", "title")


