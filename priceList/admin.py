# -*- coding: utf-8 -*-
__author__ = 'bteam'
from django.contrib import admin
from models import *

class MarkPriceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','mark','price',)
    list_filter = ('mark','brick__view','brick__color','brick__width__name','brick__price__date')

class PriceListAdmin(admin.ModelAdmin):
    pass

class ColorAdmin(admin.ModelAdmin):
    pass

class BrickAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "mark_price":
            id = request.path.split('/')[-2]
            try: kwargs["queryset"] = MarkPrice.objects.filter(brick=self.model.objects.get(pk=id))
            except ValueError: kwargs["queryset"] = MarkPrice.objects.filter(brick__pk=None)

        return super(BrickAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
#    pass

class WidthAdmin(admin.ModelAdmin):
    pass

admin.site.register(MarkPrice,MarkPriceAdmin)
admin.site.register(Width,WidthAdmin)
admin.site.register(Brick,BrickAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(PriceList,PriceListAdmin)
