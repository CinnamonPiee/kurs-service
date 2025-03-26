from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'Главная страница | OOO "КУРС"',
    }
    return render(request, "main_page/main_page.html", context=context)
