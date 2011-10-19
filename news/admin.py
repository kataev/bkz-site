# -*- coding: utf-8 -*-
__author__ = 'bteam'
from django.contrib import admin
from models import *

class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(News,NewsAdmin)