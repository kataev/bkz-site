# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from priceList.models import *

def price(request):
    p = get_object_or_404(PriceList)
#    q = p.brick_set.all()
#    color = ''
#    for m in range(len(q)-1):
#        if q[m+1].color.name!=color:
#            q[m].col+=1
#        color = q[m].color.name
#    p.brick = q

    return render(request,'Price.html',{'flatpage':{'content':p,'title':unicode(p)}})