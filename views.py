from django.shortcuts import render
from priceList.models import PriceList


def proc(request):
    return dict(price=PriceList.objects.latest('date'))

def main(request):
    return render(request,'index.html')
