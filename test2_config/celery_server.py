# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 11:22
# @Author  : Rickzuo
# @File    : celery_server
# @Software: PyCharm

from celery import Celery

app = Celery('tasks')

#加载配置模块
app.config_from_object('celeryconfig')
