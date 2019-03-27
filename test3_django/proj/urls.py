from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from django.urls import path, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from demoapp import views

urlpatterns=[
    path("index/",views.index,name="index"),
    path('admin/', admin.site.urls),
]