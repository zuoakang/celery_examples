# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 14:08
# @Author  : Rickzuo
# @File    : main.py
# @Software: PyCharm
import time
from tasks import add_num, divide_num, divide_num2, divide_num3

'''
1.返回的一些参数
'''
# result=add_num(1, 2)
# print(result)
#result=add_num.delay(1, 2)
#print(result)
# print(result.task_id,result.status)
# print(result.successful(),result.ready())
# print(result.get()) #阻塞
# print(result.successful(),result.ready(),result.status)


#取消task
#add_num.apply_async(args=[2, 2], countdown=120)
#result.revoke()


#重试
#result=divide_num.apply_async(args=[2, 0])
#print(result)

#子任务
#add.s(1) 语句将会创建一个 signature 对象，chain : 调用连, 前面的执行结果, 作为参数传给后面的任务, 直到全部完成, 类似管道。add_num(divide_num(1, 2), 3)
#result=add_num.apply_async((1, 2), link=divide_num.s(3))
#result=(add_num.s(2, 2) | divide_num.s(2)).delay()

#创建任务组 一次创建多个(一组)任务.
from celery import group
res = group(add_num.s(i, i) for i in range(20))()
print(res)



