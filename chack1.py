#!/usr/bin/python
# -*- coding:utf-8 -*-
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

path1 = check_path  # 检测目录（异常目录）
path2 = work_path   # 备份目录
path3 = bak_path    # 工作目录

def checkfile(file1, file2):  # 检测文件是否相同的函数

    return filecmp.cmp(file1, file2)


def mvfile(file, file_work):
    shutil.move(file, file_work)


def get_bakfile_name_and_path(file_nm):  # 从异常目录文件文件名得到备份文件名和目录
    print(filename[0:2])
    print(file_nm[7:12])
    print(file_nm[31:39])


filename = 'NRPAKPLHKGPP0115580#3918617767#20180424140404.tmp'
get_bakfile_name_and_path(filename)

# def main():
#     while 1:  #
#         count = 0  # 计数大文件夹下共有多少个文件
#         list = []  # 用来存放文件名
#         for filename in os.listdir(path1):
#             # print filename
#             if filename == '.DS_Store':  # 去掉系统自带的文件
#                 pass
#             else:
#                 count += 1
#                 list.append(filename)
#         print (count)
#         print list
#         if count > 0:
#             for i in list:
#                 file_bak, file_bak_path = get_bakfile_name_and_path(i)  # 得到文件目录
#
#                 if checkfile(path1 + i, file_bak_path + filename):
#                     print 'same'
#
#                 else:
#                     print 'diff'
#                     shutil.move(path1 + i, path3 + i)  # 当文件不同时移动到工作目录
#
#         time.sleep(1)  # 执行间隔设置一秒
#
#
# if __name__ == '__main__':
#     # main()

# !/usr/bin/env python
# coding=utf-8

import os


def scan_files(directory, prefix=None, postfix=None):
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list


#https://blog.csdn.net/Limenghui0614/article/details/77895728
