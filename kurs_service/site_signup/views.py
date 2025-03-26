from django.http import HttpResponse
from django.shortcuts import render


def site_signup(request):
    context = {
        'title': 'Регистрация | OOO "КУРС"',
    }
    return render(request, "site_signup/site_signup.html", context=context)
