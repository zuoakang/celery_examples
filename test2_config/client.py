# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 14:08
# @Author  : Rickzuo
# @File    : main.py
# @Software: PyCharm
import time
from tasks import add_num

#不指定队列
result = [add_num.delay(i, 0) for i in range (60)]

#指定task_a/task_b队列
#result = [add_num.apply_async((i, 0),queue="task_a") for i in range (60)]

#从配置文件中指定队列
result = [add_num.apply_async((i, 0)) for i in range (60)]

'''
2.优先任务
'''

#result = [add_num.apply_async((i, 0),queue="celery",priority=i) for i in range (3)]
# result=add_num.apply_async((1, 0),priority=5)
# result=add_num.apply_async((2, 0),priority=2)
# result=add_num.apply_async((3, 0),priority=0)

print(result)