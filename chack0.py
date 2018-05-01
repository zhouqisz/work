#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author: zhouqi
@software: PyCharm
@file: check0.py
@time: 2018/4/19 下午9:02
"""
import os
import time
import filecmp
import shutil



#目标文件检测目录
check_path = '/opt/mcb/nrt/abnormal/FileDist'

#文件工作目录
work_path  = '/opt/mcb/mcbnrt/work/incoming/'


#备份目录
bak_path   =  '/opt/mcb/mcbnrt/arch/incoming/'


#MCB_HOME/$MCB_APPID/work                                #工作，加入文件队列（预处理）


#$MCB_HOME/$MCB_APPID/arch                               #备份目录


path1 = check_path  # 检测目录（异常目录）
path2 = work_path  # 备份目录
path3 = bak_path  # 工作目录


def checkfile(file1, file2):  # 检测文件是否相同的函数

    return filecmp.cmp(path1 + file1, path2 + file2)


def main():
    while 1:  #
        count = 0  # 计数大文件夹下共有多少个文件
        list = []  # 用来存放文件名
        for filename in os.listdir(path1):
            # print filename
            if filename == '.DS_Store':  # 去掉系统自带的文件
                pass
            else:
                count += 1
                list.append(filename)
        print (count)
        print list
        if count > 0:
            for i in list:
                if os.path.isfile(path2 + i):  # 判断备份目录是否存在该文件
                    if checkfile(i, i):
                        print ('same')

                    else:
                        print ('diff')
                        shutil.move(path1 + i, path3 + i)  # 当文件不同时移动到工作目录
                else:
                    print ('path2 is not this file')  # 当文件不存在时

        time.sleep(1)  # 执行间隔设置一秒


if __name__ == '__main__':
    main()
