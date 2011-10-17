from dojango.util import dojo_collector
from django.shortcuts import render
from django.template import RequestContext

def proc(request):
    return dict(price=u'price text')


def main(request):
    return render(request,'index.html')
