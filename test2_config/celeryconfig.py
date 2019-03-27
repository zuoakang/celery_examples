# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 14:58
# @Author  : Rickzuo
# @File    : celeryconfig
# @Software: PyCharm


from datetime import timedelta
from celery.schedules import crontab

#参数文档
#http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_acks_late

#broker
BROKER_URL = 'redis://192.168.56.1:6379/0'
#backen
CELERY_RESULT_BACKEND = 'redis://192.168.56.1:6379/1'
#导入任务，如tasks.py
CELERY_IMPORTS = ('tasks', )
#列化任务载荷的默认的序列化方式
CELERY_TASK_SERIALIZER = 'json'

# 任务发送完成是否需要确认，这一项对性能有一点影响
CELERY_ACKS_LATE = True


# celery worker的并发数，默认是服务器的内核数目,也是命令行-c 10 或者--concurrency=10参数指定的数目
CELERYD_CONCURRENCY = 10

# celery worker 每次去redis预取任务的数量
CELERYD_PREFETCH_MULTIPLIER = 10
# 每个worker执行了多少任务就会死掉，默认是无限的
#CELERYD_MAX_TASKS_PER_CHILD = 10
#限制任务的速率，这样每分钟只允许处理 10 个该类型的任务
CELERY_ANNOTATIONS = {
    'tasks.add_num': {'rate_limit': '10/m'}
}

#结果序列化方式
CELERY_RESULT_SERIALIZER = 'json'

CELERY_ACCEPT_CONTENT=['json']
#时间地区与形式
CELERY_TIMEZONE = 'Asia/Shanghai'
#时间是否使用utc形式
CELERY_ENABLE_UTC = True


#borker池，默认是10
BROKER_POOL_LIMIT = 10
#任务过期时间，单位为s，默认为一天
CELERY_TASK_RESULT_EXPIRES = 3600
#backen缓存结果的数目，默认5000
CELERY_MAX_CACHED_RESULTS = 10000
# 设置默认的队列名称，如果一个消息不符合其他的队列就会放在默认队列里面，如果什么都不设置的话，数据都会发送到默认的队列中
CELERY_DEFAULT_QUEUE = "default"
# 设置详细的队列
CELERY_QUEUES = {
    "default": {  # 这是上面指定的默认队列
        "exchange": "direct_exchange",
        "exchange_type": "direct", #把消息路由到那些binding key与routing_key完全匹配的Queue中
        "routing_key": "celery"
    },
    "task_a": {
        "routing_key": "task_a",
        "exchange": "direct_exchange",
        "exchange_type": "direct",
    },
    'task_b': {
        'exchange': 'fanout_exchange', #广播形式，它没有参数绑定，就是不需要指定routing_key之类的东西
        'exchange_type': 'fanout'
    },
    "task_c": {
        "routing_key": "topic.#",
        "exchange": "topic_exchange",
        "exchange_type": "topic", # 它与direct类型的Exchage相似，这里是弱匹配。它引入了两个通配符#和*前者匹配多个单词（可以为0），后者匹配一个单词
    },


}

#设置任务路由队列
CELERY_ROUTES = {
    'tasks.add_num': {
        'queue': 'task_a',
        'routing_key': 'task_a' #redis没有强匹配
     },

    # 'tasks.add_num': {
    #     'queue': 'task_b',
    #  },
    # 'tasks.add_num': {
    #     'queue': 'task_c',
    #     'routing_key': 'topic.test'
    #  },

}

#定时任务设置
CELERYBEAT_SCHEDULE = {

    'add_30_schedule': {
        "task":"tasks.add_num",
        "schedule":timedelta(seconds=1),       # 每 30 秒执行一次,
        "args":(1,2)
    },
    'add_every_day_schedule': {
        "task":"tasks.add_num",
        "schedule":crontab(hour=9, minute=50),   # 每天早上 9 点 50 分执行一次
        "args":(1,2)
    }
}