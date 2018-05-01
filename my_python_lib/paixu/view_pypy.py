# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: view_pypy.py
@time: 2018/4/7 下午8:30
"""

def f():
    s = 0
    for i in xrange(100000):
        s += 1
        # print 'ok'

    if s >10:
        print 'hello'

    return s


if __name__ == '__main__':
    import dis
    dis.dis(f)
    f()