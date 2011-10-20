# -*- coding: utf-8 -*-
from models import *
from django.shortcuts import render,get_object_or_404

def news(request,id):
    n = get_object_or_404(News,id=id)
    return render(request,'index.html',{'flatpage':n})
