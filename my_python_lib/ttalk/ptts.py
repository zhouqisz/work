# -*- coding: UTF-8 -*-
"""
@author: zhouqi
@software: PyCharm
@file: ptts.py
@time: 2018/1/16 下午10:15
"""

from aip import AipSpeech
""" 你的百度 APPID AK SK
https://console.bce.baidu.com/ai/#/ai/speech/app/list       应用列表
http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top         API
"""
def tran_to(text,files):
    APP_ID = '10703745'
    API_KEY = 'ZDNGbZ6sn55DA2B59TsWl9M9'
    SECRET_KEY = 'lXHd9bkfg1bOSQzSTu3EzCO76vgRavMU'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result  = client.synthesis(text, 'zh', 1, {
        'vol': 3,'spd':1.5,'per': 3,
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(files, 'wb') as f:
            f.write(result)