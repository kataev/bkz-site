# -*- coding: utf-8 -*-
__author__ = 'bteam'
from django.contrib import admin
from models import *

class PriceAdmin(admin.ModelAdmin):
    pass

class PriceListAdmin(admin.ModelAdmin):
    pass

class ColorAdmin(admin.ModelAdmin):
    pass

class BrickAdmin(admin.ModelAdmin):
    pass

admin.site.register(Brick,BrickAdmin)
admin.site.register(Price,PriceAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(PriceList,PriceListAdmin)
