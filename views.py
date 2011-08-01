from dojango.util import dojo_collector
from django.shortcuts import render_to_response
from django.template import RequestContext

def main(request):
    return render_to_response('index.html',context_instance=RequestContext(request))


def about(request):
    print request.path
    return render_to_response('about.html',context_instance=RequestContext(request))