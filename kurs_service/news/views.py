from django.http import HttpResponse
from django.shortcuts import render


def news(request):
    context = {
        'title': 'Новости | OOO "КУРС"',
    }
    return render(request, "news/news.html", context=context)
