#!/usr/bin/python
# -*- coding:utf-8 -*-


import ConfigParser



conf = ConfigParser.ConfigParser()
conf.read('con.ini')
 
conf.set("section1", "name", "jhao1i04")    # 修改指定section 的option
conf.set("section1", "age", "21")       # 增加指定section 的option
conf.add_section("section3")         # 增加section
conf.set("section3", "site", "oschina.net")  # 给新增的section 写入option
conf.write(open('con.ini', 'w'))


