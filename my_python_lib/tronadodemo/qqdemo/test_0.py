
# -*- encoding: utf-8 -*-

"""
@author: zhouqi
@software: PyCharm
@file: test_0.py
@time: 2017/8/17 下午9:00
"""

import textwrap

import tornado.web
from tornado import  web
from tornado import  httpserver
from  tornado import  ioloop
import io
# import  check_code

class IndexHander(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello worfld!')


class LoginHander(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('登陆界面！')
        # self.render('html1.html')


        def post(self, *args, **kwargs):
            username = self.get_argument('username')
            password = self.get_argument('password')
            if username == 'admin' and password == '123456':
                self.write('登陆成功！')
            else:
                self.write('登陆失败！')

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))



# class ImgHandler(web.RequestHandler):
#     def

def make_app():
    return tornado.web.Application([
        (r"/index", IndexHander),
        (r"/login", LoginHander),
        (r"/reverse/(\w+)",ReverseHandler),
        (r"/wrap",WrapHandler),
    ])

if __name__ == '__main__':
    import tornado
    # print('zhouqi')
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()