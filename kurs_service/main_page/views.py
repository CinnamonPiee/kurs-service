from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'Главная страница | OOO &quot;КУРС&quot;',
        'text': 'Main page',
    }
    return render(request, "main_page/index.html", context=context)
