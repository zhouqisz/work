#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import logging.config


def log_factory(path,logname):
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',\
        datefmt='%Y-%m-%d %H:%M:%S',\
        filemode='a',\
        filename = path+logname)
    s = logging
    return s
def test01(i):
    ret = -1
    if i > 0:
        ret = 0
    else:
        ret = -1
    return ret
def test02(logs):
    i = -1
    ret = test01(i)
    if ret != 0:
        logs.error("test01 is error %d" % ret)


def main():
    logs = log_factory('/home/zhouqi/Desktop/work/','zhouqi.log')
    test02(logs)
if __name__=='__main__':
    main()
