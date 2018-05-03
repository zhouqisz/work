#!/usr/bin/python
# -*- coding:utf-8 -*-
import ConfigParser
import my_python_lib.jsonrw.json_w as js
import my_python_lib.log_w.log as logss
import path_to_json
import time
import shutil
import filecmp
import tarfile
import zipfile
import os

class works:


    def __init__(self,config_str):
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_str)
        self.tarpath   =  self.config.get("path","tarpath")
        self.checkpath = self.config.get("path","checkpath")
        self.bakpath   = self.config.get("path","bakpath")
        self.workpath  = self.config.get("path","workpath")
        self.jsonpath  = self.config.get("path","jsonpath")
        self.logspath  = self.config.get("path","logspath")
        self.jsonpaths = self.config.get("path", "jsonpaths")
        self.timesleep = self.config.get("setting","timesleep")
        self.checkdays = self.config.get("setting","checkdays")
        self.name_log  = time.strftime('%Y%m%d',time.localtime(time.time()))+'.log'
        self.name_json= time.strftime('%Y%m%d', time.localtime(time.time()))+'.json'
        self.logobj    = logss.log_factory(self.logspath,(self.name_log))
        self.list_bak      = self.makejson_bak(self.name_json,self.bakpath,self.jsonpath,self.checkdays)
        self.list_check    = self.makejson(self.name_json,self.checkpath,self.jsonpaths)
        # self.show()
        self.logobj.info('实例化成功:检测目录：{0} 备份目录: {1} 工作目录:{2} 日志目录:{3},json目录:{4},间隔时间:{5}'\
                         .format(self.checkpath,self.bakpath,self.workpath,self.logspath,self.logspath, self.timesleep))


    def show(self):
        print '检测目录：',self.checkpath,\
                '\n备份目录：',self.bakpath,\
                '\n工作目录:;',self.workpath,\
                '\n日志目录:',self.logspath,\
                '\njson目录:',self.logspath, \
                '\n间隔时间:', self.timesleep,



    def makejson(self,filename,tagpath,jsonpath):
        msg ,list= path_to_json.file_to_jsonfile(filename,tagpath,jsonpath)
        self.logobj.info(msg)
        return list
    def makejson_bak(self,filename,tagpath,jsonpath,n_days):
        msg ,list= path_to_json.file_to_jsonfile_0(filename,tagpath,jsonpath)
        self.logobj.info(msg)
        return list

    def ckeckfile(self):
        for k,v in self.list_check.items():          #遍历异常目录
            for k1,v1 in self.list_bak.items():      #遍历备份录目录
                print v,v1
                if v in v1:
                    self.makefile(k,v,k1,v1)
                    self.logobj.info('{}文件匹配到了{}文件，接下来比较两文件是否相同'.format(v,v1))
                else:
                    self.logobj.info('{}文件与{}文件不匹配'.format(v,v1))

    def makefile(self,path,file,path1,file1):
        self.mvfile(path1,self.tarpath+file1)
        # self.untar(file1)
        self.unzip_dir(self.tarpath+file1,self.tarpath)
        print 'test:  ' + path,file ,path1,file1
        if self.checkfile(path,self.tarpath+file):             #如果两个文件一样，返回true，否则返回 false
            self.logobj.info('异常文件 {}与备份文件的文件相同，完全查重处理'.format(file))
            pass
        else:
            self.mvfile(self.tarpath+file,self.workpath+file)  #如果不通就把解压的放到工作目录
            self.logobj.info('异常文件 {}与备份文件的文件不同，将解压好的文件移动到工作目录'.format(file))


    def mvfile(self,file1,file2):
        shutil.copy(file1, file2)


    def untar(self,file_name):

        tar = tarfile.open(self.tarpath+file_name)
        names = tar.getnames()
        # if os.path.isdir(file_name + "_files"):
        #     pass
        # else:
        #     os.mkdir(file_name + "_files")
        #由于解压后是许多文件，预先建立同名文件夹
        for name in names:
            tar.extract(name, self.tarpath)
        tar.close()

    def unzip_dir(self,srcname, dstPath):
        print srcname, dstPath
        zipHandle = zipfile.ZipFile(srcname, "r")
        for filename in zipHandle.namelist():
            print filename
        zipHandle.extractall(dstPath)  # 解压到指定目录
        self.logobj.info('解压文件')
        zipHandle.close()


    def checkfile(self,file1, file2):  # 检测文件是否相同的函数
        print file1,file2
        a =filecmp.cmp(file1, file2)
        if a :
            self.logobj.info('{} 与 {}相同'.format(file1,file2))
        else:
            self.logobj.info('{}与 {}不同'.format(file1,file2))
        return a
    def __del__(self):


        delDir = self.tarpath
        delList = os.listdir(delDir)

        for f in delList:
            filePath = os.path.join(delDir, f)
            if os.path.isfile(filePath):
                os.remove(filePath)
                print filePath + " was removed!"
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath, True)
            print "Directory: " + filePath + " was removed!"

        print '完成一次检查'





def main():
    s =  works('con.ini')
    s.ckeckfile()
    s.__del__()

if __name__=='__main__':
    main()