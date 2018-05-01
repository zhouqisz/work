# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: insert.py
@time: 2017/12/30 上午9:26
"""

import random


cddef d():
    list = []
    n = 10000
    now = time.time()
    for i in range(n):
        list.append(random.randint(0,5*n))

    for i in range(0,len(list)):
        j = 0
        while(j<i):
            if list[i]<list[j]:break
            j = j+1

        temp = list[i]
        k = i
        while(k>j):
            list[k] = list[k-1]
            k = k-1

        list[k] = temp
        # print list
    for k in range(20):
        print(list[k])

    print (time.time() - now)



