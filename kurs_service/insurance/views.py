from django.http import HttpResponse
from django.shortcuts import render


def insurance(request):
    context = {
        'title': 'Страхование | OOO "КУРС"',
    }
    return render(request, "insurance/insurance.html", context=context)
