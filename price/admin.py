# -*- coding: utf-8 -*-
__author__ = 'bteam'
from django.contrib import admin
from models import *

class PriceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Price,PriceAdmin)
  