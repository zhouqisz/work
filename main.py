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
        self.name_log  = time.strftime('%Y%m%d',time.localtime(time.time()))+'.log'
        self.name_json= time.strftime('%Y%m%d', time.localtime(time.time()))+'.json'
        self.logobj    = logss.log_factory(self.logspath,(self.name_log))
        self.list_bak      = self.makejson(self.name_json,self.bakpath,self.jsonpath)
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


    def ckeckfile(self):
        for k,v in self.list_check.items():          #遍历异常目录
            for k1,v1 in self.list_bak.items():      #遍历备份录目录
                if v in v1:
                    self.makefile(v,k,k1,v1)
                    self.logobj.info('{}文件匹配到了{}文件，接下来比较两文件是否相同')
                else:
                    self.logobj.info('{}文件匹配不到了{}文件')

    def makefile(self,path,file,path1,file1):
        self.mvfile(path1,self.tarpath+file1)
        self.untar(self,file1)
        if self.checkfile(path,self.tarpath+file):             #如果两个文件一样，返回true，否则返回 false
            self.logobj.info('异常文件 %与备份文件的文件相同，完全查重处理'%file)
            pass
        else:
            self.mvfile(self.tarpath+file,self.workpath+file)  #如果不通就把解压的放到工作目录
            self.logobj.info('异常文件 %与备份文件的文件不同，将解压好的文件移动到工作目录'%file)


    def mvfile(self,file1,file2):
        shutil.move(file1, file2)


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




    def checkfile(self,file1, file2):  # 检测文件是否相同的函数

        return filecmp.cmp(file1, file2)

def main():
    s =  works('con.ini')
    s.ckeckfile()

if __name__=='__main__':
    main()