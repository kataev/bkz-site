# -*- coding: utf-8 -*-
from models import *
from django.shortcuts import render,get_object_or_404

def products(request):
    n = {'title':'Продукция','content':Product.objects.all(),'url':'/products/'}
    return render(request,'Products.html',{'flatpage':n})
