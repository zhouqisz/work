#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import logging.config



logging.basicConfig(level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a',
    filename = "logging.log"
    )



def test01(i):
    ret = -1
    if i > 0:
        ret = 0
    else:
        ret = -1
    return ret
def test02():
    i = -1
    ret = test01(i)
    if ret != 0:
        logging.error("test01 is error %d" % ret)


def main():
    test02()
if __name__=='__main__':
    main()
