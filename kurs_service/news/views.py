from django.http import HttpResponse
from django.shortcuts import render


def news(request):
    context = {
        'title': 'Новости | OOO &quot;КУРС&quot;',
    }
    return render(request, "news/news.html", context=context)
