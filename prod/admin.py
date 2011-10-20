# -*- coding: utf-8 -*-
__author__ = 'bteam'
# -*- coding: utf-8 -*-
__author__ = 'bteam'
from django.contrib import admin
from models import *


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product,ProductAdmin)