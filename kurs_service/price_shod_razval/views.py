from django.http import HttpResponse
from django.shortcuts import render


def price_shod_razval(request):
    context = {
        'title': 'Прайс развал-схождение | OOO &quot;КУРС&quot;',
    }
    return render(request, "price_shod_razval/price_shod_razval.html", context=context)
