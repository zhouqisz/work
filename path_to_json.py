#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import json
import my_python_lib.jsonrw.json_w as js
import time
def scan_files(directory, prefix=None, postfix=None):
    files_list = {}
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                if special_file =='.DS_Store':
                    pass
                else:
                    files_list[os.path.join(root, special_file)]=special_file

    return files_list

def file_to_jsonfile(filename,objpath,path=None):
    list= scan_files(objpath,)
    file = path+filename
    # print list
    listold = js.read_json_from_file(file)
    if list == listold:
        return '文件没有更新',list
    else:
        js.write_json_to_file(list,file)
        return '文件已更新',list

def main():
    objpath= '/home/zhouqi/Desktop/work/my_python_lib/jsonrw/'
    filename = time.strftime('%Y%m%d',time.localtime(time.time())) +'.json'
    file_to_jsonfile(filename,objpath,'/home/zhouqi/Desktop/work/')

if __name__=='__main__':
    main()
