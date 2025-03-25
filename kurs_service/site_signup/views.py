from django.http import HttpResponse
from django.shortcuts import render


def site_signup(request):
    context = {
        'title': 'Регистрация | OOO &quot;КУРС&quot;',
    }
    return render(request, "site_signup/site_signup.html", context=context)
