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
def plot_bar(datas_list,title=None):
    ax.clear()
    ax.bar(x=range(len(datas_list)), height=datas_list, width=0.8, color=[colors[data] for data in datas_list])
    if title is not None:
        plt.title(title,fontsize = 18, loc='right')
    plt.axis('off')  # 去掉坐标轴
# 选择排序
def selectionSort(datas):
    datas_list = []
    for i in range(len(datas) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(datas)):
            if datas[j] < datas[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            datas[i], datas[minIndex] = datas[minIndex], datas[i]
        datas_list.append(tuple(datas))
    return datas, datas_list

# 初始化数据
datas = list(range(30))
# 打乱
random.shuffle(datas)
# 冒泡排序
_, datas_list = selectionSort(datas)
# 绘图
fig, ax = plt.subplots(figsize = (15,8))
animator = animation.FuncAnimation(fig, plot_bar, frames=datas_list, interval=500)
animator.save('aaa.gif')