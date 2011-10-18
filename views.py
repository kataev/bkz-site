from django.shortcuts import render,get_object_or_404
from priceList.models import PriceList


def proc(request):
    try :price = PriceList.objects.latest('date')
    except PriceList.DoesNotExist: return {}
    return dict(price=price)

def main(request):
    return render(request,'index.html')

def price(request,date):
    p = get_object_or_404(PriceList,date=date)
    return render(request,'Price.html',{'priceList':p})