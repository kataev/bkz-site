# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from priceList.models import *

def price(request):
    p = get_object_or_404(PriceList)
    return render(request,'Price.html',{'flatpage':{'content':p,'title':unicode(p),'url':'/price/'}})