# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: insert.py
@time: 2017/12/30 上午9:26
"""

import random




cdef in_ns():

    n =10000
    cdef list  li = []

    cdef int k,j,temp


    for i in range(n):
        li.append(random.randint(0,5*n))


    for i in range(0,len(li)):
        j = 0
        while(j<i):
            if li[i]<li[j]:break
            j = j+1

        temp = li[i]
        k = i
        while(k>j):
            li[k] = li[k-1]
            k = k-1

        li[k] = temp
        # print list
    # for l in range(20):
    #     print(list[l])

def in_n():
#
    return  in_ns()





