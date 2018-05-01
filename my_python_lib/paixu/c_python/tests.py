# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: tests.py
@time: 2018/3/21 下午8:45
"""

import foo
import time


# print(foo.__doc__)
# print(help(foo))
now = time.time()
foo.in_n()
print(time.time()-now)