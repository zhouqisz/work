# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: os_test.py
@time: 2018/4/7 下午5:59
"""



import os


for dirpath,dirname ,filename in os.walk('/Users/zhouqi/Desktop/tool'):
    print 'dirpath:' , dirpath
    print 'firname:' , dirname
    print 'filename:', filename







if __name__ == '__main__':
    pass