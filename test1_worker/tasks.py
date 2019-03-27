# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 11:12
# @Author  : Rickzuo
# @File    : tasks.py
# @Software: PyCharm
import celery
from celery import Celery
import time
# 配置好celery的backend和broker

app = Celery('demo',
             backend='redis://192.168.56.1:6379/0',
             broker='redis://192.168.56.1:6379/1')

#值得注意的是，任务函数本质上已经不再是一个普通函数，而是一个 celery.app.task:Task 实例对象，app.task 的 “装饰” 动作，其实是 Task 的实例化过程
@app.task  # 普通函数装饰为 celery task
def add_num(x, y):
    #time.sleep(2) #异步
    return x + y










#bind=True 具有task类的属性功能
@app.task(bind=True, max_retries=3,default_retry_delay=1)
def divide_num(self,x,y):
    try:
        return x/y
    except Exception as exc:
        self.retry(exc=exc)



from celery.task import Task
class divide_num2(Task):

    def run(self, x,y, **kwargs):
        try:
            return x/y
        except Exception as exc:
            self.retry(exc=exc)

app.tasks.register(divide_num2())



'''
    多个task有共同特性的时候，建议创建一个抽象task父类
'''
class MyTask(celery.Task):

    max_retries = 3
    default_retry_delay = 1
    # 任务失败时执行
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        '''
            exc:失败时的错误的类型；
            task_id:任务的id；
            args:任务函数的参数；
            kwargs:参数；
            einfo:失败时的异常详细信息；
            retval:任务成功执行的返回值；
        '''
        print('{} failed: {}'.format(task_id, exc))

    # 任务成功时执行
    def on_success(self, retval, task_id, args, kwargs):
        print('success...')

    # 任务重试时执行
    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print('retry...')


@app.task(bind=True,base=MyTask)
def divide_num3(self,x, y):
    try:
        return x/y
    except Exception as exc:
        self.retry(exc=exc)




