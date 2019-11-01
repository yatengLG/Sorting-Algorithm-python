# -*- coding: utf-8 -*-
# @Author  : LG

"""
基本思想:
    两个数比较大小，较大的数下沉，较小的数冒起来。

过程：
    1. 比较相邻的两个数据，如果第二个数小，就交换位置。
    2. 从后向前两两比较，一直到比较最前两个数据。最终最小数被交换到起始的位置，这样第一个最小数的位置就排好了。
    3. 继续重复上述过程，依次将第2.3...n-1个最小数排好位置。

平均时间复杂度：
    O(n2)
"""

def Bubble_Sort(datas):
    for i in range(1, len(datas)): # 用于记录遍历的次数, 由于自己不需要与自己比较,所以最多为len(datas)-1次
        for j in range(len(datas)-i):
            if datas[j] > datas[j+1]:
                datas[j], datas[j+1] = datas[j+1], datas[j]

    return datas

if __name__ == '__main__':
    import random
    a = list(range(20))
    random.shuffle(a)
    print(a)
    a = Bubble_Sort(a)
    print(a)
