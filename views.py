from django.shortcuts import render,get_object_or_404
from priceList.models import PriceList
from news.models import News

def proc(request):
    try :price = PriceList.objects.latest('date')
    except PriceList.DoesNotExist: return {}
    return dict(price=price,news=News.objects.all()[:5])

def main(request):
    return render(request,'index.html')

def price(request,date):
    p = get_object_or_404(PriceList,date=date)
    q = p.brick_set.all()
    color = ''
    for m in range(len(q)-1):
        if q[m+1].color.name!=color:
            q[m].col+=1
        color = q[m].color.name
    p.brick = q

    return render(request,'Price.html',{'priceList':p})