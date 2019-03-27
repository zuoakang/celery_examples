from __future__ import absolute_import, unicode_literals
# Create your views here.
from django.http import HttpResponse


def index(request):

    return  HttpResponse("hello")