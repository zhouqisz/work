# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: test1.py
@time: 2018/4/8 下午10:48
"""
import argparse

parser = argparse.ArgumentParser(description="argparse model test ,python is great!!")            # description参数可以用于插入描述脚本用途的信息，可以为空
parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')   # 添加--verbose标签，标签别名可以为-v，这里action的意思是当读取的参数中出现--verbose/-v的时候
parser.add_argument('--number','-n',required=True, type=int,help = 'you must input int type ')                                                                                  # 参数字典的verbose建对应的值为True，而help参数用于描述--verbose参数的用途或意义。
parser.add_argument('--name','-m',action='store',help='a name')


args = parser.parse_args()                                                         # 将变量以标签-值的字典形式存入args字典

print parser.parse_args(

    [ '-v', '-n', '78', '-m', 'zhouqi']

    )
# for i in  args:
#     print i
# if args.verbose:
#     print "Verbose mode on!"
# else:
#     print "Verbose mode off!"




if __name__ == '__main__':
    pass