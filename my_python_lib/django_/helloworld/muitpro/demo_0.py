# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: demo_0.py
@time: 2017/8/29 下午3:33
"""
import multiprocessing
import time


def worker_1(interval):
    print "worker_1"
    time.sleep(interval)
    print "end worker_1"


def worker_2(interval):
    print "worker_2"
    time.sleep(interval)
    print "end worker_2"


def worker_3(interval,hihi):
    print "worker_3"
    time.sleep(interval)
    test()

    print "end worker_3"

def test():
    for i in xrange(10):
        print i
        time.sleep(1)





if __name__ == "__main__":

    p1 = multiprocessing.Process(target=worker_1, args=(4,))
    p2 = multiprocessing.Process(target=worker_2, args=(4,))
    p3 = multiprocessing.Process(target=worker_3, args=(4,'hai',))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "END!!!!!!!!!!!!!!!!!"