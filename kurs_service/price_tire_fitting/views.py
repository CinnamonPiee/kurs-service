from django.http import HttpResponse
from django.shortcuts import render


def price_tire_fitting(request):
    context = {
        'title': 'Прайс развал-схождение | OOO &quot;КУРС&quot;',
    }
    return render(request, "price_tire_fitting/price_tire_fitting.html", context=context)
