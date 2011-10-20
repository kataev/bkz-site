# -*- coding: utf-8 -*-
from priceList.models import PriceList

__author__ = 'bteam'

def price(request):
    try :price = PriceList.objects.latest('date')
    except PriceList.DoesNotExist: return {}
    return dict(price=price)