from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    context = {
        'title': 'О сервисе | OOO "КУРС"',
    }
    return render(request, "about/about.html", context=context)
