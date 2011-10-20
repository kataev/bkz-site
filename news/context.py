# -*- coding: utf-8 -*-
__author__ = 'bteam'
from models import *

def news(request):
    return dict(news=News.objects.filter(show=True)[:5])