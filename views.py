from django.shortcuts import render
from priceList.models import PriceList


def proc(request):
    try :price = PriceList.objects.latest('date')
    except PriceList.DoesNotExist: return {}
    return dict(price=price)

def main(request):
    return render(request,'index.html')
