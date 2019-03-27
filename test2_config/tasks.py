# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 11:12
# @Author  : Rickzuo
# @File    : tasks.py
# @Software: PyCharm
import time
from celery_server import app

@app.task
def add_num(x, y):
    #time.sleep(3)
    return x + y
