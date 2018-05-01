
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouqi
@software: PyCharm
@file: bigdog.py
@time: 2018/4/25 下午10:10

在进行web开发时，后台的源代码需经过频繁地修改与测试，若每次修改完代码再去手动重启服务器测试，则会导致开发效率严重降低。
我们可以使用watchdog来监控服务器目录下的事件，当事件发生时执行我们指定的重启服务器操作
"""
command python3 bigdog.py web.py

import os, sys, time, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def log(s):
    # 记录格式
    print("[Wangwang] %s" % s)

# 继承事件处理基类
class MyBigdogHandler(FileSystemEventHandler):

    def __init__(self, fn):
        super().__init__()
        # 初始化重启服务器方法
        self.restart = fn

    # 重写事件处理方法
    def on_any_event(self, event):
        # 只监控python代码的文件
        if event.src_path.endswith('.py'):
            log("Python source file changed %s" % event.src_path)
            # 重启服务器
            self.restart()


command = ['echo', 'ok']
process = None

# 终止服务进程
def kill_process():
    global process
    if process:
        log("Kill process [%s]..." % process.pid)
        process.kill()
        process.wait()
        log("Process ended with code %s" % process.returncode)
        process = None

# 开始服务进程
def start_process():
    global process, command
    log("Start process %s..." % ' '.join(command))
    # 创建进程用于运行服务器进程，重定向输入输出
    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

# 重启服务进程
def restart_process():
    kill_process()
    start_process()

# 开始监控
def start_watch(path, callback):
    # 获得监控对象
    bigdog = Observer()
    # 配置监控对象
    bigdog.schedule(MyBigdogHandler(restart_process), path, recursive=True)
    # 开始监控
    bigdog.start()
    log("Watching directory %s..." % path)
    # 启动服务进程
    start_process()
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        bigdog.stop()
    bigdog.join()

if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv:
        print("Usage: ./pymonitor your-script.py")
        exit(0)
    if argv[0] != 'python3':
        argv.insert(0, 'python3')
    command = argv
    # 监控当前目录
    path = os.path.abspath('.')
    start_watch(path, None)