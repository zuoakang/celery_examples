# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery.task import task


@task
def add(x, y):
    return x + y


@task
def mul(x, y):
    return x * y


@task
def xsum(numbers):
    return sum(numbers)
