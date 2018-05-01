# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: demo.py
@time: 2018/4/27 下午10:06
"""

import json
import sys
import os
sys.path.append('../')
#print(test_dict)
#print(type(test_dict))
#dumps 将数据转换成字符串
#json_str = json.dumps(test_dict)
#print(json_str)
#print(type(json_str))

#new_dict = json.loads(json_str)
#print(new_dict)
#print(type(new_dict))
def write_json_to_file(new_dict,file):
    with open(file,"w") as f:
        json.dump(new_dict,f)
       # print("加载入文件完成...")


def read_json_from_file(file):
    if os.path.exists(file):
        try:
            with open(file, 'r') as load_f:
                load_dict = json.load(load_f)
                return load_dict

        except  ValueError as e :
            print e

        file = open(file,'w')
        file.close()
        return {}

def main():
    test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
    load_dict = test_dict
    load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
    # print(load_dict)
    file = '/home/zhouqi/Desktop/work/my_python_lib/jsonrw/hah.json'
    write_json_to_file(load_dict,file)

if __name__=='__main__':
    main()

    
