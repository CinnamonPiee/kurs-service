from django.shortcuts import render
from news.models import NewsContent


def news(request):
    context = {
        'title': 'Новости | OOO "КУРС"',
        'news_content': NewsContent.objects.all(),
    }
    return render(request, "news/news.html", context=context)
