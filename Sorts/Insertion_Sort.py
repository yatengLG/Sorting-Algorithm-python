# -*- coding: utf-8 -*-
# @Author  : LG

"""
基本思想：
    在要排序的一组数中，假定前n-1个数已经排好序，现在将第n个数插到前面的有序数列中，使得这n个数也是排好顺序的。如此反复循环，直到全部排好顺序。

过程：

平均时间复杂度：
    O(n2)

"""

def Insertion_Sort(datas):
    for i in range(1, len(datas)):  # 初始假定第一个数据为有序,后续数据均为无序
        for j in range(i):
            current = datas[i]
            if current < datas[j]:
                for k in range(i,j):
                #     print(k)
                #     datas[j+1] = datas[j]
                # datas[j]= current

        print(datas)
    return datas



def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
        print(arr)
    return arr

if __name__ == '__main__':
    import random
    a = list(range(10))
    random.shuffle(a)
    b = a.copy()

    arr = insertionSort(a)
    print('---'*10)
    Insertion_Sort(b)