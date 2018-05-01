# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: part_0.py
@time: 2018/4/13 下午9:38
"""
from redis import StrictRedis,ConnectionPool
import random

pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)


# for i in xrange(1000000):
#     redis.set(str(i),str(i+3))
for i in xrange(2000):
    print redis.get(str(random.randint(10,20000))),'  +  ',redis.get(str(i))



if __name__ == '__main__':
    pass