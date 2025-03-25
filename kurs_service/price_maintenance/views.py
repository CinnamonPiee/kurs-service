from django.http import HttpResponse
from django.shortcuts import render


def price_maintenance(request):
    context = {
        'title': 'Прайс технического обслуживания | OOO &quot;КУРС&quot;',
    }
    return render(request, "price_maintenance/price_maintenance.html", context=context)
