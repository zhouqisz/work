# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: falcondemo.py
@time: 2018/5/1 下午5:22
"""
import falcon

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        print 'get'

        resp.media = quote

api = falcon.API()
api.add_route('/quote', QuoteResource())
