# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: part0_importlib.py
@time: 2018/4/17 下午9:37
"""

import importlib
import time

# third_buy中有N个***_func(params)函数
# import third_buy
#
# third_method = '%s_func' % method
# # 通过函数名的字符串来调用这个函数
# res = getattr(third_buy, third_method)(params)

# business 为业务类型：flow, bill
# method 为文件名：dingxin, xunzhong

def func(method):
    # method = '{0}.{1}'.format(business, method)
    # print method
    module = importlib.import_module(method)
    print mudule.__doc__
    # buy_res = module.func(params)

if __name__ == '__main__':
    func('time')