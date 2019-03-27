# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 13:08
# @Author  : Rickzuo
# @File    : celery_server
# @Software: PyCharm
from celery import Celery

app = Celery('demo',
             backend='redis://192.168.56.1:6379/0',
             broker='redis://192.168.56.1:6379/1')