# -*- coding: utf-8 -*-
# @Author  : LG

"""
基本思想：
    在长度为N的无序数组中，第一次遍历n-1个数，找到最大的数值与第一个元素交换；
    第二次遍历n-2个数，找到最小的数值与第二个元素交换；
    ...
    第n-1次遍历，找到最小的数值与第n-1个元素交换，排序完成。
过程:
    1. 找最大数
    2. 放到对应位置
    ...
平均时间复杂度:
    O(n2)
"""

def Selction_Sort(datas):
    for i in range(len(datas)-1):
        max = i # 第一次从第一个数开始,第二次从第二个数开始
        for j in range(i+1, len(datas)):    # 用记录的max数与其他数挨着作比较
            if datas[j] > datas[i]:
                max = j
        datas[i], datas[max] = datas[max], datas[i]

    return datas
