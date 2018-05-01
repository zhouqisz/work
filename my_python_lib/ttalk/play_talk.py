# encoding: utf-8
# -*- coding: UTF-8 -*-


"""
@author: zhouqi
@software: PyCharm
@file: play_talk.py
@time: 2018/1/17 上午9:43
'/Users/zhouqi/Desktop/python/work/my_python_lib/ttalk/do.mp3'
"""

import time
import pygame
import ptts

file = r'do.mp3'
text = '江山如此多娇！'
ptts.tran_to(text,file)

pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(2)
pygame.mixer.music.stop()
"""
wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocksR.sh && chmod +x shadowsocksR.sh





Congratulations, ShadowsocksR server install completed!
Your Server IP        :  104.199.179.4  ->35.201.194.240
Your Server Port      :  2025 
Your Password         :  z12345678 
Your Protocol         :  origin 
Your obfs             :  plain 
Your Encryption Method:  aes-256-cfb 
Welcome to visit:https://shadowsocks.be/9.html
Enjoy it!
root@zhouqi-0:~# 
"""
