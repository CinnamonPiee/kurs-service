from django.http import HttpResponse
from django.shortcuts import render


def site_login(request):
    context = {
        'title': 'Вход | OOO "КУРС"',
    }
    return render(request, "site_login/site_login.html", context=context)
