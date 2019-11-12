# -*- coding: utf-8 -*-
# @Author  : LG

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random
import time
from IPython.display import HTML

cmap=plt.get_cmap('plasma')
colors = [cmap(i) for i in np.linspace(0, 1, 30)]

datas = list(range(10))
random.shuffle(datas)

# 绘图使用
def plot_bar(datas_list,title='Bubble Sort'):
    ax.clear()
    ax.bar(x=range(len(datas_list)), height=datas_list, width=0.8, color=[colors[data] for data in datas_list])
    if title is not None:
        plt.title(title,fontsize = 24, loc='right')
    plt.axis('off')  # 去掉坐标轴
    plt.figtext(0.3, 0.05, 'https://github.com/yatengLG/Sorting-Algorithm-python',fontsize = 18)


def Bubble_Sort(datas):
    datas_list = []
    for i in range(1, len(datas)): # 用于记录遍历的次数, 由于自己不需要与自己比较,所以最多为len(datas)-1次
        for j in range(len(datas)-i):   # 用于遍历剩余没遍历过的点
            if datas[j] > datas[j+1]:   # 比较俩个数,如果前面数大,则交换俩个数
                datas[j], datas[j+1] = datas[j+1], datas[j]
            datas_list.append(tuple(datas))
    return datas, datas_list


# 初始化数据
datas = list(range(30))
# 打乱
random.shuffle(datas)
# 冒泡排序
_, datas_list = Bubble_Sort(datas)
# 绘图
fig, ax = plt.subplots(figsize = (10,6))
animator = animation.FuncAnimation(fig, plot_bar, frames=datas_list, interval=500)
animator.save('../Images/Bubble_Sort.gif')