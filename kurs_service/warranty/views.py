from django.http import HttpResponse
from django.shortcuts import render


def warranty(request):
    context = {
        'title': 'Гарантия | OOO "КУРС"',
    }
    return render(request, "warranty/warranty.html", context=context)
