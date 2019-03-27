# celery_example
分享Celery用到的三个例子

### test1_worker
- 最初始的例子
    - 包含普通函数装饰为 celery task
    - bind=True 具有task类的属性功能
    - 多个task有共同特性的时候，建议创建一个抽象task父类
    - Task类定义task
    
 
     
### test1_worker2
- 将test1_worke的celery app和tasks拆分，放到不同文件


### test2_worker
- 使用到celeryconfig文件配置celery



### test3_django
- django中使用celery，不推荐直接使用django_celery包

